def pow15(x):
	x2 = x * x
	x4 = x2 * x2
	x8 = x4 * x4
	return x * x2 * x4 * x8


for i in range(100):
	assert (pow15(i) == i ** 15)

print("good")
