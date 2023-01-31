import json


with open("metrics.json", "w") as f:
    json.dump({"acc":0.1},f)

print("1,2,4")
