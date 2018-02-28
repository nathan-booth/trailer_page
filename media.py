import webbrowser

class Video():
    """Store information common to videos, including movies, video games, and tv shows."""
    def __init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year):
        self.video_title = video_title
        self.video_tagline = video_tagline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year

class Movie(Video):
    """Store movie-specific information."""
    def __init__ (self, video_title, video_tagline, poster_image, trailer_youtube, release_year, movie_id, movie_genre, director):
        Video.__init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year)
        self.movie_id = movie_id
        self.movie_genre = movie_genre
        self.director = director

class Game(Video):
    """Store game-specific information."""
    def __init__ (self, video_title, video_tagline, poster_image, trailer_youtube, release_year, game_id, game_genre, studio):
        Video.__init__(self, video_title, video_tagline, poster_image, trailer_youtube, release_year)
        self.game_id = game_id
        self.game_genre = game_genre
        self.studio = studio
