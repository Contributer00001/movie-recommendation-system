from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

# Load movies and similarity matrix
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# TMDB API
API_KEY = "8aa7376043988f84e8c4e4f3f40241ac"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        data = requests.get(url).json()
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        return "https://via.placeholder.com/200x300"  # fallback
    except:
        return "https://via.placeholder.com/200x300"

def recommend(movie_name):
    recommended_movies = []
    recommended_posters = []
    try:
        idx = movies[movies['title'] == movie_name].index[0]
        distances = similarity[idx]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        for i in movie_list:
            movie_id = movies.iloc[i[0]].id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_posters.append(fetch_poster(movie_id))
    except IndexError:
        # If movie not found
        recommended_movies = ["Movie not found"]
        recommended_posters = ["https://via.placeholder.com/200x300"]
    return recommended_movies, recommended_posters

@app.route("/", methods=["GET", "POST"])
def home():
    names, posters = [], []
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        names, posters = recommend(movie_name)
    return render_template("index.html", names=names, posters=posters)

if __name__ == "__main__":
    app.run(debug=True)
