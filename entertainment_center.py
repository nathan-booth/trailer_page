import media
import fresh_tomatoes

fury_road = media.Movie("Mad Max: Fury Road",
                        "An average day in Australia",
                        "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                        "https://www.youtube.com/watch?v=hEJnMQG9ev8",
                        "2015",
                        "m1",
                        "Action",
                        "George Miller")

shawkshenk = media.Movie("The Shawkshenk Redemption",
                         "Fear can hold you prisoner. Hope can set you free.",
                         "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                         "https://www.youtube.com/watch?v=6hB3S9bIaco",
                         "1994",
                         "m2",
                         "Drama",
                         "Frank Darabont")

spaceballs = media.Movie("Spaceballs",
                         "Ludicrous speed!",
                         "https://upload.wikimedia.org/wikipedia/en/4/45/Spaceballs.jpg",
                         "https://www.youtube.com/watch?v=kGIM_yNzeUo",
                         "1987",
                         "m3",
                         "Comedy",
                         "Mel Brooks")

hots = media.Game("Heroes of the Storm",
                  "It's about time.", "https://upload.wikimedia.org/wikipedia/en/4/44/Heroes_of_the_Storm_logo_2016.png",
                  "https://www.youtube.com/watch?v=0ecv0bT9DEo", "2015",
                  "g1",
                  "Multiplayer online battle arena",
                  "Blizzard Entertainment")

sc2 = media.Game("StarCraft II",
                 "My life for Aiur.",
                 "https://upload.wikimedia.org/wikipedia/en/7/77/StarCraft_II_-_Legacy_of_the_Void_cover.jpg",
                 "https://nathanielbooth.squarespace.com/config/",
                 "2015",
                 "g2",
                 "Real-time strategy",
                 "Blizzard Entertainment")

lol = media.Game("League of Legends",
                 "Last hit!",
                 "https://upload.wikimedia.org/wikipedia/en/7/77/League_of_Legends_logo.png",
                 "https://www.youtube.com/watch?v=IzMnCv_lPxI",
                 "2009",
                 "g3",
                 "Multiplayer online battle arena",
                 "Riot Games")

movies = [fury_road, shawkshenk, spaceballs]
games = [hots, sc2, lol]
fresh_tomatoes.open_page(movies, games)
