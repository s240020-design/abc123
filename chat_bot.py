import  streamlit as st

st.title("Echo Bot")
user_message = st.chat_input("Type a message")\

if user_message:

    st.chat_message("user").write(user_message)
    st.chat_message("assistant").write(f"You said : {user_message}")