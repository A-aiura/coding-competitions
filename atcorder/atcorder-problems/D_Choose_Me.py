
N = int(input())

X = []
x = 0
for i in range(N):
	A, B = map(int, input().split())
	x -= A
	X.append(A+A+B)
X.sort()

count = 0
while x <= 0:
	x += X.pop()
	count += 1

print(count)

'''
4
2 1
2 2
5 1
1 3

1

5
2 1
2 1
2 1
2 1
2 1

3


'''

'''


N = int(input())

AB = [list(map(int, input().split())) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

if N == 1:
	print(1)
	exit()

SUM = [A[i] + B[i] for i in range(N)]
SUM_sort = sorted(SUM,reverse=True)

SUM_idx = []
for i in range(N):
	for j in range(N):
		if (SUM[j] == SUM_sort[i]) and (j not in SUM_idx):
			SUM_idx.append(j)

count = 0
sum_acc = SUM_sort[0]
for i in range(1,N):
	A_vote = 0
	for j in range(N):
		if SUM_idx[i-1] != j:
			A_vote += A[j]
	
	if sum_acc > A_vote:
		count += 1
		break
	else:
		sum_acc += SUM_sort[i]
		count += 1

print(count)





SUM_acc = []
SUM_acc.append(SUM_sort[0])
for i in range(1,N):
	SUM_acc.append(SUM_acc[i-1] + SUM_sort[i])
'''

