import csv  
import json


ls = []

with open('houses.csv', 'r') as file:
    r = csv.DictReader(file, delimiter=';')
    for row in r:
        if int(row['inside']) != int(row['outside']):
            x = abs(int(row['inside']) - int(row['outside']))
            ls.append({"address": row['address'], "difference": x})

with open('unusual.json', 'w') as f:
    json.dump(ls, f)
    
