import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    df = pd.read_csv("telugu_songs.csv")  # Unified filename
    df = df.fillna("")

    def infer_genre(title):
        title = title.lower()
        if "love" in title or "prema" in title:
            return "Romantic"
        elif "devudu" in title or "lord" in title or "deva" in title:
            return "Devotional"
        elif "dance" in title or "dj" in title:
            return "Dance"
        elif "folk" in title or "janapada" in title:
            return "Folk"
        else:
            return "Pop"

    def infer_mood(title):
        title = title.lower()
        if "sad" in title or "melancholy" in title:
            return "Sad"
        elif "happy" in title or "fun" in title:
            return "Happy"
        elif "calm" in title or "relax" in title:
            return "Calm"
        elif "love" in title:
            return "Romantic"
        else:
            return "Energetic"

    df['genre'] = df['title'].apply(infer_genre)
    df['mood'] = df['title'].apply(infer_mood)

    df['features'] = (
        df['title'].astype(str) + " " +
        df['artist'].astype(str) + " " +
        df['genre'].astype(str) + " " +
        df['mood'].astype(str)
    )

    return df

def build_model(df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['features'])
    return cosine_similarity(tfidf_matrix)

def recommend_song(df, cos_sim, title):
    title_lower = title.lower()
    matched = df[df['title'].str.lower() == title_lower]
    if matched.empty:
        return pd.DataFrame()  # Empty DataFrame if not found
    idx = matched.index[0]
    scores = list(enumerate(cos_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5
    return df.iloc[[i[0] for i in scores]]

def get_songs_by_album(df, album_name):
    return df[df['album'].str.lower() == album_name.lower()]
