import json
import  streamlit as st
import requests

BASE_URL =  "https://ai-edu.sillykeungvalley.tech/api/v1/final"
api_response = requests.get(
    f"{BASE_URL}/bus/arrivals",
    params={"stop_id": "SCH-01"}, timeout=10,
)
api_response.raise_for_status()
api_data = api_response.json()

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("type here")

POE_API_URL ="https://api.poe.com/v1/chat/completions"
POE_API_KEY="sk-poe-MjhH3Icmmm2EsGarbnOn0F4Vr20NDXnDd2XCIa3F1LI"
POE_HEADERS={
    "Authorization": f"Bearer {POE_API_KEY}",
    "Content-Type": "application/json"
}
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    request_body = {
        "model": "Gemini-3.5-Flash",
        "messages": 
        [
            {
                "role": "system",
                "content": (
                      "Extract Stop ID",
                      'in json format: {"stop_id": "SCH-01"| "SCH-02"}| "SCH-03"}'
                      "SCH-01 is main gate",
                      "SCH-02 is MTR station side",
                      "SCH-03 is Sports ground"
                )
            },
            {
                  "role":"user",
                  "content": "Which bus should I take form Main Gate"
            },
            {
                  "role": "assistant",
                  "content": "{'stop_id': 'SCH-01'}",
            },
            {
                  "role": "user",
                  "content": "I am at Sport Ground right now"
            },
            {
                    "role": "user",
                    "content": "I am at Sport Ground right now"
            },
            {
                  "role": "assistant",
                  "content": "{'stop_id': 'SCH-03'}",
            },
            {
                   "role": "user",
                   "content": user_input
            }
        ]
    }
    with st.spinner("Thinking..."):
            ai_response = requests.post(
                POE_API_URL,
                headers=POE_HEADERS,
                json=request_body,
                timeout=30
            )
            ai_response.raise_for_status()
            reply = ai_response.json()["choices"][0]["message"]["content"]
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
                )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
                st.write(message["content"])

    context = (
          f"What bus are arriving at {api_data['stop_name']}?"
          f"{api_data['buses']}"
    )

reply_json = json.loads(reply)
    stop_id = reply_json['stop_id']

    response = request.get(
      "https://ai-edu.sillykeungvalley.tech/api/v1/final/bus/arrivals",
      params={'stop_id: stop_id'}
    )
    response_json = response.json()
    st.json(response_json)