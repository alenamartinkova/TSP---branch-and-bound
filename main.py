from Coordinate import Coordinate
from typing import List
import itertools as it
import multiprocessing as mp
import time


def open_file():
    """
    Function that opens and reads file
    :return:
    """
    coords_list_l = []
    with open("/Users/alenamartinkova/Desktop/School/Ing./2. rok/PA/TSP/data.txt") as f:
        lines_after_7 = list(f.readlines())[7:]

        for line in lines_after_7:
            _, number, x, y = line.split(" ")
            coords_list_l.append(Coordinate(float(x), float(y)))

    return coords_list_l


def create_matrix(input_list: List[Coordinate]):
    """
    Function that creates matrix of distances from coordinates
    :param input_list:
    :return:
    """
    output_matrix = []
    row_size = column_size = len(input_list)

    for i in range(0, row_size):
        tmp = []
        for j in range(0, column_size):
            tmp.append(0)

        output_matrix.append(tmp)

    for i in range(len(output_matrix)):
        for j in range(len(output_matrix)):
            if i != j:
                output_matrix[i][j] = output_matrix[j][i] = input_list[i].distance(input_list[j])

    return output_matrix


def get_value_or_index(distances, perm, n, best):
    """
    Function that counts distance for route
    :param distances:
    :param perm:
    :param n:
    :param best:
    :return:
    """
    result = 0
    route = ''
    for i in range(n - 1):
        result += distances[perm[i]][perm[i + 1]]
        route += str(perm[i])
        if result >= best:
            return False, i, route

    result = result + distances[perm[-1]][perm[0]]
    return True, result, route


def branch_and_bound(matrix_distances, n, s):
    """
    Function that counts branch and bound for root
    :param matrix_distances:
    :param n:
    :param s:
    :return:
    """
    permutations = [a for a in range(n) if a != s]
    best = 9999999
    skip = False
    value = 0
    current = 0
    best_route = ''

    for permutation in it.permutations(permutations):
        permutations = [s]
        permutations.extend(permutation)

        if skip:
            if permutations[value] == current:
                continue
            else:
                skip = False
                success, value, route = get_value_or_index(matrix_distances, permutations, n, best)
        else:
            success, value, route = get_value_or_index(matrix_distances, permutations, n, best)

        if success:
            if value < best:
                best = value
                best_route = route
        else:
            current = permutations[value]
            skip = True

    best_route = best_route + best_route[0]

    return best, best_route


def main():
    start = time.time()
    coords_list = open_file()
    x = 10
    coords_list = coords_list[:x]
    matrix = create_matrix(coords_list)
    range_list = list(range(0, x))

    with mp.Pool(processes=1) as pool:
        ret = pool.starmap(branch_and_bound, zip(it.repeat(matrix), it.repeat(x), range_list))

    print(ret)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
