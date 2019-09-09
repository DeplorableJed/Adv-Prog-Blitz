import json

json_example = open("vlans.json").read()

json_python = json.loads(json_example)

json_python["general"]["hostname"] = str("RouterBB")

new_host = json.dumps(json_python)

open("vlans.json").write(new_host)




