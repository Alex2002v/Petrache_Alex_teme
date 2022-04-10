import json
import csv
import uuid

id1 = uuid.uuid4()
id2 = uuid.uuid4()
id3 = uuid.uuid4()
id4 = uuid.uuid4()
id5 = uuid.uuid4()
id6 = uuid.uuid4()
id7 = uuid.uuid4()
id8 = uuid.uuid4()
id9 = uuid.uuid4()

cars = [{'id': id(id1),
         'brand': 'Toyota',
         'model': 'hatchback',
         'hp': 76,
         'price': 400},
        {'id': id(id2),
         'brand': 'Toyota',
         'model': 'suv',
         'hp': 99,
         'price': 600},
        {'id': id(id3),
         'brand': 'Mazda',
         'model': 'sedan',
         'hp': 88,
         'price': 800},
        {'id': id(id4),
         'brand': 'Peugeot',
         'model': 'universal',
         'hp': 150,
         'price': 750},
        {'id': id(id5),
         'brand': 'Peugeot',
         'model': 'roadster',
         'hp': 116,
         'price': 870},
        {'id': id(id6),
         'brand': 'VW Passat',
         'model': 'sedan',
         'hp': 120,
         'price': 1300},
        {'id': id('cars'),
         'brand': 'VW Passat',
         'model': 'coupe',
         'hp': 180,
         'price': 1580},
        {'id': id(id7),
         'brand': 'VW Passat',
         'model': 'coupe',
         'hp': 220,
         'price': 3024},
        {'id': id(id8),
         'brand': 'Mazda',
         'model': 'coupe',
         'hp': 250,
         'price': 5400},
        {'id': id(id9),
         'brand': 'Mazda',
         'model': 'targa',
         'hp': 280,
         'price': 5900}, ]


slow_cars = []
fast_cars = []
sport_cars = []

cheap_car = []
medium_car = []
expensive_car = []

toyota_brand_car = []
peugeot_brand_car = []
mazda_brand_car = []
vw_passat_brand_car = []


for car in cars:
    if car['hp'] < 120:
        slow_cars.append(car)
        slow_cars = sorted(slow_cars, key=lambda x: x['hp'])
    elif car['hp'] < 180:
        fast_cars.append(car)
        fast_cars = sorted(fast_cars, key=lambda x: x['hp'])
    elif car['hp'] >= 180:
        sport_cars.append(car)
        sport_cars = sorted(sport_cars, key=lambda x: x['hp'])

    if car['price'] < 1000:
        cheap_car.append(car)
        cheap_car = sorted(cheap_car, key=lambda x: x['price'])
    elif car['price'] < 5000:
        medium_car.append(car)
        medium_car = sorted(medium_car, key=lambda x: x['price'])
    elif car['price'] >= 5000:
        expensive_car.append(car)
        expensive_car = sorted(expensive_car, key=lambda x: x['price'])

    if car['brand'] == 'Toyota':
        toyota_brand_car.append(car)
    elif car['brand'] == 'Peugeot':
        peugeot_brand_car.append(car)
    elif car['brand'] == 'Mazda':
        mazda_brand_car.append(car)
    elif car['brand'] == 'VW Passat':
        vw_passat_brand_car.append(car)

print('\n', 'cars =', cars, '\n')

print('slow_cars =', slow_cars)
print('fast_cars =', fast_cars)
print('sport_cars =', sport_cars, '\n')

print('cheap_car =', cheap_car)
print('medium_car =', medium_car)
print('expensive_car =', expensive_car, '\n')

print('brand_car =', toyota_brand_car)
print('brand_car =', peugeot_brand_car)
print('brand_car =', mazda_brand_car)
print('brand_car =', vw_passat_brand_car)


with open('output_data/slow_cars.json', 'w') as json_file:
    json.dump(slow_cars, json_file, indent=2)

with open('output_data/fast_cars.json', 'w') as json_file:
    json.dump(fast_cars, json_file, indent=2)

with open('output_data/sport_cars.json', 'w') as json_file:
    json.dump(sport_cars, json_file, indent=2)

with open('output_data/cheap_car.json', 'w') as json_file:
    json.dump(cheap_car, json_file, indent=2)

with open('output_data/medium_car.json', 'w') as json_file:
    json.dump(medium_car, json_file, indent=2)

with open('output_data/expensive_car.json', 'w') as json_file:
    json.dump(expensive_car, json_file, indent=2)


with open('output_data/toyota_brand_car.json', 'w') as json_file:
    json.dump(toyota_brand_car, json_file, indent=2)

with open('output_data/peugeot_brand_car.json', 'w') as json_file:
    json.dump(peugeot_brand_car, json_file, indent=2)

with open('output_data/mazda_brand_car.json', 'w') as json_file:
    json.dump(mazda_brand_car, json_file, indent=2)

with open('output_data/vw_passat_brand_car.json', 'w') as json_file:
    json.dump(vw_passat_brand_car, json_file, indent=2)


with open('input.csv', 'w') as my_file:
    writer = csv.writer(my_file)
    keys = cars[0].keys()
    writer.writerow(keys)
    for car in cars:
        writer.writerow(car.values())
