def bubblesort(L):
	for k in range(len(L), 1, -1):
		for i in range(0, k-1):
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]
	return L