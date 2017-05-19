#!/usr/bin/env python

"""media.py: Module containing classes refered to by entertainment_center.py.

    Part of the Fresh Tomatoes project."""

import webbrowser

__author__ = "Udacity Full Stack Web Developer Nanodegree, Jordan Lamoreaux"
__credits__ = "Jordan Lamoreaux"

__version__ = "1.0"
__maintainer__ = "Jordan Lamoreaux"
__email__ = "jnacious88@gmail.com"
__status__ = "Development"


class Video():
    """This is the Parent Class with attributes that Movie and TvShow inheret.

    Attributes:
        title: A string containing the title of the movie.
        storyline: A string containing a summary of the movie's story line.
        image: A string containing the URL to the movie poster.
    """

    def __init__(self, title, storyline, image):
        """Inits Video with title, storyline and image"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image

class Movie(Video):
    """Movie stores details of movies to display on the Fresh Tomatoes Website.

    Attributes:
        Inherets title, storyline and image from Video.
        trailer_youtube: A string containing the URL for the movie trailer.
        rating: A predefined variable that is selected from the list 'VALID_RATINGS'.
            Indicates movie's MPAA Rating.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube, rating):
        """Inits Movie class with movie_title, movie_storyline, poster_image_url,
            trailer_youtube and rating."""
        Video.__init__(self, movie_title, movie_storyline, poster_image_url)
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    def show_trailer(self):
        """Plays movie trailer from YouTube"""
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """TvShow stores details of TV Shows to display on the Fresh Tomatoes Website.

    Attributes:
        Inherets title, storyline and image from Video.
        number_of_seasons: An integer count of the total number of seasons TV Show ran"""

    def __init__(self, title, storyline, image, number_of_seasons):
        Video.__init__(self, title, storyline, image)
        self.seasons = number_of_seasons
