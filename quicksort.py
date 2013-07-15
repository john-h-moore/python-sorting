def find_pivot(unsorted):
	first = unsorted[0]
	middle = unsorted[len(unsorted)/2]
	last = unsorted[-1]
	if first <= middle <= last:
		return len(unsorted)/2
	elif middle <= first <= last:
		return 0
	else:
		return len(unsorted)-1

def quicksort(unsorted):
	quicksorted = []
	if len(unsorted) < 2:
		quicksorted += unsorted
	else:
		pivot = unsorted[find_pivot(unsorted)]
		lt = []
		gt = []
		for i in range(0, unsorted.index(pivot)):
			if unsorted[i] < pivot:
				lt.append(unsorted[i])
			else:
				gt.append(unsorted[i])
		for i in range(unsorted.index(pivot)+1, len(unsorted)):
			if unsorted[i] < pivot:
				lt.append(unsorted[i])
			else:
				gt.append(unsorted[i])
		quicksorted += quicksort(lt)
		quicksorted.append(pivot)
		quicksorted += quicksort(gt)
	return quicksorted