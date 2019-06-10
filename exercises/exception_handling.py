import json

try:
    with open("/home/uriel/smarterway/unknown.json") as j:
        text_to_read = json.load(j)
        print(text_to_read)
except FileNotFoundError:
    print("File not found!")