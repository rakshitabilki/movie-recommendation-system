# 🎬 Netflix Movie Recommendation System

A simple Netflix-inspired Movie Recommendation System built using **Flask** and **Machine Learning**. This web application recommends similar movies based on the selected movie using **CountVectorizer** and **Cosine Similarity**.

##  Features

-  Search for a movie
-  Get Top 5 similar movie recommendations
-  Display IMDb ratings
-  View a short description of each recommended movie
-  Netflix-inspired user interface
-  Responsive and easy-to-use web application


##  Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── recommendation.py
├── movies.csv
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### 2. Navigate to the project folder

```bash
cd Movie-Recommendation-System
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

##  How It Works

1. The movie dataset is loaded using **Pandas**.
2. Movie genres and overviews are combined into a single text feature.
3. **CountVectorizer** converts text into numerical vectors.
4. **Cosine Similarity** calculates the similarity between movies.
5. When a user searches for a movie, the system recommends the five most similar movies along with their IMDb ratings and descriptions.

---

##  Application Preview

### Home Page
- Search movies
- Netflix-inspired interface

### Recommendation Page
- Top 5 similar movies
- IMDb ratings
- Movie descriptions

---


## 👩‍💻 Author

**Rakshita Bilki**

GitHub: https://github.com/rakshitabilki

---

## 📄 License

This project is developed for educational and learning purposes.
