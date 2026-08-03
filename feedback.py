import streamlit as st

form_title = "Workshop Feedback"
ratings = [1,2,3,4,5]
button_label = "save"

 st.title("form_title")

with st.form ('feed_back_form')
reply_json = json.loads(reply)
    stop_id = reply_json['stop_id']

    response = request.get(
      "https://ai-edu.sillykeungvalley.tech/api/v1/final/bus/arrivals",
      params={'stop_id: stop_id'}
    )
    response_json = response.json()
    st.json(response_json)