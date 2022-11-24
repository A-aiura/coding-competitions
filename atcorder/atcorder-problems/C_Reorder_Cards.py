# Input
H, W, N = map(int, input().split())

A, B = [], []
for i in range(N):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

A_dict = {a:i+1 for i,a in enumerate(sorted(list(set(A))))}
B_dict = {b:i+1 for i,b in enumerate(sorted(list(set(B))))}

# Output
for i in range(N):
	print(A_dict[A[i]], B_dict[B[i]])

'''
[Ex 1]
4 5 2
3 2
2 5

[Ex 2]
1000000000 1000000000 10
1 1
10 10
100 100
1000 1000
10000 10000
100000 100000
1000000 1000000
10000000 10000000
100000000 100000000
1000000000 1000000000

'''

'''
# Read
H, W, N = map(int, input().split())

A, B = [], []
for i in range(N):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

# Define others of A or B
Ao = list( set(list(range(1,H+1,1))) ^ set(A) )
Bo = list( set(list(range(1,W+1,1))) ^ set(B) )

ans = []
for (a, b) in zip(A, B):
	a_ans = a - len( [ao for ao in Ao if  ao<a] )
	b_ans = b - len( [bo for bo in Bo if  bo<b] )
	print(a_ans, b_ans)
'''






















