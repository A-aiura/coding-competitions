import math
from functools import reduce

# 最小公倍数を返す(引数が3つ以上でもOK)
def gcd_all(*numbers):
    return reduce(math.gcd, numbers)

# 引数Nの素数をlistで返す
def factorize(N):
    A = []
    
    i = 2
    while N % i == 0:
        A.append(i)
        N //= i

    i = 3
    while i * i <= N:
        if N % i == 0:
            A.append(i)
            N //= i
        else:
            i += 2
    
    if N != 1:
        A.append(N)
    
    return A

N = int(input())

A = list(map(int, input().split()))
'''
# 正解者のを参照
flg = 0
judge = 0
for i in range(N-1):
	judge = math.gcd(judge, math.gcd(A[i],A[i+1]))
	if judge != 1: flg = 1
'''

# 定義通り
flg = 0
for i in range(N):
	a = A[i]
	for j in range(i+1,N):
		judge = math.gcd(a,A[j])
		if judge != 1: flg = 1

if flg == 1:
	print("pairwise coprime")
	exit()

judge = gcd_all(*A)

if judge == 1:
	print("setwise coprime")
else:
	print("not coprime")

'''

3
3 4 5

pairwise coprime

3
6 10 15

setwise coprime

3
6 10 16

not coprime

'''