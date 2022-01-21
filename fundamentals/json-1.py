peoples = [
    {
        "name": "John",
        "city": "Ottawa",
        "age": 30
    },
    {
        "name": "Smith",
        "city": "Toronto",
        "age": 31
    }
]

for people in peoples:
    for key in people:
        print(key, ":", people[key])


