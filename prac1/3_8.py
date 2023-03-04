def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16k(x, y):
    x1, x2 = x >> 8, x & (2 ** 8 - 1)
    y1, y2 = y >> 8, y & (2 ** 8 - 1)
    n, n1 = 16, 8
    mul1 = mul_bits(x1, y1, n1)
    mul2 = mul_bits(x2, y2, n1)
    mul3 = mul_bits(x1 + x2, y1 + y2, n)
    return (mul1 << n) - (mul1 << n1) + mul2 - (mul2 << n1) + (mul3 << n1)


for i in range(200, 300):
    for j in range(200, 300):
        assert (mul16k(i, j) == i * j)

assert (mul16k(65535, 65535) == 65535 * 65535)
print('good')