from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Japanese technology", "country_of_origin": "Japan"},
        {"name": "Mercedes", "description": "German technology", "country_of_origin": "Germany"},
        {"name": "Audi", "description": "German technology", "country_of_origin": "Germany"},
        {"name": "Kia", "description": "Korean technology", "country_of_origin": "South Korea"},
        {"name": "Toyota", "description": "Japanese technology", "country_of_origin": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                country_of_origin=data['country_of_origin']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "engine_type": "V6", "horsepower": 284},
        {"name": "Qashqai", "type": "SUV", "year": 2019, "car_make": car_make_instances[0], "engine_type": "I4", "horsepower": 140},
        {"name": "XTRAIL", "type": "SUV", "year": 2017, "car_make": car_make_instances[0], "engine_type": "I4", "horsepower": 170},
        {"name": "A-Class", "type": "HATCHBACK", "year": 2020, "car_make": car_make_instances[1], "engine_type": "I4", "horsepower": 188},
        {"name": "C-Class", "type": "SEDAN", "year": 2025, "car_make": car_make_instances[1], "engine_type": "I4", "horsepower": 255},
        {"name": "E-Class", "type": "SEDAN", "year": 2024, "car_make": car_make_instances[1], "engine_type": "V6", "horsepower": 362},
        {"name": "A4", "type": "SEDAN", "year": 2024, "car_make": car_make_instances[2], "engine_type": "I4", "horsepower": 201},
        {"name": "A5", "type": "COUPE", "year": 2024, "car_make": car_make_instances[2], "engine_type": "I4", "horsepower": 261},
        {"name": "A6", "type": "SEDAN", "year": 2024, "car_make": car_make_instances[2], "engine_type": "V6", "horsepower": 335},
        {"name": "Sorrento", "type": "SUV", "year": 2014, "car_make": car_make_instances[3], "engine_type": "I4", "horsepower": 191},
        {"name": "Carnival", "type": "MINIVAN", "year": 2023, "car_make": car_make_instances[3], "engine_type": "V6", "horsepower": 290},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[3], "engine_type": "I4", "horsepower": 147},
        {"name": "Corolla", "type": "SEDAN", "year": 2022, "car_make": car_make_instances[4], "engine_type": "I4", "horsepower": 169},
        {"name": "Camry", "type": "SEDAN", "year": 2021, "car_make": car_make_instances[4], "engine_type": "V6", "horsepower": 301},
        {"name": "Kluger", "type": "SUV", "year": 2021, "car_make": car_make_instances[4], "engine_type": "I4", "horsepower": 203},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            engine_type=data['engine_type'],
            horsepower=data['horsepower']
        )
