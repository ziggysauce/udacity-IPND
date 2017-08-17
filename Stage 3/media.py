import webbrowser

class Movie():
    """Stores movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date, mcu_phase, mcu_phaseid):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release = release_date
        self.phase = mcu_phase
        self.phaseid = mcu_phaseid

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
