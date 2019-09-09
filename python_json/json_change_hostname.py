import json

json_example = open("vlans.json").read()

json_python = json.loads(json_example)

json_names = json_python["interfaces"]

for interfaces in json_names:
    name = interfaces["name"]
    print (name)
