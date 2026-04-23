
people = [
    {"name": "Amit", "age": 17},
    {"name": "Pradeep", "age": 22},
    {"name": "Jagdish", "age": 15},
    {"name": "Sanjay", "age": 19}
]

# Step 1: Filter people with age >= 18
adults = filter(lambda person: person["age"] >= 18, people)

# Step 2: Get names of filtered people
names = list(map(lambda person: person["na" \
"me"], adults))

print(names)
