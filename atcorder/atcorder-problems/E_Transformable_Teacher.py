
# input
[N, M] = map(int, input().split())
# input H:student's height
H = list(map(int, input().split()))
# input W:teacher's height
W = list(map(int, input().split()))

# calc sum of differences in pares
SUM = float('inf')
for w in W:
	h = list(H)
	h.append(w)
	h.sort()

	s = 0
	for j in range(0,N+1,2):
		s = s+abs(h[j] - h[j+1])
		if s > SUM:
			break

	if s < SUM:
		SUM = s

print(SUM)

'''

5 3
1 2 3 4 7
1 3 8

3

7 7
31 60 84 23 16 13 32
96 80 73 76 87 57 29

34

15 10
554 525 541 814 661 279 668 360 382 175 833 783 688 793 736
496 732 455 306 189 207 976 73 567 759

239

'''