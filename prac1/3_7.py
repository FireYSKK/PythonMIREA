def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y

def mul16(x, y) -> int:
    return mul_bits(x, y, 8) + ((mul_bits(x >> 8, y, 8) + mul_bits(x, y >> 8, 8)) << 8) + (mul_bits(x >> 8, y >> 8, 8) << 16)


for i in range(200, 300):
    for j in range(200, 300):
        assert (mul16(i, j) == i * j)

assert (mul16(65535, 65535) == 65535 * 65535)

print('good')