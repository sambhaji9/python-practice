#python program to write JSON to a file called

import json

dict = {
    "name": "Sambhaji Mane",
    "age": 40,
    "gender": "male"
}

# serializing json
json_object = json.dumps(dict, indent=4)

# writing to sample json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)