import  streamlit as st
import requests

POE_API_URL ="https://api.poe.com/v1/chat/completions"
POE_API_KEY="sk-poe-MjhH3Icmmm2EsGarbnOn0NDXnDd2XCIa3F1LI"
POE_HEADERS={
    "Authorization": f"Bearer {POE_API_KEY}",
    "Content-Type": "application/json"
}

requests_body = {
    "model": "Gemini-3.5-Flash", 
    "messages": [
        {"role": "system", "content" :"You are a helpful tutor"},
        {"role": "user", "content": "Explain GET and POST in one sentence each."}
    ]
}

st.title("Echo Bot")
user_message = st.chat_input("Type a message")\

if user_message:

    st.chat_message("user").write(user_message)
    st.chat_message("assistant").write(f"You said : {user_message}")

if "message" not in st.session_state:
    st.session_state.message = []

if user_message:
    st.session_state.message.append({"role": "user", "content":user_message})
    st.request_body = {
        "model": "Gemini-3.5-Flash", 
        "messages":st.session_state.messages
        }
    with st.spinner("Thinking..."):
        ai_response = requests.post(
            POE_API_URL,
            headers=POE_HEADERS,
            json=requests_body,
            timeout=30
        )
        ai_response.raise_for_ststus()
        reply = ai_response.json["choices"][0][message][content]

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])



response = requests.post(
    POE_API_URL,
    headers=POE_HEADERS,
    json = requests_body,
    timeout=30
)
response_body = response.json()
reply = response_body["choices"][0]["message"]["content"]
print(reply)