from Coordinate import Coordinate
from typing import List
import itertools as it
import multiprocessing as mp


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


def evaluate_bnb(distances, perm, n, best_found):
    result = 0
    for i in range(n - 1):
        result += distances[perm[i]][perm[i + 1]]
        if result >= best_found:
            return False, i

    result = result + distances[perm[-1]][perm[0]]
    return True, result


def perms_prefix_bnb(distances, n, s):
    perm = [a for a in range(n) if a != s]
    best_found = 100000000
    skip = False
    val = 0
    current = 0

    for p in it.permutations(perm):
        perm = [s]
        perm.extend(p)

        if skip:
            if perm[val] == current:
                continue
            else:
                skip = False
                success, val = evaluate_bnb(distances, perm, n, best_found)
        else:
            success, val = evaluate_bnb(distances, perm, n, best_found)

        if success:
            if val < best_found:
                best_found = val
        else:
            current = perm[val]
            skip = True

    return best_found


def main():
    coords_list = open_file()
    x = 10
    coords_list = coords_list[:x]
    matrix = create_matrix(coords_list)
    Is = list(range(0, x))

    with mp.Pool(processes=9) as pool:
        ret = pool.starmap(perms_prefix_bnb, zip(it.repeat(matrix), it.repeat(x), Is))

    print(ret)


if __name__ == '__main__':
    main()
