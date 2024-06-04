import os
import streamlit as st
from openai import AzureOpenAI    

client = AzureOpenAI(    
  azure_endpoint="https://provider-openai-2.openai.azure.com/",     
  api_key="84a58994fdf64338b8c8f0610d63f81c",      
  api_version="2024-02-01"    
)

#print(client.models.list())

with st.sidebar:
    openai_api_key = st.text_input("API Key", key="chatbot_api_key", type="password")

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
  if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()

  st.session_state.messages.append({"role": "user", "content": prompt})
  st.chat_message("user").write(prompt)

  response = client.chat.completions.create(model="chatbot-model", messages=st.session_state.messages)
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

  msg = response.choices[0].message.content
  st.session_state.messages.append({"role": "assistant", "content": msg})
  st.chat_message("assistant").write(msg)