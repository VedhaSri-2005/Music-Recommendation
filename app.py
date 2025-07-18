import streamlit as st
import pandas as pd
from recommend import load_data, build_model, recommend_song

st.set_page_config(page_title="🎶 Telugu Music Recommender", layout="wide")

# ---------------------- Load Data and Model ----------------------
df = load_data()
cos_sim = build_model(df)

st.title("🎧 Telugu Music Recommendation System")

# ---------------------- Filter by Singer ----------------------
unique_artists = sorted(df['artist'].dropna().unique(), key=lambda x: x.lower())
selected_artist = st.selectbox("🎤 Filter by Singer", ["All"] + unique_artists)

# ---------------------- Search by Song Name ----------------------
search_query = st.text_input("🔍 Search for a Song Name").lower()

# Filter by search and artist
filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[filtered_df['title'].str.lower().str.contains(search_query)]

if selected_artist != "All":
    filtered_df = filtered_df[filtered_df['artist'].str.lower() == selected_artist.lower()]

# ---------------------- Song Selection ----------------------
if not filtered_df.empty:
    song_titles = sorted(filtered_df['title'].dropna().unique(), key=lambda x: x.lower())
    selected_song = st.selectbox("🎵 Choose a Song", song_titles)

    if st.button("🔍 Recommend Similar Songs"):
        results = recommend_song(df, cos_sim, selected_song)

        if not results.empty:
            st.markdown("### 🎯 Recommended Songs")
            top_5 = results.head(5)
            cols = st.columns(5)

            for idx, (_, song) in enumerate(top_5.iterrows()):
                with cols[idx]:
                    st.image(song['image_url'], use_container_width=True)
                    st.markdown(f"**{song['title']}**")
                    st.markdown(f"*{song['artist']}*")
                    st.markdown(f"[🎧 Listen]({song['url']})", unsafe_allow_html=True)
        else:
            st.warning("No recommendations found.")
else:
    st.warning("❌ No matching songs found. Please refine your search.")
