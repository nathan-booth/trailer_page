import webbrowser
import os
import re

main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .trailer_image:hover {
            /*change: pointer change on image, not on whole tile*/
            background-color: #EEE;
            cursor: pointer;
        }
        .game-tile {
            /*change: added 2nd type of tiles*/
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .section_title {
            /*change: added style for section titles*/
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened;
        // Change: .movie-tile to .trailer_image, so trailer video can click-open upon clicking trailer_image, not whole tile
        $(document).on('click', '.trailer_image', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Change: added a second type of tile for games
        $(document).ready(function () {
          $('.game-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

main_page_title = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="Crosshatch button"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content: Title Bar -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Video Trailers</a>
          </div>
        </div>
      </div>
    </div>
'''

main_page_movies = '''
    <div class="section_title">
        <h1><u>Movie Trailers</u></h1>
    </div>
    <!-- First section: movies -->
    <div class="container">
      {movie_tiles}
    </div>
'''

main_page_games = '''
    <div class="section_title">
        <h1><u>Video Game Trailers</u></h1>
    </div>
    <!-- 2nd section: games -->
    <div class="container">
      {game_tiles}
    </div>
  </body>
</html>
'''

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img class="trailer_image" src="{poster_image_url}" alt="{movie_title} Poster" width="260" height="404" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h3>{movie_title}</h3>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" href="#{movie_id}">More Information</a>
                </h4>
            </div>
            <div id="{movie_id}" class="panel-collapse collapse">
                <div class="panel-body">{movie_tagline}</div>
                <div class="panel-body">Genre: {genre}</div>
                <div class="panel-body">Director: {director}</div>
                <div class="panel-body">Release Year: {release_year}</div>
            </div>
        </div>
    </div>
</div>
'''

game_tile_content = '''
<div class="col-md-6 col-lg-4 game-tile text-center">
    <img class="trailer_image" src="{poster_image_url}" alt="{game_title} Poster" width="260" height="404" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h3>{game_title}</h3>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" href="#{game_id}">More Information</a>
                </h4>
            </div>
            <div id="{game_id}" class="panel-collapse collapse">
                <div class="panel-body">{game_tagline}</div>
                <div class="panel-body">Genre: {genre}</div>
                <div class="panel-body">Publisher: {publisher}</div>
                <div class="panel-body">Release Year: {release_year}</div>
            </div>
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
        content += movie_tile_content.format(
            movie_title=movie.video_title,
            movie_id=movie.movie_id,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_tagline=movie.video_tagline,
            genre=movie.genre,
            director=movie.director,
            release_year=movie.release_year)
    return content

def create_game_tiles_content(games):
    content = ''
    for game in games:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', game.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', game.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
        content += game_tile_content.format(
            game_title=game.video_title,
            game_id=game.game_id,
            poster_image_url=game.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            game_tagline=game.video_tagline,
            genre=game.genre,
            publisher=game.publisher,
            release_year=game.release_year)
    return content

def open_page(movies, games):
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_content_movies = main_page_movies.format(movie_tiles= create_movie_tiles_content(movies))
    rendered_content_games = main_page_games.format(game_tiles=create_game_tiles_content(games))

    output_file.write(main_page_head + main_page_title + rendered_content_movies + rendered_content_games)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
