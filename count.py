import streamlit as st

st.title("The Broken Counter")

count = 0
if st.button("Click Me! +")
    count = count +1

st.write(f"Button clicked: {count} times")