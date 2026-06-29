from flask import Flask, render_template, request
from recommendation import recommend

app = Flask(__name__)
import pandas as pd

movie_data = pd.read_csv("movies.csv")

movies = movie_data["title"].tolist()

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend(movie)

    return render_template(
        "index.html",
        movies=movies,
        recommendations=recommendations
    )

if __name__ == "__main__":
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)