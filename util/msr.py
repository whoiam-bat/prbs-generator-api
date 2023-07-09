import copy
import math

import numpy as np


def generate_prbs(rankA, rankB, polyA, polyB, rankS, it, jt):
    matrix_a = generate_matrix_a(rankA, polyA)
    matrix_b = generate_matrix_b(rankB, polyB)
    matrix_s = generate_init_matrix_s(rankS, rankA, rankB)

    period_a = (2 ** rankA) - 1
    period_b = (2 ** rankB) - 1

    result = {
        'matrA': matrix_to_str_arr(matrix_a), 'matrB': matrix_to_str_arr(matrix_b),
        'periodA': period_a, 'periodB': period_b, 'stateMatrixS': [matrix_to_str_arr(matrix_s)],
        'analS': 0, 'theorS': 0, 'hammingWeightTheoretical': 0,
        'hammingWeightPractice': 0, 'polynomialA': '', 'polynomialB': '', 'prbs': '', 'prbsIndexes': [], 'acf': []
    }

    numpy_a = np.array(matrix_a)
    numpy_b = np.array(matrix_b)
    numpy_s = np.array(matrix_s)

    current_state = numpy_s
    while(True):
        prbs_state = current_state[it - 1][jt - 1]
        if prbs_state == 1:
            result['hammingWeightPractice'] += 1
        result['prbs'] += str(prbs_state)

        temp = current_state.tolist()
        result['stateMatrixS'].append(matrix_to_str_arr(temp))

        current_state = np.dot(np.dot(numpy_a, current_state), numpy_b) % 2
        if np.array_equal(current_state, numpy_s):
            break

    result['polynomialA'] = get_function(polyA)
    result['polynomialB'] = get_function(polyB)
    result['analS'] = len(result['prbs'])
    result['prbsIndexes'] = get_sequence_indexes(result['prbs'])
    result['acf'] = get_acf(convert_prbs_for_acf([int(x) for x in result['prbs']]))

    if period_a == period_b:
        result['hammingWeightTheoretical'] = result['hammingWeightPractice']
        result['theorS'] = math.lcm(period_b, period_a)
    else:
        result['hammingWeightTheoretical'] = get_theor_hamming(rankA, rankB, rankS)
        result['theorS'] = period_a * period_b

    return result


def convert_prbs_for_acf(sequence):
    return [1 if it == 1 else -1 for it in sequence]


def get_theor_hamming(rankA, rankB, rankS):
    return ((2 ** rankS) - 1) * (2 ** (rankB + rankA - rankS - 1))


def get_function(polynomial):
    binaryArray = [1]
    binaryArray += poly_to_num_arr(polynomial)
    result = ''
    length = len(binaryArray)
    for i, curr in enumerate(binaryArray):
        if curr == 1:
            if i == length - 1:
                result += "1"
            else:
                result += f"x^{length - i - 1} + "
    return result


def poly_to_num_arr(poly):
    return [int(bit) for bit in poly]


def matrix_to_str_arr(matrix):
    string_array = []
    for row in matrix:
        string_array.append(''.join(str(element) for element in row))
    return string_array


def generate_matrix_a(rankA, polyA):
    structural_matrix = [[] for _ in range(rankA)]
    structural_matrix[0] = poly_to_num_arr(polyA)

    identity = [[int(i == j) for j in range(rankA)] for i in range(rankA - 1)]
    identity = copy.deepcopy(identity)

    for i in range(rankA - 1):
        structural_matrix[i + 1] = poly_to_num_arr(identity[i])

    return structural_matrix


def generate_matrix_b(rankB, polyB):
    structural_matrix = [[int(i == j) for j in range(rankB - 1)] for i in range(rankB)]
    first_col = poly_to_num_arr(polyB)

    temp = np.array(structural_matrix)
    matrix = np.insert(temp, 0, first_col, axis=1).astype(int)

    return matrix.tolist()


def generate_init_matrix_s(rankS, rankA, rankB):
    matrix = [[0 for _ in range(rankB)] for _ in range(rankA)]
    for i in range(rankA):
        for j in range(rankB):
            if i < rankS:
                if i == j:
                    matrix[i][j] = 1
    return matrix


def get_acf(sequence):
    correlation = np.correlate(sequence, sequence, mode='same')

    normalization = np.dot(sequence, sequence)
    res = correlation / normalization

    temp = [round(num, 7) for num in res]
    new_arr = [1] + temp[:temp.index(1)] + temp[temp.index(1) + 1:] + [1]

    return new_arr


def get_sequence_indexes(sequence):
    res = [i for i in range(len(sequence) + 1)]
    return res
