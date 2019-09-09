import json

json_example = open("vlans.json").read()

json_python = json.loads(json_example)

hostname = json_python["general"]["hostname"]

print(hostname)
