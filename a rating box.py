import streamlit as st

st.title("⭐ Community Rating Box")

left_column, right_column = st.columns(2)

with left_column:
    st.header("Leave a ratings")

with right_column:
    st.header("Recent ratings")

with left_column:
    with st.form("rating_form"):
        name = st.text_input(
            "Your name"
        )
        rating = st.slider(
            "Rating",
            1,
            5,
            5
        )
        comment = st.text_area(
            "Comment"
            )
        submitted = st.form_submit_button(
            "Submit rating"
        )
if "rating" not in st.session_state:
    st.session_state.ratings = []

if submitted:
    new_rating = {
        "name": name,
        "rating": rating,
        "comment": comment
    }
    st.session_state.rating.append(
        new_rating
    )
with right_column:
    for item in st.session_state.ratings:
        st.subheader(item["name"])
        st.write("⭐" * item["rating"])
        st.write(item["comment"])
        st.divider()