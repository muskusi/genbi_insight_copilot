from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI

import pandas as pd

# Set your OpenAI key as a string

# Load your CSV
df = pd.read_csv("sales_data.csv")

# Initialize GPT model
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Build LangChain agent
agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)


# Ask your business questions
while True:
    query = input("\nAsk a question about your data (type 'exit' to quit): ")
    if query.lower() == "exit":
        break
    response = agent.invoke(query)
    print("\n🧠 Insight:", response)
