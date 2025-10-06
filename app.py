import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# --- 環境変数の読み込み ---
load_dotenv()

# --- Streamlit UI ---
st.title("💬 専門家に質問できるAIアプリ")
st.write("ラジオボタンで専門家を選び、質問を入力してAIに聞いてみよう！")

# --- 専門家の選択 ---
role = st.radio(
    "専門家の種類を選んでください：",
    ["心理学者", "料理研究家", "エンジニア", "歴史学者"]
)

# --- ユーザー入力 ---
question = st.text_input("質問を入力してください:")

# --- LLMに質問する関数 ---
def ask_expert(role, question):
    system_prompt = f"あなたは{role}です。専門家の視点からわかりやすく回答してください。"
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=question)
    ]
    response = llm.invoke(messages)
    return response.content

# --- ボタン押下で実行 ---
if st.button("送信") and question:
    with st.spinner("AIが考え中です..."):
        answer = ask_expert(role, question)
        st.success("回答：")
        st.write(answer)
