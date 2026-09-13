import os
import streamlit as st
from agent import root_agent

# Ensure Streamlit secrets are explicitly mapped to the environment variable
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

st.title("☕ AI Coffee Barista")
st.write("Welcome! Ask me anything about our menu or recommendations.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What can I get for you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = root_agent(prompt)
            except Exception as e:
                response = f"An error occurred: {e}"
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


