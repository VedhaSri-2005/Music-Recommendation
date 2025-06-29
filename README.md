# Music-Recommendation
A **Telugu Music Recommendation System** developed with **Python**, **Spotify API**, and **Streamlit**.
This project dynamically loads freshly released Telugu songs from Spotify, processes their genre and mood, and gives **content-based song recommendations** with embeddable Spotify play links—all within a user-friendly web application.
---

## 🚀 Features

* **Automatic fetching** of new Telugu songs from Spotify
* **Content-based filtering** using genre and mood
* **Streamlit-powered web interface**
* **Clickable Spotify links** to play each recommended song
* Data stored and updated in a lightweight CSV file

---

## 🛠️ Tech Stack

* **Python 3**
* **Spotipy (Spotify Web API)**
* **Scikit-learn** (TF-IDF & Cosine Similarity)
* **Streamlit** for UI
* **Pandas** for data processing

---

## 🔍 How It Works

1. **Fetch Songs:** Use Spotify API to search for latest Telugu tracks
2. **Store Data:** Append song metadata to a CSV file (`telugu_songs.csv`)
3. **Vectorize Features**: Use TF-IDF on genre+mood to build feature vectors
4.**Recommend Songs**: Compute cosine similarity to find similar songs
5.**Display UI**: Streamlit app lets users input a song and get recommendations with Spotify links


🌐 **Live Demo**




🔹 **Folder Structure**

Music-Recommendation/
├── app.py                # Streamlit UI
├── recommend.py          # Recommendation logic
├── spotify_fetch.py      # Spotify API integration
├── telugu_songs.csv      # Song data storage
├── requirements.txt      # Python dependencies
└── README.md             # Project description

🚀 **Future Enhancements**
✨ Use Spotify audio features for better mood detection
📃 Add filtering by artist, genre, or mood in UI
🔖 Deploy with database support (SQLite/Firebase)
🔺 Embed Spotify player previews

👤 Author
**Muthineni Vedha Sri**
