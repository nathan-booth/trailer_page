import webbrowser

class Video():
    """Store information common to videos, including movies, video games, and tv shows."""
    def __init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year, genre):
        self.video_title = video_title
        self.video_tagline = video_tagline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
        self.genre = genre

class Movie(Video):
    """Store movie-specific information."""
    def __init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year, genre, movie_id, director):
        Video.__init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year, genre)
        self.movie_id = movie_id
        self.director = director

class Game(Video):
    """Store game-specific information."""
    def __init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year, genre, game_id, publisher):
        Video.__init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year, genre)
        self.game_id = game_id
        self.publisher = publisher
