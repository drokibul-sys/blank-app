


import streamlit as st
from google import genai

st.set_page_config(page_title="My Personal AI", page_icon="🤖")

st.title("🤖 My Personal AI Assistant")
st.write("Hello! I am your personal AI assistant.")

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            answer = response.text
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )




