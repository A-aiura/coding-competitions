
# input
[H, W, N, M] = map(int, input().split())
 
# make Field
Field = [[0]*W for _ in range(H)]
 
# input location of Lump
Light = [list(map(int, input().split())) for i in range(N)]

# input location of Block
for i in range(M):
	[c, d] = map(int, input().split())
	Field[c-1][d-1] = -1

count = 0
for A, B in Light:
	A = A-1 # change into idx num
	B = B-1
	a = A
	b = B
	for i in range(H+1): # up
		if a == H:
			a = A
			break
		elif Field[a][b] == -1:
			a = A
			break
		elif Field[a][b] == 1:
			a = a+1
		else:
			Field[a][b] = 1
			a = a+1
			count = count+1
	for i in range(H+1): # down
		if a < 0:
			a = A
			break
		elif Field[a][b] == -1:
			a = A
			break
		elif Field[a][b] == 1:
			a = a-1
		else:
			Field[a][b] = 1
			a = a-1
			count = count+1
 
	for i in range(W+1): # right
		if b == W:
			b = B
			break
		elif Field[a][b] == -1:
			b = B
			break
		elif Field[a][b] == 1:
			b = b+1
		else:
			Field[a][b] = 1
			b = b+1
			count = count+1
 
	for i in range(W+1): # left
		if b < 0:
			b = B
			break
		elif Field[a][b] == -1:
			b = B
			break
		elif Field[a][b] == 1:
			b = b-1
		else:
			Field[a][b] = 1
			b = b-1
			count = count+1

print(count)




'''
# numpy Ver

from numpy import zeros

# input
H, W, N, M = input().split(" ")
H = int(H) # line
W = int(W) # column
N = int(N) # Lump
M = int(M) # Block

# make Field
Field = zeros((H,W), dtype = int)

# input location of Lump
A = []
B = []
for i in range(N):
	a, b = input().split(" ")
	a = int(a)-1 # change into idx num
	b = int(b)-1 # change into idx num
	A.append(a)
	B.append(b)
	Field[int(a)][int(b)] = 1

# input location of Block
for i in range(M):
	C, D = input().split(" ")
	C = int(C) - 1
	D = int(D) - 1
	Field[C][D] = -1

# turn 0 into 1 if not -1
for i in range(N):
	a = A[i]
	b = B[i]
	while True: # up
		if (a == H) or (Field[a][b] == -1):
			a = A[i]
			break
		else:
			Field[a][b] = 1
			a = a+1

	while True: # down
		if (a < 0) or (Field[a][b] == -1):
			a = A[i]
			break
		else:
			Field[a][b] = 1
			a = a-1

	while True: # right
		if (b == W) or (Field[a][b] == -1):
			b = B[i]
			break
		else:
			Field[a][b] = 1
			b = b+1

	while True: # left
		if (b < 0) or (Field[a][b] == -1):
			b = B[i]
			break
		else:
			Field[a][b] = 1
			b = b-1

count = 0
for i in range(H):
	for j in range(W):
		if Field[i][j] == 1:
			count = count + 1

# print(Field)
print(count)

'''


'''

3 3 2 1
1 1
2 3
2 2

7

4 4 3 3
1 2
1 3
3 4
2 3
2 4
3 2

8

5 5 5 1
1 1
2 2
3 3
4 4
5 5
4 2

24

'''