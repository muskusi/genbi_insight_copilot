# 📊 GenBI Insight Copilot

**GenBI Insight Copilot** is an AI-powered business intelligence assistant built using Streamlit, LangChain, and LLMs. It allows users to upload CSV files, explore data using natural language, and forecast revenue trends using Prophet.

---

## 🚀 Features

- 📁 Upload CSV files for analysis
- 💬 Ask natural language questions about your data
- 🔍 Get instant AI-powered insights using LLMs
- 📈 Forecast future revenue trends with Prophet
- 🖼️ Visualize data and forecasts interactively using Streamlit
- ✅ Error handling for invalid questions or data issues

---

## 🧑‍💻 Technologies Used

- Python 3.10
- Streamlit
- LangChain
- OpenRouter (LLM API)
- Prophet (for time series forecasting)
- Pandas & Matplotlib

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/muskusi/genbi_insight_copilot.git
   cd genbi_insight_copilot

2. Create and activate a virtual environment:
 ```bash
   python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
```bash
###  4. Create a .env file and add your OpenRouter API key
OPENAI_API_KEY="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"
```
```bash
###  5. Run the app
streamlit run streamlit_app.py
```
