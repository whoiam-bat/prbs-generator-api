# API contains 2 algorithms of generating pseudo random binary sequence

## Linear Feedback Shift Register (LFSR) Algorithm

A Linear Feedback Shift Register (LFSR) is a mathematical algorithm used for generating a sequence
of binary digits. It is commonly used in the field of cryptography, digital signal processing, and
error-correcting codes.
The LFSR algorithm involves a shift register, which is a sequence of flip-flops that can be shifted
left or right by one position at each clock cycle. The output of the LFSR is obtained by taking a
linear combination of the bits in the shift register, where the coefficients are either 0 or 1.

### How it Works

The LFSR algorithm works by taking the initial state of the shift register, which is usually a
random sequence of binary digits. At each clock cycle, the bits in the shift register are shifted
one position to the left or right, and a new bit is inserted into the shift register.
The new bit is obtained by taking a linear combination of the bits in the shift register, where the
coefficients are determined by a feedback polynomial. The feedback polynomial determines which bits
are combined to produce the new bit, and which bits are discarded.
The output of the LFSR is obtained by reading the output bit of the shift register at each clock
cycle. The output sequence is typically a pseudo-random sequence, which appears to be random but is
actually deterministic.

## Matrix Shift Register (MSR) Algorithm

The MFSR algorithm is used in a variety of applications, including cryptography, digital
communications, and circuit testing. In cryptography, the MFSR can be used to generate pseudorandom
keys for encryption algorithms.
In digital communications, the MFSR can be used to generate pseudorandom noise sequences for
scrambling signals. In circuit testing, the MFSR can be used to generate test patterns for digital
circuits.

The MFSR algorithm is a powerful tool for generating pseudorandom sequences. It is relatively easy
to implement in hardware and software, and it can be used in a variety of applications. However, it
is important to be aware that the output sequences of an MFSR are not truly random. They are
deterministic and can be predicted given the initial state of the register.

### How it works

The Matrix Shift Register Algorithm (MFSR) works by generating a sequence of bits from a linear
feedback shift register (LFSR). The LFSR is a circuit that has a number of bits, each of which can
be either a 0 or a 1. The bits are shifted one position to the right at each clock cycle, and the
output bit is determined by a linear function of the previous state of the register.

The MFSR algorithm extends the LFSR algorithm by adding a matrix to the linear function. The matrix
can be any square matrix, but it is typically chosen to be a Hadamard matrix. The Hadamard matrix is
a matrix that has the property that the sum of each row and column is equal to 1.

The output bit of the MFSR algorithm is determined by the following equation:

```output_bit = matrix * previous_state + previous_output```
where:

- ```matrix``` is the Hadamard matrix
- ```previous_state``` is the previous state of the LFSR
- ```previous_output``` is the previous output bit


The MFSR algorithm can generate more complex and unpredictable sequences than the LFSR algorithm
because the matrix introduces non-linearity into the function. This makes it more difficult to
predict the output of the MFSR algorithm from its previous state.

## Call API endpoint

`http://127.0.0.1:8000/docs` - this is a main page with documentation to this API, if you are going to run locally.

`https://generatorapi-1-a7624134.deta.app/docs` - this is the same API but deployed to the remote server.

`https://prbs-generator.netlify.app` - this is the URL to get complete application.