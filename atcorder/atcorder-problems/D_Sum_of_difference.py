
N = int(input())
 
A = list(map(int, input().split()))
A.sort()

A_acc = []
A_acc.append(A[0])
for i in range(1,N):
	A_acc.append(A_acc[i-1] + A[i])
 
A_sum = sum(A)
SUM = 0
for i in range(N):
	SUM += (A_sum - A_acc[i]) - (N-i-1)*A[i]

print(SUM)

'''
3
5 1 2

8

5
31 41 59 26 53

176

'''