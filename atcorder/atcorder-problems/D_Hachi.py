'''
from collections import Counter

s = input()
cnt = Counter(s)
n = Counter(str(432))

print(cnt)
print(n)

if not n - cnt:
	print(n - cnt)

'''
s = int(input())
S = list(str(s))

if len(S) <= 2:
	if s%8 == 0:
		print("Yes")
		exit()
	s = int(S[1])*10 + int(S[0])
	if s%8 == 0:
		print("Yes")
		exit()

	print("No")
	exit()


for i in range(112, 1000, 8):
	num = list(str(i))
	count = 0
	for j in range(3):
		if num[j-count] in S:
			num.pop(j-count)
			count += 1
	if not num:
		print("Yes")
		exit()

print("No")




'''
S = int(input())

num = []
s = S
while True:
	s_mod = s%10
	num.append(int(s_mod))
	if s//10 == 0:
		break
	else:
		s = (s-s_mod)/10

for i in range(112,1000,8):


print("No")
'''