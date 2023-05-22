import numpy as np


def generate_prbs(degree, polynomial, polynomial_gf2):
    seed = 0b1
    rang = (2 ** degree) - 1
    start = seed
    j = parse_polynomial_gf2(polynomial_gf2)

    result = {
        'prbs': '', 'rang_formula': 0, 'rang_experimental': 0, 'polynomial_type': '', 'hamming_weight': 0,
        'register_states': [], 'accompanying_matrix': get_accompanying_matrix(polynomial, degree),
        'prbs_indexes': [], 'acf': []
    }

    taps = get_polynomial_degrees(polynomial)

    i = 0
    while True:
        i += 1
        out = 0
        for it in taps:
            out ^= ((start >> it) & 0b1)

        start = (start >> 1) | (out << (degree - 1))

        if out & 0b1:
            result['hamming_weight'] += 1

        result['prbs'] += str(out & 0b1)
        result['register_states'].append(to_binary(start, degree))
        if start == seed:
            break

    result['rang_formula'] = rang
    result['rang_experimental'] = i

    if result['rang_formula'] == result['rang_experimental']:
        result['polynomial_type'] = 'M-sequence'
    else:
        result['polynomial_type'] = ' S-sequence'

    result['prbs_indexes'] = get_sequence_indexes(result['prbs'])
    result['acf'] = get_acf([int(x) for x in result['prbs']])

    return result


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


def get_accompanying_matrix(polynomial, degree):
    accompanying_matrix = [polynomial]

    identity = [[int(i == j) for j in range(degree)] for i in range(degree - 1)]

    for i in range(degree - 1):
        temp = ''
        for j in range(degree):
            temp += str(identity[i][j])
        accompanying_matrix.append(temp)

    return accompanying_matrix


def get_polynomial_degrees(polynomial):
    polynomial = polynomial[::-1]

    degrees = []
    for i in range(len(polynomial)):
        if polynomial[i] == '1':
            degrees.append(i)
    degrees.sort()

    return degrees


def to_binary(num, num_bits):
    binary_str = bin(num)[2:]
    padded_str = binary_str.zfill(num_bits)
    return padded_str


def parse_polynomial_gf2(polynomial_gf2):
    j = polynomial_gf2.split(" ")[0]
    return int(j)
