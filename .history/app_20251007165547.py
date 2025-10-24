import streamlit as st
import pickle
import requests

st.title('🎬 Movie Recommender System')

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    api_key = "YOUR_API_KEY"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()

    # ✅ Check for errors or missing poster
    if response.status_code != 200 or 'poster_path' not in data or data['poster_path'] is None:
        print(f"⚠️ No poster found for movie_id={movie_id} — response: {data}")
        return "https://via.placeholder.com/500x750?text=No+Image"  # fallback placeholder image

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
