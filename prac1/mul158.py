def mul158(x):
	x2 = x + x
	x4 = x2 + x2
	x8 = x4 + x4
	x16 = x8 + x8
	x32 = x16 + x16
	x64 = x32 + x32
	x128 = x64 + x64
	return x2 + x4 + x8 + x16 + x128


for i in range(100):
	assert (mul158(i) == i * 158)

print("good")
