# Imports and setup
from groq import Groq
from dotenv import load_dotenv
import os
# Environment setup
load_dotenv()
# Langchain Prompt and LLM Setup
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq 
from newsapi import NewsApiClient

# Initialize Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")
print("Loaded GROQ KEY:", os.getenv("GROQ_API_KEY"))
# Instantiates the Groq LLM (using LLaMA3-70B). temperature=0 means the output will be deterministic and less creative (good for summarization).
groq_llm = ChatGroq(api_key=groq_api_key,temperature=0 , model_name="llama3-70b-8192")  # Choose a suitable model

# Initialize NewsAPI Key
newsapi_key = os.getenv("NEWS_API_KEY") # store api key securely
newsapi = NewsApiClient(api_key=newsapi_key)

# Featching News Articles
def get_news_articles(query):
    articles = newsapi.get_everything(q=query, language="en", sort_by="relevancy")
    print(articles)  # Debug output
    return articles.get("articles", [])

# Summarizing News Descriptions
def summarize_articles(articles):
    summaries = [article["description"] for article in articles if article["description"]]
    return " ".join(summaries) # Extracts and join description fields from the articles

# Query-to-Summary Wrapper
def get_summary(query):
    articles = get_news_articles(query)
    return summarize_articles(articles) # Combine the above two articles and fatches articles->extract descriptions->return a single summary string

# Define the prompt template
template = """
You are an AI assistant helping an equity research analyst. Given the following query and the provided news article summaries, provide an overall summary.

Query: {query}
Summaries: {summaries}
"""
# Wrapes the prompt in a Langchain pipeline using the Groq LLM
prompt = PromptTemplate(template=template, input_variables=["query", "summaries"])
llm_chain = LLMChain(prompt=prompt, llm=groq_llm)

# Run the LLM pipeline
user_query="what are the latest news on IPL 2025?" 

# fetch news and summarize
articles_summary = get_summary(user_query)

# run the chain and print response
response = llm_chain.run({"query": user_query, "summaries": articles_summary})
print(response)  # Print AI-generated summary
