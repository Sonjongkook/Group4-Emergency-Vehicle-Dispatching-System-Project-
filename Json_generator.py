import json
import random

data = {}
vehicles = []
add = 0
for i in range(30):
    add += random.randint(0, 1)
    vehicles.append(
        {'id': i+1, 'type': random.randint(1, 3), 'zipcode': 64151+add})
data['vehicles'] = vehicles

requests = []
for i in range(20):
    requests.append({'id': i+1, 'type': random.randint(1, 3), 'zipcode': random.randint(
        vehicles[0]['zipcode'], vehicles[-1]['zipcode']), "vehicle_id": None, 'distance': 0})
data['requests'] = requests


vehicle_zip = [i for i in range(vehicles[0]['zipcode'],vehicles[-1]['zipcode']+1)]
distance = []
i = 0
while i <= 10:
    zipcode1 = random.choice(vehicle_zip)
    zipcode2 = random.choice(vehicle_zip)
    if zipcode1 == zipcode2:
        continue

    i += 1
    distance.append({'zipcode1': zipcode1, 'zipcode2': zipcode2,
                     'distance': random.randint(1, 30)})
data['distance'] = distance

json_data = json.dumps(data)

print(json_data)
