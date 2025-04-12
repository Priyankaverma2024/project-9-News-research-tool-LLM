# Environment & Imports
from dotenv import load_dotenv
load_dotenv()  #  Loads environment variables (like your API keys) from the .env file.
# Imports Streamlit, a Python library for building interactive web apps with just Python.
import streamlit as st
from langchain_config import llm_chain, get_summary

# Add title and description
st.title("News Research Tool")
st.write("Enter your query to get the latest news articles summarized.")
# user unput
query = st.text_input("Query")
# Action BUtton
if st.button("Get News"):

#News Summary Generation
    if query:
        with st.spinner("Fetching news and generating summary..."): # Add spinner
            try: # Add try Block
                summaries = get_summary(query)
                response = llm_chain.run({"query": query ,"summaries": summaries})
                st.write("### Summary:")
                st.write(response)
            except Exception as e: # add except block
                st.error(f"An error occured :{e}")
        
    else:
        st.write("Please enter a query.")
