#!/usr/bin/env python

"""entertainment_center.py: Contains database for the Fresh Tomatoes website.

    Runs fresh_tomatoes.open_movies_page() to create fresh_tomatoes.html"""

import media
import fresh_tomatoes

__author__ = "Udacity Full Stack Web Developer Nanodegree, Jordan Lamoreaux"
__credits__ = "Jordan Lamoreaux"

__version__ = "1.0"
__maintainer__ = "Jordan Lamoreaux"
__email__ = "jnacious88@gmail.com"
__status__ = "Development"


#The following are the Movies contained on Fresh Tomatoes

GOG_VOL2 = media.Movie("Guardians of the Galaxy Vol. 2",
                       "Star Lord and his companions come face to face with Star Lord's "
                       "father named Ego",
                       "http://cdn.movieweb.com/img.site/PHi3FGAu4Fkdlm_1_l.jpg",
                       "https://www.youtube.com/watch?v=duGqrYw4usE",
                       media.Movie.VALID_RATINGS[2])

WONDER_WOMAN = media.Movie("Wonder Woman",
                           "Before she was Wonder Woman she was Diana,"
                           "princess of the Amazons, trained warrior.",
                           "https://images-na.ssl-images-amazon.com/images/"
                           "M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5Yj"
                           "kzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                           "https://www.youtube.com/watch?v=INLzqh7rZ-U",
                           media.Movie.VALID_RATINGS[2])

THOR3 = media.Movie("Thor 3 Ragnarok",
                    "Imprisoned, the mighty Thor finds himself in a lethal "
                    "gladiatorial contest against the Hulk, his former ally.",
                    "https://images-na.ssl-images-amazon.com/images/M/"
                    "MV5BMjE1ODgwOTkzNF5BMl5BanBnXkFtZTgwMDcwMTg5MTI@."
                    "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=v7MGUNV8MxU",
                    media.Movie.VALID_RATINGS[2])

SPIDERMAN_HOMECOMING = media.Movie("Spider-Man: Homecoming",
                                   "Peter Parker attempts to balance his life in high school "
                                   "with his career as the web-slinging superhero Spider-Man",
                                   "https://images-na.ssl-images-amazon.com/images/M/"
                                   "MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@."
                                   "_V1_SY1000_CR0,0,658,1000_AL_.jpg",
                                   "https://www.youtube.com/watch?v=39udgGPyYMg",
                                   media.Movie.VALID_RATINGS[2])

JUSTICE_LEAGUE = media.Movie("Justice League",
                             "Fueled by his restored faith in humanity and inspired by Superman's selfless act, "
                             "Bruce Wayne enlists the help of his newfound ally, Diana Prince, "
                             "to face an even greater enemy.",
                             "https://images-na.ssl-images-amazon.com/images/M/"
                             "MV5BMjI2NjI2MDQ0NV5BMl5BanBnXkFtZTgwMTc1MjAwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw",
                             media.Movie.VALID_RATINGS[2])

SW_THE_LAST_JEDI = media.Movie("Star Wars: The Last Jedi",
                               "Rey continues her epic journey with Finn, Poe and "
                               "Luke Skywalker in the next chapter of the saga.",
                               "https://images-na.ssl-images-amazon.com/images/M/"
                               "MV5BOTE5NzYyNjM0Ml5BMl5BanBnXkFtZTgwNjk4MDIwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=zB4I68XVPzQ",
                               media.Movie.VALID_RATINGS[2])


# pylint recommends 'movies' being in formatted differently. I believe it
# views it as a GLOBAL_CONSTANT so it should be in ALL CAPS, but for
# consistancy with fresh_tomatoes, 'movies' was left lowercase
movies = [SW_THE_LAST_JEDI, WONDER_WOMAN, THOR3, SPIDERMAN_HOMECOMING,
          JUSTICE_LEAGUE, GOG_VOL2]


fresh_tomatoes.open_movies_page(movies)
