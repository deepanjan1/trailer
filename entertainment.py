import media
import fresh_tomatoes

#create instances of the class Movie
vinny = media.Movie("My Cousin Vinny",
                    "https://upload.wikimedia.org/wikipedia/en/7/76/My-Cousin-Vinny-Poster.jpg",
                    "https://www.youtube.com/watch?v=0t7GMLXRnNM")

star_wars = media.Movie("Star Wars",
                    "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                    "https://www.youtube.com/watch?v=1g3_CFmnU7k")

home_alone = media.Movie("Home Alone",
                    "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
                    "https://www.youtube.com/watch?v=owU3lMxd6jI")

bourne_identity = media.Movie("Bourne Identity",
                    "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                    "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

piku = media.Movie("Piku", "https://upload.wikimedia.org/wikipedia/en/9/98/Piku.jpg",
                    "https://www.youtube.com/watch?v=oeiKUlUUNQ8")

the_descendants = media.Movie("The Descendants",
                                "https://upload.wikimedia.org/wikipedia/en/7/7d/Descendants_film_poster.jpg",
                                "https://www.youtube.com/watch?v=CWHNXJ1K4yA")

#load movies into a list structure
my_movies = [vinny, star_wars, home_alone, bourne_identity, piku, the_descendants]

#use fresh_tomatoes to open movies page with my_movies
fresh_tomatoes.open_movies_page(my_movies)
