import csv  
import json


ls = []

with open('houses.csv', 'r') as file:
    r = csv.DictReader(file, delimiter=';')
    for row in r:
        f = False
        for i in row:
            if int(i['inside']) != int(i['outside']):
                x = abs(int(i['inside']) - int(i['outside']))
                f = True
                break
        if f is True:
            ls.append({"adress": row['adress'], "difference": x})

with open('unusual.json', 'w') as f:
    json.dump(ls, f)
    
