#MikeAndCompression_592

N, Q = map(int, input().split())

tree = []

for i in range(N+1):
	x = []
	tree.append(x)

for _ in range(N-1):
	u, v = map(int, input().split())
	tree[u].append(v)
	tree[v].append(u)

for _ in range(Q):
	K = int(input())
	Y = len(tree[K])
	print(N - Y - 1)