class Song:
    # Class attributes to track overall data
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
        self.__class__.add_song_to_count()

        # Add genre and artist to their respective collections
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)

        # Update genre and artist counts
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)

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

# Example Usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
hello = Song("Hello", "Adele", "Pop")
drunk_in_love = Song("Drunk in Love", "Beyonce", "Pop")



      


