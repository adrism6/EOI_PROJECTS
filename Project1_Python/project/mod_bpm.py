import sys

from spotify import Song

"""Information about headers in datafile
0: track name
1: artist name
2: genre
3: beats per minute
4: energy
5: danceability
6: length"""

if __name__ == "__main__":
    input_file = "../files/top50.csv"
    output_file = "../files/top50_mod.csv"
    relative_bpm = int(sys.argv[1])

    loaded_songs = Song.load_songs(input_file)

    for song in loaded_songs:
        song.change_speed(relative_bpm)

    Song.save_songs(loaded_songs, output_file)
