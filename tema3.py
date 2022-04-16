import json
import csv
import uuid
import os


def main():
    cars = [{'id': id(uuid.uuid4),
             'brand': 'Toyota',
             'model': 'hatchback',
             'hp': 76,
             'price': 400},
            {'id': id(uuid.uuid4),
             'brand': 'Toyota',
             'model': 'suv',
             'hp': 99,
             'price': 600},
            {'id': id(uuid.uuid4),
             'brand': 'Mazda',
             'model': 'sedan',
             'hp': 88,
             'price': 800},
            {'id': id(uuid.uuid4),
             'brand': 'Peugeot',
             'model': 'universal',
             'hp': 150,
             'price': 750},
            {'id': id(uuid.uuid4),
             'brand': 'Peugeot',
             'model': 'roadster',
             'hp': 116,
             'price': 870},
            {'id': id(uuid.uuid4),
             'brand': 'VW Passat',
             'model': 'sedan',
             'hp': 120,
             'price': 1300},
            {'id': id('cars'),
             'brand': 'VW Passat',
             'model': 'coupe',
             'hp': 180,
             'price': 1580},
            {'id': id(uuid.uuid4),
             'brand': 'VW Passat',
             'model': 'coupe',
             'hp': 220,
             'price': 3024},
            {'id': id(uuid.uuid4),
             'brand': 'Mazda',
             'model': 'coupe',
             'hp': 250,
             'price': 5400},
            {'id': id(uuid.uuid4),
             'brand': 'Mazda',
             'model': 'targa',
             'hp': 280,
             'price': 5900}, ]

    toyota_brand_car = []
    peugeot_brand_car = []
    mazda_brand_car = []
    vw_passat_brand_car = []

    slow_cars = [car for car in cars if car['hp'] < 120]
    slow_cars = sorted(slow_cars, key=lambda x: x['hp'])

    fast_cars = [car for car in cars if 120 <= car['hp'] < 180]
    fast_cars = sorted(fast_cars, key=lambda x: x['hp'])

    sport_cars = [car for car in cars if car['hp'] >= 180]
    sport_cars = sorted(sport_cars, key=lambda x: x['hp'])

    cheap_car = [car for car in cars if car['price'] < 1000]
    cheap_car = sorted(cheap_car, key=lambda x: x['price'])

    medium_car = [car for car in cars if 1000 <= car['price'] < 5000]
    medium_car = sorted(medium_car, key=lambda x: x['price'])

    expensive_car = [car for car in cars if car['price'] >= 5000]
    expensive_car = sorted(expensive_car, key=lambda x: x['price'])

    for car in cars:
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

    dir_ = os.path.join('C:\\', 'Users', 'Alex', 'Desktop', 'Teme-09-python', 'output_data_tema3')
    if not os.path.exists(dir_):
        os.mkdir(dir_)

    with open('output_data_tema3/slow_cars.json', 'w') as json_file:
        json.dump(slow_cars, json_file, indent=2)

    with open('output_data_tema3/fast_cars.json', 'w') as json_file:
        json.dump(fast_cars, json_file, indent=2)

    with open('output_data_tema3/sport_cars.json', 'w') as json_file:
        json.dump(sport_cars, json_file, indent=2)

    with open('output_data_tema3/cheap_car.json', 'w') as json_file:
        json.dump(cheap_car, json_file, indent=2)

    with open('output_data_tema3/medium_car.json', 'w') as json_file:
        json.dump(medium_car, json_file, indent=2)

    with open('output_data_tema3/expensive_car.json', 'w') as json_file:
        json.dump(expensive_car, json_file, indent=2)

    with open('output_data_tema3/toyota_brand_car.json', 'w') as json_file:
        json.dump(toyota_brand_car, json_file, indent=2)

    with open('output_data_tema3/peugeot_brand_car.json', 'w') as json_file:
        json.dump(peugeot_brand_car, json_file, indent=2)

    with open('output_data_tema3/mazda_brand_car.json', 'w') as json_file:
        json.dump(mazda_brand_car, json_file, indent=2)

    with open('output_data_tema3/vw_passat_brand_car.json', 'w') as json_file:
        json.dump(vw_passat_brand_car, json_file, indent=2)


    with open('input_tema3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        keys = cars[0].keys()
        writer.writerow(keys)
        for car in cars:
            writer.writerow(car.values())


if __name__ == '__main__':
    main()
