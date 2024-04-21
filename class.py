class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)


film_1 = Movie("Life of Brian", 1979, 8.1, True)
film_2 = Movie("The Holy Grail", 1975, 8.2, True)

# print(film_1.title, film_1.imdb_score)
#film_2.nice_print()
#Movie.nice_print(film_2)

#craete a list of films 
films = [film_1,film_2]
print("\nList of titles \n",films[0].title,"\n",films[1].title)

print("\nMovie Details\n")
films[0].nice_print()
# Classes are blueprints
# Objects are the actual things you built
# variables => attributes
# functions => methods