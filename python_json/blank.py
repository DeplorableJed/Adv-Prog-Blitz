import json
rtr_json= open("router.json").read()
rtr_dict=json.loads(rtr_json)
print("Hostname:"+rtr_dict["general"]["hostname"])
for intf in rtr_dict["interfaces"]:
	print (intf["name"])

