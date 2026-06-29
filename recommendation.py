import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Combine genre and overview
movies["tags"] = movies["genre"] + " " + movies["overview"]

# Convert text into vectors
cv = CountVectorizer(stop_words="english")
vectors = cv.fit_transform(movies["tags"])

# Calculate similarity
similarity = cosine_similarity(vectors)

def recommend(movie_name):

    movie_name = movie_name.lower()

    movie_titles = movies["title"].str.lower()

    if movie_name not in movie_titles.values:
        return []

    index = movie_titles[movie_titles == movie_name].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    recommendations=[]

    for i in movie_list:

        recommendations.append({

            "title":movies.iloc[i[0]].title,

            "rating":movies.iloc[i[0]].rating,
            
            "overview":movies.iloc[i[0]].overview

        })

    return recommendations