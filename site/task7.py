# 01101010 10001 0 1000001 1111 0000110
# 000 001101010 1 00000 1000001 0000110

# 01011101 11100 1 1101111 0001 0011001
# 000 001011111 0 00001 1101111 0011001

# 00100110 00101 1 1001111 1011 1011000
# 000 000100110 1 00001 1001111 1011000

# 101011001 00011 1 0101110 1001 1100011
#  000 101011001 1 00001 0101110 1100011


def main(s: str):
    num = int(s)
    h1 = num & 127
    h3 = (num & (127 << 11)) >> 11
    h4 = (num & (1 << 18)) >> 18
    h5 = (num & (31 << 19)) >> 19
    h6 = num >> 24

    new_num = (h6 << 20) | (h4 << 19) | (h5 << 14) | (h3 << 7) | h1

    return str(new_num)


print(main('1787432838'))
print(main('1575450777'))
print(main('640581080'))
print(main('5790069987'))