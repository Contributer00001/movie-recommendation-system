from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load your saved data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', movies=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie']
    if movie_name not in movies['title'].values:
        return render_template('index.html', movies=movies['title'].values, error="Movie not found!")

    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended = [movies.iloc[i[0]].title for i in distances[1:6]]
    return render_template('index.html', movies=movies['title'].values, recommendations=recommended)

if __name__ == '__main__':
    app.run(debug=True)
