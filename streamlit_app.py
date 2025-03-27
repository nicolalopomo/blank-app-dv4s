import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="My application for DV4S",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎈 My new application for DV4S!")

st.header('_Hi_ :green[DV4S]!')

st.subheader('Welcome to the class! 😇')

st.write("Let's start **building**!")

value = st.slider('Select a value: ', 0, 100, 30)

st.write('You selected: ', value)

st.markdown('<p style="color:yellow; font-size:20px;">I should be yellow</p>',
            unsafe_allow_html=True)

sports_list = ['soccer', 'basket', 'football', 'tennis']

button_pressed = st.button('Push me for Sports List', type="primary")

if button_pressed:
    st.write(sports_list)

check_pressed = st.checkbox('I like it!')

if check_pressed:
    st.write(sports_list)
else:
    st.write('')

chosen_item = st.radio('What sport do you like?', sports_list)

st.write('I knew that you liked ' + chosen_item)

chosen_item_again = st.selectbox('What sport do you like?', sports_list)
st.write('I knew that you liked ' + chosen_item_again)

multi_item = st.multiselect('What sports do you like?', sports_list)

age = st.slider('Your age:', 18, 65, (25, 50))
st.write('Your age is', age)

user_name = st.text_input('Your name', placeholder='Write your name here...')
st.write('Your name is:', user_name)

user_age = st.number_input('Your age:', 
                           min_value=18,
                           max_value=65,
                           value=25,
                           step=1)

match_date = st.date_input('Select date ranges',
                           value=datetime(2025, 3, 15))


with st.form('User Information'):
    user_name = st.text_input('Your name', placeholder='Write your name here...')

    user_age = st.number_input('Your age:', 
                           min_value=18,
                           max_value=65,
                           value=25,
                           step=1)
    submitted = st.form_submit_button('Submit it!')

if submitted:
    st.write('You submitted it!')