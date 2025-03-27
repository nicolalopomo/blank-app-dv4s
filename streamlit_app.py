import streamlit as st

st.title("🎈 My new application for DV4S!")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

value = st.slider('Select a value: ', 0, 100, 30)

st.write('You selected: ', value)


