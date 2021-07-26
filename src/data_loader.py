import os
from src.utils.utils import convertListToInt, isValidCoordinateLength

# data diretory
directory = 'data'
allowed_extension = '.txt'

# load_data loads files in [directory]
def load_data():
    for filename in os.listdir(directory):
        if filename.endswith(allowed_extension):
            print("loading file "+filename)
            # join path
            path = os.path.join(directory, filename)
            # parse file
            return path
        else:
            continue

# parser parses given file based on delimiter
def parser(file_path):
    with open(file_path) as f:
        data = f.read()
        # remove leading/trailing white spaces
        data = data.strip()
        cars = [item.strip() for item in data.split(';')]
        # convert file to dict
        cars = convertToDect(cars)
        return cars

# convertToDect extracts cars to dict
def convertToDect(cars):
        cars_dic = {}
        for car in cars:
            car_cords = [item.strip() for item in car.split('|')]
            if len(car_cords)!=2:
                print("parsing error")
                continue
            car_cords_splitted = [item.strip() for item in car_cords[1].split('/')]
            splitted_cords = []
            for cor in car_cords_splitted:
                new_cor = cor.split("*")
                if not isValidCoordinateLength(new_cor):
                    continue
                splitted_cords.append(convertListToInt(new_cor))
            cars_dic[car_cords[0]] = splitted_cords
        return cars_dic

