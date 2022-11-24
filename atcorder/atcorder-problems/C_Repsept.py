
K = int(input())

# そもそも無理なやつをはじき出し
if (K%10) in [0, 2, 4, 5, 6, 8]:
	print(-1)
	exit()

# 割り切れるまで計算
K_mod = []
K_mod.append(7%K)
for i in range(1,K+1):
	if K_mod[i-1] == 0:
		print(i)
		exit()
	K_mod.append( (K_mod[i-1]*10 + 7) % K ) # 一個前のあまり*10+7

print(-1)

'''

101

4

2

-1

999983

999982

'''