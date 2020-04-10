movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]
#magic of enumeration and tuple unpacking :)
for counter,(mov_name,dir_name,year) in enumerate(movies,start=1):
    print(f"{counter}.{mov_name} is directed by {dir_name} in {year}")



#without unpacking 
for mov in movies:
    print(f"{mov[0]} is made by {mov[1]} in {mov[2]}")

# List unpacking
for mov_name,dir_name,date in movies:
    print(f"{mov_name} is directed by {dir_name} in {date}")

#Enumerate
names = ["Harry", "Rachel", "Brian"]
for counter,name in enumerate(names,start=1):
    print(f"{counter}.{name}")

#magic of zip function
fav_food = ["ice cream","chocolate","tuffy"]
kids = ["bobby","james","alexis"]
for kid,food in zip(kids,fav_food):
    print(f"{kid} loves {food}")


