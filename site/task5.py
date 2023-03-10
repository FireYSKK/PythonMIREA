def main(x: list, z: list, y: list):
    s = 0
    n = len(x)
    for i in range(n):
        s += 44 * (((z[n - 1 - i] ** 3) / 5 + 93 * y[i // 4]
                    + (x[i] ** 2) / 16) ** 3)
    return 66 * s


# print(
#     '{:.2e}'.format(main([-0.2, 0.48, 0.26, -0.92, 0.48],
#          [0.84, 0.35, 0.52, 0.76, -0.89],
#          [0.1, -0.84, 0.83, 0.41, -0.02])),
#     '{:.2e}'.format(main([-0.64, 0.7, -0.54, -0.2, 0.81],
#          [-0.74, 0.56, -0.75, 0.1, 0.09],
#          [0.03, 0.2, 0.24, 0.02, -0.48])),
#     '{:.2e}'.format(main([-0.31, 0.14, -0.81, -0.66, 0.62],
#          [-0.63, 0.33, 0.11, 0.56, -0.26],
#          [0.84, 0.53, 0.7, -0.33, 0.8])),
#     '{:.2e}'.format(main([0.56, -0.48, 0.46, 0.16, -0.08],
#          [-0.0, -0.4, -0.78, -0.59, -0.02],
#          [-0.51, -0.97, 0.11, 0.14, -0.14])),
#     '{:.2e}'.format(main([0.28, 0.06, 0.51, 0.19, -0.15],
#          [0.24, 0.52, -0.13, -0.79, 0.69],
#          [0.58, -0.9, -0.93, -0.63, -0.71])),
# )
