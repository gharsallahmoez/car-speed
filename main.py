from src.calcul import calcul_speed
from src.data_loader import load_data, parser

if __name__ == '__main__':
    # main program
    path = load_data()
    data = parser(path)

    for key, value in data.items():
        speed = calcul_speed(value)
        if speed >= 5:
            print('ID : ',key, ' Speed : ',speed, 'm/s')