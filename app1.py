import requests
import streamlit as st

st.title("Classroom Forum")
st.header("All class comments")

BASE_URL = "https://ai-edu.sillykeungvalley.tech/api/v1/applications"
COMMENTS_URL = f"{BASE_URL}/comments"

response =requests.get(COMMENTS_URL)
response.raise_for_status()
response_body = response.json()
comments = response_body["comments"]

for comment in comments:
    st.subheader(comment["name"])
    st.write(comment["message"])
    st.divider()

left_column, right_column = st.columns(2)

with left_column:
    st.header("Leave a comment")

with right_column:
    st.header(All class comment)

with st.form('comment_form'):
    name = st.text_input("Your name")
    passcode = st.text_input("Your passcode",type="password")
    message = st.text_area(Your comment)
    submitted = st.form_submit_button("Post comment")

if submitted:
    response_body = {
        "name": "Maya" , "passcode": "123456" , "message" : "Great lesson!"
    }

    post_response = requests.post(COMMENTS_URL)