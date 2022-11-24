
N, M = map(int, input().split())

if M == 0:
	print(1)
	exit()

A = list(map(int, input().split()))
A.sort()
A.append(N+1)

if N == M:
	print(0)
	exit()

Blanc = []
tmp = 0
for i in range(M+1):
	Blanc.append(A[i] - tmp - 1)
	tmp = A[i]

Blanc.sort()
if Blanc[0] == 0:
	for i in range(M+1):
		if Blanc[i] != 0:
			k = Blanc[i]
			begin = i
			break
else:
	k = Blanc[0]
	begin = 0

count = 0
for i in range(begin,M+1):
	if Blanc[i]%k == 0:
		count += Blanc[i]//k
	else:
		count += (Blanc[i]//k) + 1

print(count)

'''

5 2
1 3

3

13 3
13 3 9

6

5 5
5 2 1 4 3

0

1 0

1

'''