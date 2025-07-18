import pandas as pd
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

# 🔐 Spotify API credentials
SPOTIFY_CLIENT_ID = "4b7ac4ffb94549fa9b2da2c5eb0bc317"
SPOTIFY_CLIENT_SECRET = "21c0d92e203549bcb06ce525e81f82ff"

def fetch_telugu_songs():
    # Setup Spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))

    all_songs = []
    years = list(range(2000, 2026))  # From 2000 to 2025

    for year in years:
        print(f"\n📅 Fetching songs from {year}...")
        for offset in range(0, 1000, 50):  # Max 1000 per year
            try:
                query = f"telugu year:{year}"
                results = sp.search(q=query, type="track", limit=50, offset=offset)
                tracks = results['tracks']['items']

                if not tracks:
                    break  # No more results

                for item in tracks:
                    all_songs.append({
                        'title': item['name'],
                        'artist': item['artists'][0]['name'],
                        'album': item['album']['name'],
                        'release_date': item['album']['release_date'],
                        'url': item['external_urls']['spotify'],
                        'image_url': item['album']['images'][0]['url'] if item['album']['images'] else "",
                        'year': pd.to_datetime(item['album']['release_date'], errors='coerce').year,
                        'genre': "Romantic",  # default
                        'mood': "Happy"       # default
                    })

                time.sleep(0.3)  # Respect API limits

            except Exception as e:
                print(f"⚠️ Error at year {year}, offset {offset}: {e}")
                continue

    # Create DataFrame & clean up
    df = pd.DataFrame(all_songs).drop_duplicates(subset='title')
    df.to_csv("telugu_songs.csv", index=False)

    print(f"\n✅ DONE! Total unique songs collected: {len(df)}")
    return df

# Test run (optional)
if __name__ == "__main__":
    df = fetch_telugu_songs()
    print("\n🎵 Top 10 Latest Telugu Songs:\n")
    latest = df.sort_values(by="release_date", ascending=False).head(10)
    for i, row in latest.iterrows():
        print(f"{i+1}. {row['title']} - {row['artist']} ({row['release_date']})")
        print(f"   🔗 {row['url']}\n   🖼️ {row['image_url']}\n")
