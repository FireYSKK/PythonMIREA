def main(x: list[5]):
    if x[1] == 'TXL':
        return 13

    if x[3] == 'TCL':
        return 7

    x0 = ['FLUX', 'OCAML', 'M4']
    list2 = [1986, 1974, 1966]
    list4 = ['EJS', 'LIMBO', 'CHUCK']

    x2 = list2.index(x[2])
    x4 = list4.index(x[4])

    if x[3] == 'RUST':
        return 3 * x2 + x0.index(x[0]) * (0 if x2 == 2 else 1)

    return 8 + 2 * x4 + (x2 - 1 if x4 == 1 else 0)


print(
    main(['OCAML', 'M4', 1986, 'RUST', 'CHUCK']),
    main(['M4', 'TXL', 1974, 'RUST', 'LIMBO']),
    main(['FLUX', 'M4', 1966, 'ALLOY', 'LIMBO']),
    main(['OCAML', 'M4', 1974, 'TCL', 'EJS']),
    main(['FLUX', 'M4', 1974, 'RUST', 'CHUCK']),
    main(['FLUX', 'M4', 1986, 'ALLOY', 'EJS'])
)
