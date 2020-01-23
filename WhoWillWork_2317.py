N, K = map(int, input().split())
schedule = []
for i in range(N):
	schedule.append([0,0])
for _ in range(K):
	start, end, workers = map(int, input().split())
	worker = []
	for i in range(N):
		if start > schedule[i][1] and workers > 0:
			schedule[i][0] = start
			schedule[i][1] = end
			worker.append(i+1)
			workers -= 1 
	if sum(worker) == 0:
		print(-1)
	else:
		print(sum(worker))

