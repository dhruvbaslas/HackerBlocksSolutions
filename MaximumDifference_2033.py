T = int(input())
import math
for _ in range(T):
	N = int(input())
	A = list(map(int, input().split()))
	max_diff = -1*math.inf
	min_ele = A[0]
	for i in range(1, N):
		if A[i] - min_ele > max_diff:
			max_diff = A[i] - min_ele
		if A[i] < min_ele:
			min_ele = A[i]
	print(max_diff)

