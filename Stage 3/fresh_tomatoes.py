import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Passion+One:700" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 7vw;
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
            padding: 20px;
            width: 100%;
        }
        .movie-tile:hover {
            background-color: #ABABAB;
            cursor: pointer;
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
        #navback {
            background-color: #F0141E;
            height: 7vw;
            border-bottom: 5px #000 solid;
            border-top: 5px #000 solid;
        }
        #navtitle1 {
            color: #FFF;
            text-decoration: none;
            font-size: 4vw;
            font-family:'Passion One', cursive;
            content-align: center;
            padding: 3px;
        }
        #navtitle {
            color: #FFF;
            text-decoration: none;
            font-size: 2.5vw;
            font-family:'Passion One', cursive;
            content-align: center;
            padding: 10px;
        }
        #navtitle:hover {
            border: #FFF 2px solid;
        }
        #flexcont {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            width: 100%;
        }
        .textcont {
            color: #818181;
            font-family: sans-serif;
            padding: 5px;
        }
        .bigcontainer {
            display: flex;
            flex-direction: column;
            justification-content: center;
            align-items: center;
            width: 28em;
            margin: 0px auto;
            padding-top: 7vw;
        }
        .moviehead {
            background-color: #F0141E;
            color: #FFF;
            font-size: 3em;
            font-family: 'Passion One', cursive;
            padding: 5px;
            text-align: center;
        }
        .moviehead:hover {
            outline: 2px solid #F0141E;
            background-color: FFF;
            color: #F0141E;
            cursor: pointer;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate description when clicking on movie title
        $(document).on('click', '.moviehead', function(action) {
            $('.textcont').toggle(400);
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            $('.textcont').hide();
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container" id="toptop">
      <div class="navbar-fixed-top" role="navigation" id="navback">
        <div class="container">
          <div>
            <a id="navtitle1" href="#toptop">MARVEL FILMS</a>
            <a id="navtitle" href="#p1">PHASE 1</a>
            <a id="navtitle" href="#p2">PHASE 2</a>
            <a id="navtitle" href="#p3">PHASE 3</a>
            <a id="navtitle" href="#p4">FUTURE</a>
          </div>
        </div>
      </div>
    </div>
    <div id="flexcont">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="bigcontainer" id="{mcu_phaseid}">
    <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
    </div>
    <div>
        <h2 class="moviehead">{movie_title}</h2>
        <p class="textcont">{movie_storyline}</p>
        <p class="textcont">{release_date}</p>
        <p class="textcont">{mcu_phase}</p>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            release_date=movie.release,
            mcu_phase=movie.phase,
            mcu_phaseid=movie.phaseid
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
