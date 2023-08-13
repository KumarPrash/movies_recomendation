import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similar[movie_index]
    # But before sorting i want to catch index of sorting movie with the help of enumerate function.
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recom=[]
    for i in movies_list:
        recom.append(movies.iloc[i[0]].title)
    return recom

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similar=pickle.load(open('similar.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommened System')
selected_movie = st.selectbox(
    'Please Select Movie. Thank-You',
    movies['title'].values)

if st.button('Recommened'):
    recommendation=recommend(selected_movie)
    for i in recommendation:
        st.write(i)