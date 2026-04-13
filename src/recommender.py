import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {}
            for key, value in row.items():
                # Try to convert to int first, then float, otherwise keep as string
                try:
                    if '.' in value:
                        song[key] = float(value)
                    else:
                        song[key] = int(value)
                except ValueError:
                    song[key] = value
            songs.append(song)
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Calculate scores for all songs
    scored_songs = [(song, score, reasoning) for song in songs 
                   for score, reasoning in [score_song(user_prefs, song)]]
    
    # Sort by score in descending order and take top k
    top_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
    
    return top_songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Scores a song based on user preferences.
    Required by tests/test_recommender.py
    """
    score = 0.0
    reasoning_parts = []
    
    # Genre match: +2.0 points
    if song.get('genre', '').lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasoning_parts.append(f"+2.0 for genre match ({song['genre']})")
    else:
        reasoning_parts.append(f"+0.0 genre mismatch (user: {user_prefs.get('genre')}, song: {song.get('genre')})")
    
    # Mood match: +1.0 point
    if song.get('mood', '').lower() == user_prefs.get('mood', '').lower():
        score += 1.0
        reasoning_parts.append(f"+1.0 for mood match ({song['mood']})")
    else:
        reasoning_parts.append(f"+0.0 mood mismatch (user: {user_prefs.get('mood')}, song: {song.get('mood')})")
    
    # Energy match: +(1.0 - abs(target_energy - song_energy))
    target_energy = user_prefs.get('energy', 0.5)
    song_energy = song.get('energy', 0.5)
    energy_score = 1.0 - abs(target_energy - song_energy)
    score += energy_score
    reasoning_parts.append(f"+{energy_score:.2f} for energy match (target: {target_energy}, song: {song_energy})")
    
    # Acousticness match
    song_acousticness = song.get('acousticness', 0.5)
    if user_prefs.get('likes_acoustic', False):
        score += song_acousticness
        reasoning_parts.append(f"+{song_acousticness:.2f} for acousticness (user likes acoustic)")
    else:
        acoustic_score = 1.0 - song_acousticness
        score += acoustic_score
        reasoning_parts.append(f"+{acoustic_score:.2f} for low acousticness (user dislikes acoustic)")
    
    reasoning = "\n".join(reasoning_parts)
    return score, reasoning
