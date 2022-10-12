from Coordinate import Coordinate
from typing import List
import numpy as np


def open_file():
    coords_list_l = []
    with open("/Users/alenamartinkova/Desktop/School/Ing./2. rok/PA/TSP/data.txt") as f:
        lines_after_7 = list(f.readlines())[7:]

        for line in lines_after_7:
            _, number, x, y = line.split(" ")
            coords_list_l.append(Coordinate(float(x), float(y)))

    return coords_list_l


def create_matrix(input_list: List[Coordinate]):
    output_matrix = []
    row_size = column_size = len(input_list) + 1

    for i in range(0, row_size):
        tmp = []

        for j in range(0, column_size):
            if i == j:
                tmp.append(0)
            else:
                tmp.append(input_list[j - 1])

        output_matrix.append(tmp)

    for row in output_matrix:
        print(row)

    return output_matrix


coords_list = open_file()
coords_list = coords_list[:4]
coords_list = [1, 2, 3, 4]
matrix = create_matrix(coords_list)

#print(coords_list)
