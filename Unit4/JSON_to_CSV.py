import json
import csv

json_data = '''
[
    {"Name": "Maria", "Age": 19, "City": "Pune"},
    {"Name": "John", "Age": 22, "City": "Mumbai"},
    {"Name": "Asha", "Age": 20, "City": "Delhi"}
]
'''

data = json.loads(json_data)

with open("output.csv", "w", newline="") as csv_file:
    # Get headers from JSON keys
    headers = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print("JSON successfully converted to CSV!")