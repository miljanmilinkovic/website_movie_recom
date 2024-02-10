import streamlit as st
import numpy as np
import pandas as pd
import requests
from streamlit_player import st_player



#prompt = st.chat_input("Say something")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")
# '''
# ### Prompt a movie summary:
# '''
predict_movies = False
with st.sidebar:
    promt = st.text_area('Prompt a movie summary:', 'man in midlife crisis searches for meaning in life')
    if st.button('generate recommendations'):
        predict_movies = True
    # print is visible in the server output, not in the page

# promt = str(promt)

# with st.sidebar:
#     messages = st.container(height=300)
#     if prompt := st.chat_input("Say something"):
#         messages.chat_message("user").write(prompt)
#         messages.chat_message("assistant").write(f"Echo: {prompt}")

# '''
# ## How many recommendations do you want?
# '''

# number_of_recommendations = st.slider('Select number of passengers', 1, 10, 1)

# st.write('getting', number_of_recommendations, 'recommendations!')

number_of_recommendations = 4
user_input = {'prompt': promt,
              'n_recom': number_of_recommendations}

url = 'https://firstworkingimage-qgokkfvvpq-ew.a.run.app/predict'

show_movies = False
if predict_movies:
    #response = requests.get(url, params=user_input)
    #data = response.json() #=> {wait: 64}
    # data = {"Our recommendation is": list_of_titles}
    # st.write('Our recommendations are:')
    # for recommendation in data['Our recommendation is']:
    #     st.write(recommendation)
    # #else:
    #     #st.write('Error:', response.status_code)
    list_of_titles = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Godfather: Part II']
    list_of_links = ['https://www.youtube.com/watch?v=6hB3S9bIaco',
    'https://www.youtube.com/watch?v=sY1S34973zA',
    'https://www.youtube.com/watch?v=_PZpmTj1Q8Q',
    'https://www.youtube.com/watch?v=9O1Iy9od7-A']
    show_movies = True


if show_movies:
    st_player(list_of_links[0])
    agree1 = st.checkbox('add to favorites')
    st_player(list_of_links[1])
    agree2 = st.checkbox('add to favorites')
    st_player(list_of_links[2])
    st_player(list_of_links[3])



# if agree1:
#     st.write('Great!')
