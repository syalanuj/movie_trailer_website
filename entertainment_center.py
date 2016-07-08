import fresh_tomatoes
import media

#initialize movie objects
toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", # NOQA
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
shivaji_the_boss = media.Movie("Shivaji the boss",
                                "The film revolves around a well-established software systems"
                                    " architect, Sivaji, who returns home to India after"
                                    " finishing work in the United States",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Sivaji_The_Boss.jpg/220px-Sivaji_The_Boss.jpg", # NOQA
                                "https://www.youtube.com/watch?v=Tc_IkLznzL8")
school_of_rock = media.Movie("School of Rock",
                            "The main plot follows struggling rock singer and guitarist,"
                                 " Dewey Finn (Black), who is kicked out of his band and"
                                 " subsequently disguises himself as a substitute teacher"
                                 " at a prestigious prep school",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", # NOQA
                            "https://www.youtube.com/watch?v=5afGGGsxvEA")
good_night_mommy = media.Movie("Good Night Mommy",
                                "After undergoing a cosmetic facial surgery, a woman (Susanne"
                                    " Wuest) comes back home to her modern, isolated lakeside"
                                    " house and to her ten-year-old twin sons, Elias and Lukas"
                                    " (Elias and Lukas Schwarz)",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Goodnight_Mommy.jpg/220px-Goodnight_Mommy.jpg", # NOQA
                                "https://www.youtube.com/watch?v=0kXpUaQpXMA")
inception = media.Movie("Inception",
                        "Dominick 'Dpm' Cobb (Leonardo DiCaprio) and Arthur (Joseph"
                            " Gordon-Levitt) are 'extractors', who perform corporate"
                            " espionage using an experimental military technology to"
                            " infiltrate the subconscious of their targets and extract"
                            " valuable information through a shared dream world",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg", # NOQA
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
#Array of Movie Objects
movies = [toy_story, avatar, shivaji_the_boss, school_of_rock, good_night_mommy, inception]
#Open Html in browser
fresh_tomatoes.open_movies_page(movies)
