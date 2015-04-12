import fresh_tomatoes
import media

whats_eating_gilbert_grape = media.Movie("What's Eating Gilbert Grape", 
                                         "Taking care of Arnie is mostly Gilbert's task which can be pretty demanding, at least while you are working at the local grocery store. Then one day Becky and her grandmother passes through Endora getting trouble with the car. Gilbert falls in love with Becky, but gets problems when he tries to find time for his own private life.",
                                         "Drama",
                                         "1994",
                                         "https://mariasmoviereviews.files.wordpress.com/2012/06/936full-whats-eating-gilbert-grape-poster.jpg",
                                         "https://www.youtube.com/watch?v=X6sLIP3908w")

the_judge = media.Movie("The Judge",
                        "Big city lawyer Hank Palmer returns to his childhood home where his father, the town's judge, is suspected of murder. Hank sets out to discover the truth and, along the way, reconnects with his estranged family.",
                        "Drama",
                        "2014",
                        "http://cf.broadsheet.ie/wp-content/uploads/2014/06/the-judge-poster.jpg",
                        "https://www.youtube.com/watch?v=ZBvK6ni97W8")

wall_e = media.Movie("Wall-E",
                     "In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                     "Animation, Adventure, Sci-Fi ",
                     "2008",
                     "http://cobalt.rocky.edu/~korinne.wilkerson/walle2.jpg",
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "Crime, Drama",
                            "1972",
                            "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=OfnUvYn6HoM")

american_history_x = media.Movie("American History X",
                                 "A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path that he did.",
                                 "Crime, Drama",
                                 "1998",
                                 "http://ia.media-imdb.com/images/M/MV5BMjMzNDUwNTIyMF5BMl5BanBnXkFtZTcwNjMwNDg3OA@@._V1_SX640_SY720_.jpg",
                                 "https://www.youtube.com/watch?v=JsPW6Fj3BUI")

in_bruges = media.Movie("In Bruges",
                        "Guilt-stricken after a job gone wrong, hitman Ray and his partner await orders from their ruthless boss in Bruges, Belgium, the last place in the world Ray wants to be.",
                        "Comedy, Crime, Drama",
                        "2008",
                        "http://ia.media-imdb.com/images/M/MV5BMTY4OTYxODg4MV5BMl5BanBnXkFtZTcwMDcyNzM2MQ@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=p-gG2qo_l_A")

birdman = media.Movie("Birdman",
                      "A washed-up actor, who once played an iconic superhero, battles his ego and attempts to recover his family, his career and himself in the days leading up to the opening of his Broadway play.",
                      "Comedy, Drama, Romance",
                      "2014",
                      "http://ia.media-imdb.com/images/M/MV5BODAzNDMxMzAxOV5BMl5BanBnXkFtZTgwMDMxMjA4MjE@._V1_SX640_SY720_.jpg",
                      "https://www.youtube.com/watch?v=uJfLoE6hanc")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                                      "Action, Adventure, Sci-Fi",
                                      "2014",
                                      "http://ia.media-imdb.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SX640_SY720_.jpg",
                                      "https://www.youtube.com/watch?v=b3isCLVghoI")

movies = [the_judge, birdman, guardians_of_the_galaxy, in_bruges, american_history_x, the_godfather, whats_eating_gilbert_grape, wall_e]


# create (and open in browser) html file containing all items from list "movies"
fresh_tomatoes.open_movies_page(movies)
