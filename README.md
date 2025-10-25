# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using **Python, Flask, Pandas, and Scikit-learn**.  
The app suggests movies similar to the one selected by the user, based on metadata such as genres, keywords, cast, and crew.

---

## 🚀 Features
- 🔍 Suggests top-5 movies similar to the user's choice  
- 🧠 Uses **cosine similarity** on feature vectors derived from movie metadata  
- 🗂️ Data preprocessing notebook to **generate `movies.pkl` and `similarity.pkl`** automatically  
- 🌐 Interactive **Flask web app** with HTML templates  
- ⚙️ Clean and reproducible project structure  

---

## 🧰 Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Backend** | Flask (Python) |
| **Libraries** | Pandas, NumPy, Scikit-learn, Pickle |
| **Dataset** | TMDB 5000 Movies and Credits (from Kaggle) |

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── app.py                      # Flask application
├── data_preprocessing.ipynb    # Notebook to generate pickle files
├── requirements.txt            # Dependencies
├── templates/
│   └── index.html              # Web UI template
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate       # for macOS/Linux
# venv\Scripts\activate         # for Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 🧠 Generate Model Files
Before running the app, generate the required pickle files (`movies.pkl` and `similarity.pkl`) by running the preprocessing notebook:

```bash
jupyter notebook data_preprocessing.ipynb
```

This will:
- Load TMDB datasets
- Extract important metadata
- Compute vector similarity
- Save the generated files (`movies.pkl`, `similarity.pkl`) in your project root directory

### ▶️ Run the Flask App
Once the `.pkl` files are ready, start your Flask server:

```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## 🧮 How It Works
- **Data Preprocessing** – Merges TMDB movie and credits datasets, cleans metadata, and combines tags.
- **Vectorization** – Uses CountVectorizer to convert text tags into feature vectors.
- **Similarity Calculation** – Computes cosine similarity between all movie vectors.
- **Recommendation** – When a movie is selected, displays the top 5 most similar titles.

---

## 🖼️ Example Output
If the user selects "Avatar", recommendations might include:
- Guardians of the Galaxy
- Star Trek
- Star Wars: The Force Awakens
- The Fifth Element
- John Carter

---

## 🌟 Future Improvements
- 🎞️ Integrate TMDB API to display movie posters and descriptions
- 🧩 Add collaborative filtering for personalized user recommendations
- 🚀 Deploy app on Render / Vercel / Streamlit Cloud
- 🎨 Enhance UI/UX with search autocomplete and animations

---

## 📜 License
This project is licensed under the MIT License — feel free to fork and modify it.

---

## 👨‍💻 Author
**Parth Giri**

- 📧 giriparth13@gmail.com
- 🌐 [linkedin.com/in/parth-giri](https://linkedin.com/in/parth-giri)
- 💻 [github.com/Contributer00001](https://github.com/Contributer00001)

---

⭐ If you found this project useful, don't forget to give it a star on GitHub!
