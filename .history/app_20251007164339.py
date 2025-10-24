from flask import Flask, request, render_template
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load your saved data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    """Fetch poster from TMDB API"""
    api_key = 'YOUR_TMDB_API_KEY'  # 🔴 Replace with your key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movie_id)
        })
    return recommended_movies

@app.route('/')
def home():
    return render_template('index.html', movies=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie_name = request.form['movie']
    if movie_name not in movies['title'].values:
        return render_template('index.html', movies=movies['title'].values, error="Movie not found!")
    data = recommend(movie_name)
    return render_template('index.html', movies=movies['title'].values, recommendations=data)

if __name__ == '__main__':
    app.run(debug=True)
