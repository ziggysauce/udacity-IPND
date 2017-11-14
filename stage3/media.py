import webbrowser

class Movie():
    """Stores movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date, mcu_phase, mcu_phaseid):
        """
        Initialize movie instance
        Arguments:
        movie_title: Title of movie_title
        movie_storyline: Quick description of movie
        poster_image: Movie poster image
        trailer_youtube: Youtube link for movie trailer
        release_date: The movie release date in the US
        mcu_phase: The MCU Phase that the movie belongs to
        mcu_phaseid: For navbar purposes to direct user to MCU phase
        ...
        Returns: None
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release = release_date
        self.phase = mcu_phase
        self.phaseid = mcu_phaseid

    def show_trailer(self):
        """
        Opens an HTML webbrowser in the python file
        Argument: url for youtube trailer of movie
        Returns: Opens link to trailer
        """
        webbrowser.open(self.trailer_youtube_url)
