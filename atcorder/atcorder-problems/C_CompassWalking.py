import numpy as np

[R, X, Y] = map(int, input().split())

r = np.sqrt(X**2 + Y**2)

count = r // R
if r%R == 0:
	print(count)
else:
	count += 1
	print(count)
