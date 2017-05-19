import webbrowser


class Video():
    def __init__(self, title, storyline, image):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image

class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube, rating):
        Video.__init__(self, movie_title, movie_storyline, poster_image_url)
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, title, storyline, image, number_of_seasons):
        Video.__init__(self, title, storyline, image)
        self.seasons = number_of_seasons
