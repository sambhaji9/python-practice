import json

# opening json file
f = open("./data.json")

# return JSON object as a dictionary
data = json.load(f)
for i in data["familyDetails"]:
    print(i)

# closing file
f.close()