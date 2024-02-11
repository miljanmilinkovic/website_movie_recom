import streamlit as st
import numpy as np
import pandas as pd
import requests
from streamlit_player import st_player

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)

if 'agree' not in st.session_state:
    st.session_state.agree = [False, False, False, False]
st.session_state.predict_movies = False
if 'list_of_favorites' not in st.session_state:
    st.session_state.list_of_favorites = []
if 'already_presented_list' not in st.session_state:
    st.session_state.already_presented_list = []
if 'titles_to_present' not in st.session_state:
    st.session_state.titles_to_present = []
if 'links_to_present' not in st.session_state:
    st.session_state.links_to_present = []
if 'promt' not in st.session_state:
    st.session_state.prompt = ''

#st.session_state.agree[0] = st.checkbox('add to favorites', key='agree0')


if 'show_movies' not in st.session_state:
    st.session_state.show_movies = False


#prompt = st.chat_input("Say something")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")
# '''
# ### Prompt a movie summary:
# '''



with st.sidebar:
    # To Do implement max length of 500 characters input
    st.session_state.promt = st.text_area('Summarise the movie:', 'man in midlife crisis searches for meaning in life')
    if st.button('generate recommendations'):
        st.session_state.predict_movies = True
        st.session_state.show_movies = True

    # if st.session_state.show_movies == True:
    #     # Create two columns
    #     col1, col2 = st.columns([0.8,0.25])
    #     # Add widgets to each column
    #     with col1:
    #         for j in range(len(st.session_state.list_of_favorites)):
    #             st.write(st.session_state.list_of_favorites[j])
    #     with col2:
    #         if  st.button("Remove"):
    #             st.session_state.list_of_favorites = []


number_of_recommendations = 15
user_input = {'prompt': st.session_state.promt,
              'n_recom': number_of_recommendations,
              'favs': st.session_state.list_of_favorites}

url = 'https://firstworkingimage-qgokkfvvpq-ew.a.run.app/predict'

if st.session_state.predict_movies:
    st.session_state.predict_movies = False
    st.session_state.already_presented_list.extend(st.session_state.titles_to_present)

    #response = requests.get(url, params=user_input)
    #data = response.json() #=> {wait: 64}
    # data = {"Our recommendation is": list_of_titles}
    # st.write('Our recommendations are:')
    # for recommendation in data['Our recommendation is']:
    #     st.write(recommendation)
    # #else:
    #     #st.write('Error:', response.status_code)
    api_return_movie_list = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Godfather: Part II', 'The Lord of the Rings: The Return of the King', 'Forrest Gump', 'The Matrix', 'The Silence of the Lambs', 'The Green Mile', 'The Departed', 'Ex Machina', 'The Prestige', 'The Sixth Sense', 'The Usual Suspects', 'The Game']
    api_return_movie_links = ['https://www.youtube.com/watch?v=6hB3S9bIaco',
    'https://www.youtube.com/watch?v=sY1S34973zA',
    'https://www.youtube.com/watch?v=_PZpmTj1Q8Q',
    'https://www.youtube.com/watch?v=9O1Iy9od7-A',
    'https://www.youtube.com/watch?v=r5X-hFf6Bwo',  # The Lord of the Rings: The Return of the King
    'https://www.youtube.com/watch?v=bLvqoHBptjg',  # Forrest Gump
    'https://www.youtube.com/watch?v=Q8g9zL-JL8E',  # The Matrix
    'https://www.youtube.com/watch?v=W6Mm8Sbe__o',  # The Silence of the Lambs
    'https://www.youtube.com/watch?v=Ki4haFrqSrw',  # The Green Mile
    'https://www.youtube.com/watch?v=auYbpnEwBBg',   # The Departed
    'https://www.youtube.com/watch?v=bggUmgeMCdc',  # Ex Machina
    'https://www.youtube.com/watch?v=o4gHCmTQDVI',  # The Prestige
    'https://www.youtube.com/watch?v=VG9AGf66tXM',  # The Sixth Sense
    'https://www.youtube.com/watch?v=KSqL9ygBCck',  # The Usual Suspects
    'https://www.youtube.com/watch?v=0kqQNBR09Rc'  # The Game
    ]

    # empty list for new recommendations
    st.session_state.titles_to_present = []
    st.session_state.links_to_present = []
    i = 0
    for index, title in enumerate(api_return_movie_list):
        if len(st.session_state.titles_to_present) < 4 and title not in st.session_state.already_presented_list:
            st.session_state.titles_to_present.append(title)
            st.session_state.links_to_present.append(api_return_movie_links[index])
            #st.write(api_return_movie_list[index])



#st.write(st.session_state.titles_to_present)
#st.write(st.session_state.links_to_present)
#st.session_state.list_of_favorites = []
if st.session_state.show_movies:
    for n in range(len(st.session_state.titles_to_present)):
        st_player(st.session_state.links_to_present[n], key=f'player{n}')
        st.session_state.agree[n] = st.checkbox('add to favorites', value = False, key= f'agree{n}')
        st.write('')


        if st.session_state.agree[n]:
            if st.session_state.titles_to_present[n] not in st.session_state.list_of_favorites:
                st.session_state.list_of_favorites.append(st.session_state.titles_to_present[n])
        else:
            if st.session_state.titles_to_present[n] in st.session_state.list_of_favorites:
                st.session_state.list_of_favorites.remove(st.session_state.titles_to_present[n])

with st.sidebar:
    # if st.session_state.show_movies == True:
        # Create two columns
        # col1, col2 = st.columns([0.8,0.25])
        # # Add widgets to each column
        # with col1:
        #     for j in range(len(st.session_state.list_of_favorites)):
        #         st.write(st.session_state.list_of_favorites[j])
        # with col2:
        #     if len(st.session_state.list_of_favorites) > 0:
        #         if  st.button("Remove"):
        #             st.session_state.list_of_favorites = []
        #             st.session_state.agree[0] = False

    if len(st.session_state.list_of_favorites) > 0:
        st.write('')
        st.write('')
        st.markdown("⭐ **Favorites:**")
        for j in range(len(st.session_state.list_of_favorites)):
            st.write('  ',st.session_state.list_of_favorites[j])
        # if st.button('refine search'):
        #     st.session_state.predict_movies = True
