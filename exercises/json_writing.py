import json

random_list = ["X", "Y", "Z"]

with open("/home/uriel/smarterway/test.json", "w") as j:
    json.dump(random_list, j)