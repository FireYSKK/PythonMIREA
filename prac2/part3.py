import random
import string
from itertools import groupby

s = ['15', '23', '42', '42']

# 1
print("1.", s, [int(j) for j in s])

# 2
print("2.", len(set(s)))

# 3
print("3.", list(reversed(s)))

# 4
s = [42, 42, 42, 42, 15, 23, 42, 42]
print("4.", list(set([(s[i:].index(42) + i) for i in range(len(s))])))

# 5
print("5.", sum(s[i] if i % 2 == 0 else 0 for i in range(len(s))), 42+42+15+42)

# 6
s = ['Lorem', 'ipsum', 'dolor', 'sit', 'amer', 'очень длинная строка']
print("6.", s[[len(iter_str) for iter_str in s].index(max([len(iter_str) for iter_str in s]))])

# 7
num = 42
print("7.", num % sum(list(int(iter_digit) for iter_digit in str(num))) == 0)

# 8
str_len = 15
print("8.", ''.join([string.ascii_letters[random.randrange(52)] for _ in range(str_len)]))

# 9
rle_encode = 'ABBCCCDEFAABBBCDD'
print("9.", [(symb[0], len(symb)) for symb in [''.join(g) for _, g in groupby(rle_encode)] ])