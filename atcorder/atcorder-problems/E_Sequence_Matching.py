
def solve(N, M, A, B):
	# N行M列の0行列を定義
    dp = [[0]*(M+1) for _ in range(N+1)]

    # 1列目に0からNまで数字を代入
    for j in range(N+1):
        dp[j][0] = j

    # 1行目に0からMまで数字を代入
    for i in range(M+1):
        dp[0][i] = i

    # 2行2列目スタート
    for j in range(1, N+1):
        for i in range(1, M+1):
            dp[j][i] = min(　# 以下の3つの中で最小の値を渡す
                dp[j-1][i] + 1, # 1つ前の行の値+1
                dp[j][i-1] + 1, # 1つ前の列の値+1
                dp[j-1][i-1] + (A[j-1] != B[i-1]) # (a != b)はTureなら0, Falseなら1を返す
            )

    return dp[N][M]

# input num of A, num of B
[N,M] = map(int,input().split())
# input A, B
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# output
print(solve(N,M,A,B))



'''

4 3
1 2 1 3
1 3 1

2

4 6
1 3 2 4
1 5 2 6 4 3

3

5 5
1 1 1 1 1
2 2 2 2 2

5

'''