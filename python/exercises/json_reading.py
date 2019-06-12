import json

with open("/home/uriel/smarterway/test.json") as f:
    text_to_read = json.load(f)
    rows = []
    
    for i in text_to_read:
        rows += i
    
print(rows)