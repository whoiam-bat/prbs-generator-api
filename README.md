# API contains 2 algorithms of generating pseudo random binary sequence

## Linear Feedback Shift Register (LFSR) Algorithm

A Linear Feedback Shift Register (LFSR) is a mathematical algorithm used for generating a sequence of binary digits. It is commonly used in the field of cryptography, digital signal processing, and error-correcting codes.
The LFSR algorithm involves a shift register, which is a sequence of flip-flops that can be shifted left or right by one position at each clock cycle. The output of the LFSR is obtained by taking a linear combination of the bits in the shift register, where the coefficients are either 0 or 1.

### How it Works

The LFSR algorithm works by taking the initial state of the shift register, which is usually a random sequence of binary digits. At each clock cycle, the bits in the shift register are shifted one position to the left or right, and a new bit is inserted into the shift register.
The new bit is obtained by taking a linear combination of the bits in the shift register, where the coefficients are determined by a feedback polynomial. The feedback polynomial determines which bits are combined to produce the new bit, and which bits are discarded.
The output of the LFSR is obtained by reading the output bit of the shift register at each clock cycle. The output sequence is typically a pseudo-random sequence, which appears to be random but is actually deterministic.


## Matrix Shift Register (MSR) Algorithm

to be continued...


## Call API endpoint
``http://127.0.0.1:8000/docs`` - this is a main page with documentation to this API.