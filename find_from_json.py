# Some random data
# This is simplified version (only unique entries)
data = [
    { "name": "John", "age": 30, "phone": 111222333 },
    { "name": "Jane", "age": 24, "phone": 999888777 },
    { "name": "Emily", "age": 26, "phone": 555666777 },
    { "name": "Will", "age": 20, "phone": 777888999 },
    { "name": "Ashley", "age": 22, "phone": 222333444 }
]

# Getter function
get = lambda val, by: dict(*filter(lambda entry: entry[by] is val, data))

# Get person by name
ashley = get("Ashley", by="name")
print(f"Ashley's age is {ashley['age']}")

# Get person by phone
that_person = get(999888777, by="phone")
print(f"That person's name is: {that_person['name']}")

# Some more useful way
people = [
    get("Will", by="name"),
    get(30, by="age"),
    get("Emily", by="name")
]
for person in people: print(f"The age is: {person['age']}")

