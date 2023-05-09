import math


def generate_prbs(degree, polynomial, polynomial_gf2):
    seed = 0b1
    rang = (2 ** degree) - 1
    start = seed
    j = parse_polynomial_gf2(polynomial_gf2)

    result = {
        'degree': degree, 'polynomial': polynomial, 'seed': to_binary(seed, degree), 'prbs': '',
        'rang_formula': 0, 'rang_experimental': 0, 'polynomial_type': '', 'hamming_weight': 0,
        'register_states': [], 'accompanying_matrix': get_accompanying_matrix(polynomial, degree)
    }

    taps = get_polynomial_degrees(polynomial)

    while True:
        out = 0
        for it in taps:
            out ^= ((start >> it) & 0b1)

        start = (start >> 1) | (out << (degree - 1))

        if out & 0b1:
            result['hamming_weight'] += 1

        result['prbs'] += str(out & 0b1)
        result['register_states'].append(to_binary(start, degree))
        if start == seed: break

    result['rang_formula'] = rang
    result['rang_experimental'] = rang / (math.gcd(rang, j))

    if result['rang_formula'] == result['rang_experimental']:
        result['polynomial_type'] = 'M-sequence'
    else:
        result['polynomial_type'] = 'C-sequence'

    return result


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
        if polynomial[i] == '1': degrees.append(i)
    degrees.sort()

    return degrees


def to_binary(num, num_bits):
    binary_str = bin(num)[2:]
    padded_str = binary_str.zfill(num_bits)
    return padded_str


def parse_polynomial_gf2(polynomial_gf2):
    j = polynomial_gf2.split(" ")[0]
    return int(j)
