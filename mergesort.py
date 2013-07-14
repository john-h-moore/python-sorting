def merge(left, right):
	sortedlist = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sortedlist.append(left[i])
			i += 1
		elif left[i] > right[j]:
			sortedlist.append(right[j])
			j += 1
		else:
			sortedlist.append(left[i])
			sortedlist.append(right[j])
			i += 1
			j += 1
	if i < len(left):
		sortedlist += left[i:]
	elif j < len(right):
		sortedlist += right[j:]
	return sortedlist

def mergesort(unsorted):
	if len(unsorted) < 3:
		return merge(unsorted[:len(unsorted)/2], unsorted[len(unsorted)/2:])
	else:
		lsub = mergesort(unsorted[:len(unsorted)/2])
		rsub = mergesort(unsorted[len(unsorted)/2:])
	return merge(lsub, rsub)