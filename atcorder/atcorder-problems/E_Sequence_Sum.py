# input
[N, X, M] = map(int, input().split())

A = X
SUM = A
for i in range(N-1):
	A = ( A*A ) % M
	SUM += A

print(SUM)

'''
6 2 1001

1369

1000 2 16

6

10000000000 10 99959

492443256176507

'''