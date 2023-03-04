def fast_mul_gen(y):
    func_text = f'def mul{y}(x):\n'
    bits = bin(y)[2:]
    print(bits)
    return_string = "\treturn "
    flag = False
    if bits[-1] == '1':
        return_string += 'x'
        flag = True
    for i in range(1,len(bits)):
        func_text += f'\tx{2**i} = x{2 ** (i - 1) if i > 1 else ""} + x{2 ** (i - 1) if i > 1 else ""}\n'
        if bits[len(bits) - 1 - i] == '1':
            if flag:
                return_string += f' + x{2**i}'
            else:
                return_string += f'x{2 ** i}'
                flag = True
    func_text += return_string
    return func_text


num = int(input())
generated_func = fast_mul_gen(num)
print(generated_func)
with open(f'mul{num}.py', 'w') as f:
    f.write(generated_func)
    f.write('\n' * 3)
    f.write(f'for i in range(100):\n\tassert (mul{num}(i) == i * {num})')
    f.write('\n\n')
    f.write('print("good")\n')
exec(open(f'mul{num}.py').read(), globals())
# print(eval(generated_func, {}, {'y': num}))
