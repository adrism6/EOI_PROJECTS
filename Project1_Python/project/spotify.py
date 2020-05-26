class Song:
    def __init__(self, track, artist, genre, bpm, energy, danceability, length):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = int(bpm)
        self.energy = int(energy)
        self.danceability = int(danceability)
        self.length = int(length)

    def __str__(self):
        return f"{self.track},{self.artist},{self.genre},{self.bpm},{self.energy},{self.danceability},{self.length}\n"

    def change_speed(self, relative_bpm):
        self.bpm += relative_bpm
        self.energy += 2 * relative_bpm
        self.danceability += 3 * relative_bpm
        self.length -= relative_bpm

    @staticmethod
    def load_songs(path):
        with open(path, "r", encoding="utf8") as fin:
            songs = []
            for line in fin.readlines():
                args = line.split(",")
                song = Song(*args)
                songs.append(song)
        return songs

    @staticmethod
    def save_songs(songs, path):
        with open(path, "w", encoding="utf8") as fout:
            for song in songs:
                fout.write(f"{song}")
