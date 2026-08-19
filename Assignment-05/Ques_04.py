# Q4. Create a Python dictionary of 3 cities and their populations. Save it to
# "cities.json".

# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population - update this info in the JSON
#    file.

import json

dict_cities = {"New York": 8419600, "Los Angeles": 3980400, "Chicago": 2716000}

with open("cities.json", "w") as f:
    f.write(json.dumps(dict_cities, indent=2))

with open("cities.json", "r") as f:
    dict_citie = json.load(f)

for city, population in dict_cities.items():
    print(city, population)

city = input("Enter a new city: ")
population = int(input("Enter cities population :"))

dict_cities[city] = population

with open("cities.json", "w") as f:
    json.dump(dict_cities, f)
