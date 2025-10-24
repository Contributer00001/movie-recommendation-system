from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your TMDB API key
TMDB_API_KEY = "YOUR_TMDB_API_KEY"


def fetch_poster(movie_id):
    """
    Fetch poster URL from TMDB. Returns placeholder if not found.
    Handles connection errors gracefully.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=5)  # 5 sec timeout
        response.raise_for_status()  # Raise HTTPError for bad status
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            # Poster not found, return placeholder
            return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie_name):
    """
    Returns lists of recommended movie names and poster URLs.
    Replace this with your actual content-based recommendation logic.
    """
    recommended_names = []
    recommended_posters = []

    # Example TMDB IDs for demo purposes, replace with actual recommendations
    recommended_movie_ids = [550, 500, 600]

    for movie_id in recommended_movie_ids:
        recommended_names.append(movie_name)  # Replace with actual movie title
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selected_movie = request.form.get("movie_name")
        names, posters = recommend(selected_movie)
        return render_template("index.html", names=names, posters=posters)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
