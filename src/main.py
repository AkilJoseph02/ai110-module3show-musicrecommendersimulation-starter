"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded Songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": True}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    #Stress Test Profiles
    #High Energy + Sad Mood (Adversarial: Contradictory energy and mood)
    stress_test_profile1 = {"genre": "rock", "mood": "sad", "energy": 1.0, "likes_acoustic": False}
    stress_recommendations1 = recommend_songs(stress_test_profile1, songs, k=5)
    #Low Energy + Intense Mood (Adversarial: Contradictory energy and mood)
    stress_test_profile2 = {"genre": "pop", "mood": "intense", "energy": 0.2, "likes_acoustic": True}
    stress_recommendations2 = recommend_songs(stress_test_profile2, songs, k=5)
    #Acoustic Preference + High Energy (Edge Case: Acoustic songs are often mellow)
    stress_test_profile3 = {"genre": "folk", "mood": "happy", "energy": 0.9, "likes_acoustic": True}
    stress_recommendations3 = recommend_songs(stress_test_profile3, songs, k=5)
    #Non-Acoustic Preference + Low Energy (Edge Case: Non-acoustic songs are often energetic)
    stress_test_profile4 = {"genre": "electronic", "mood": "chill", "energy": 0.1, "likes_acoustic": False}
    stress_recommendations4 = recommend_songs(stress_test_profile4, songs, k=5)
    #Extreme Energy Mismatch (Adversarial: Very high energy with calm mood)
    stress_test_profile5 = {"genre": "jazz", "mood": "calm", "energy": 1.0, "likes_acoustic": False}
    stress_recommendations5 = recommend_songs(stress_test_profile5, songs, k=5)
    #No Genre/Mood Matches (Edge Case: Rare or nonexistent preferences)
    stress_test_profile6 = {"genre": "classical", "mood": "mysterious", "energy": 0.5, "likes_acoustic": True}
    stress_recommendations6 = recommend_songs(stress_test_profile6, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()
    
    print("\nStress Test Recommendations:\n")
    print("1. High Energy + Sad Mood:")
    for rec in stress_recommendations1:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

    print("2. Low Energy + Intense Mood:")
    for rec in stress_recommendations2:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

    print("3. Acoustic Preference + High Energy:")
    for rec in stress_recommendations3:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

    print("4. Non-Acoustic Preference + Low Energy:")
    for rec in stress_recommendations4:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

    print("5. Extreme Energy Mismatch:")
    for rec in stress_recommendations5:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

    print("6. No Genre/Mood Matches:")
    for rec in stress_recommendations6:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: \n{explanation}")
        print()

if __name__ == "__main__":
    main()
