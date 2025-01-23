class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count
        Song.add_song_to_count()
        
        # Add genre and artist to their respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

# Create more songs to see the counts
song1 = Song("Song 1", "Artist 1", "Rock")
song2 = Song("Song 2", "Artist 1", "Rap")
song3 = Song("Song 3", "Artist 2", "Country")
song4 = Song("Song 4", "Artist 3", "Rock")

# Check class attributes
print(Song.count)  # Total number of songs created
print(Song.genres)  # Unique genres
print(Song.artists)  # Unique artists
print(Song.genre_count)  # Count of songs per genre
print(Song.artist_count)  # Count of songs per artist
