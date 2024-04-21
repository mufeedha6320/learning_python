# Dictionary comprehensions
movies = ["The goat life","Jana gana mana",
"Ozler","Premalu","The Meaning of Life","Live Mostly"]
year =[2023,2022,2023,2024,1983,2024]
names = ['Raj','Prathvi','Mammootty','Naslen','Terry','TerryG']
print(list(zip(movies, year)))

# create a dict('movies': year) for each movies, year in zip(movies, year)
'''
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)
'''
new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 2024 and movie.startswith('The')}
print('My new dictionary\n',new_dict)
NMY_list = [(name+"'s movie is '"+movie +"' in "+str(yr)) for name,movie,yr in zip(names,movies,year)]
print(NMY_list)
