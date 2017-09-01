import webbrowser

from MovieWebsite.Movies import Movie
from MovieWebsite.fresh_tomatoes import open_movies_page
def main():
    logan1 = Movie("Logan"
                   , "A hugh jackman movie",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                   "https://www.youtube.com/watch?v=Div0iP65aZo")

    logan2 = Movie("Logan", "A hugh jackman movie",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                   "https://www.youtube.com/watch?v=Div0iP65aZo")

    logan3 = Movie("Logan", "A hugh jackman movie",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                   "https://www.youtube.com/watch?v=Div0iP65aZo")

    logan4 = Movie("Logan", "A hugh jackman movie",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                   "https://www.youtube.com/watch?v=Div0iP65aZo")

    logan5 = Movie("Logan", "A hugh jackman movie",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                   "https://www.youtube.com/watch?v=Div0iP65aZo")


    movies=[logan1,logan2,logan3,logan4,logan5]
    open_movies_page(movies)
main()
