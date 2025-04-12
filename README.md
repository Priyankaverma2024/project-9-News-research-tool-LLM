
# 📰 LLM-News Research Tool

A powerful research assistant that leverages LLM (Groq's LLaMA3), LangChain, and NewsAPI to fetch, summarize, and analyze live news articles. Built with Streamlit for an interactive interface.

---

## 🚀 Features

- 🔍 Search live news based on user queries
- 🧠 Summarize articles using LLaMA3 via Groq API
- 🧱 LangChain integration for smart prompt handling
- 🌐 Streamlit app for easy user interaction
- 🔐 .env support for API key security

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**: NewsAPI, Groq (LLaMA3)
- **Libraries**: LangChain, dotenv, requests

---

## 📦 Installation

```bash
git clone https://github.com/your-username/LLM-News-Research-Tool.git
cd LLM-News-Research-Tool
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

### **🚦Run the App**
       streamlit run app.py

###  **📁 Project Structure**
       LLM-News-Research-Tool/
│
├── app.py
├── langchain_config.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

