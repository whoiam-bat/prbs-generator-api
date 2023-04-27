def generate_prbs(degree, polynomial):
    seed = 0b1
    rang = (2 ** degree) - 1
    start = seed

    result = {
        'degree': degree, 'polynomial': polynomial, 'seed': to_binary(seed, degree), 'prbs': '',
        'rang_formula': 0, 'rang_experimental': 0, 'polynomial_type': '',
        'register_states': [], 'accompanying_matrix': []
    }

    taps = get_polynomial_degrees(polynomial)

    i = 0
    while True:
        i += 1
        out = 0
        for it in taps:
            out ^= ((start >> it) & 0b1)

        start = (start >> 1) | (out << (degree - 1))

        result['prbs'] += str(start & 1)
        result['register_states'].append(to_binary(start, degree))
        if start == seed: break

    result['rang_formula'] = rang
    result['rang_experimental'] = i

    if i == rang: result['polynomial_type'] = 'M-sequence'
    else: result['polynomial_type'] = 'C-sequence'

    return result


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
