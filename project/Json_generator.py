import json
import random

json_data = {}
vehicles = []
add = 0
for i in range(30):
    add += random.randint(0, 1)
    vehicles.append(
        {'id': i+1, 'type': random.randint(1, 3), 'zipcode': 64151+add})
json_data['vehicles'] = vehicles

requests = []
for i in range(20):
    requests.append({'id': i+1, 'vehicle_type': random.randint(1, 3), 'zipcode': random.randint(
        vehicles[0]['zipcode'], vehicles[-1]['zipcode']), "vehicle_id": None, 'distance': 0})
json_data['requests'] = requests


vehicle_zip = [i for i in range(
    vehicles[0]['zipcode'], vehicles[-1]['zipcode']+1)]
distance = []
i = 0
while i <= 30:
    zipcode1 = random.choice(vehicle_zip)
    zipcode2 = random.choice(vehicle_zip)
    if zipcode1 == zipcode2:
        continue

    i += 1
    distance.append({'zipcode1': zipcode1, 'zipcode2': zipcode2,
                     'distance': random.randint(1, 30)})
json_data['distances'] = distance
