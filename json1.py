import json

# some json
x = '{"name": "Sambhaji Mane", "age": 40, "city": "Pune"}'

# parse x
y = json.loads(x)

# the result is python dictionary
print(y)
print(y['age'])