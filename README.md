# 🎧 Telugu Music Recommendation System

A content-based music recommendation web app built with **Streamlit**, recommending Telugu songs using Spotify metadata. Users can search songs, filter by singer, and get similar songs based on lyrics or metadata using TF-IDF and cosine similarity.

---

## 🚀 Features

- 🔍 **Search Songs**: Search by full or partial title (case-insensitive)
- 🎤 **Filter by Singer**: Narrow down songs based on your favorite artist
- 🤖 **Content-Based Recommendations**: Using TF-IDF and cosine similarity
- 🎵 **Spotify Integration**: View cover art and listen to songs directly via links
- ⚡ **Responsive UI**: Clean, modern design with horizontal layout of recommended songs

---

## 📁 Project Structure

telugu-music-recommender\
├── app.py              # Streamlit frontend\
├── recommend.py        # TF-IDF based recommendation engine\
├── spotify_fetch.py    # Script to fetch Telugu songs from Spotify API\
├── telugu_songs.csv    # Dataset of Telugu songs\
├── requirements.txt    # Python dependencies\
└── README.md           # Project documentation\


## 🧠 How It Works
-Songs are fetched using the Spotify API and stored in a CSV file.

-A TF-IDF vectorizer is used to convert song titles and artist names into vectors.

-Cosine similarity is calculated to find the most similar songs.

-You can select a song and view similar recommendations instantly.

---
## 🧑‍💻 Developed By
**Muthineni Vedha Sri**

