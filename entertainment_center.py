import media
import fresh_tomatoes

gog_vol2 = media.Movie("Guardians of the Galaxy Vol. 2",
                       "Star Lord and his companions come face to face with Star Lord's father named Ego",
                       "http://cdn.movieweb.com/img.site/PHi3FGAu4Fkdlm_1_l.jpg",
                       "https://www.youtube.com/watch?v=duGqrYw4usE",
                       media.Movie.VALID_RATINGS[2])

#print(gog_vol2.storyline)

wonder_woman = media.Movie("Wonder Woman",
                           "Before she was Wonder Woman she was Diana, princess of the Amazons, trained warrior.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                           "https://www.youtube.com/watch?v=INLzqh7rZ-U",
                           media.Movie.VALID_RATINGS[2])
#print(wonder_woman.storyline)
#wonder_woman.show_trailer()

thor3 = media.Movie("Thor 3 Ragnarok",
                    "Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1ODgwOTkzNF5BMl5BanBnXkFtZTgwMDcwMTg5MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=v7MGUNV8MxU",
                    media.Movie.VALID_RATINGS[2])
#thor3.show_trailer()

spiderman_homecoming = media.Movie("Spider-Man: Homecoming",
                                   "Peter Parker attempts to balance his life in high school with his career as the web-slinging superhero Spider-Man",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
                                   "https://www.youtube.com/watch?v=39udgGPyYMg",
                                   media.Movie.VALID_RATINGS[2])

justice_league = media.Movie("Justice League",
                             "Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI2NjI2MDQ0NV5BMl5BanBnXkFtZTgwMTc1MjAwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw",
                             media.Movie.VALID_RATINGS[2])

sw_the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                               "Rey continues her epic journey with Finn, Poe and Luke Skywalker in the next chapter of the saga.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BOTE5NzYyNjM0Ml5BMl5BanBnXkFtZTgwNjk4MDIwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=zB4I68XVPzQ",
                               media.Movie.VALID_RATINGS[2])

movies = [sw_the_last_jedi, wonder_woman, thor3, spiderman_homecoming, justice_league, gog_vol2]

#fresh_tomatoes.open_movies_page(movies)

print(gog_vol2.rating)
