def merge(left, right):
	sorted = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted.append(left[i])
			i += 1
		elif left[i] > right[j]:
			sorted.append(right[j])
			j += 1
		else:
			sorted.append(left[i])
			sorted.append(right[j])
			i += 1
			j += 1
	if i < len(left):
		sorted += left[i:]
	elif j < len(right):
		sorted += right[j:]
	return sorted

def mergesort(unsorted):
	if len(unsorted) < 3:
		return merge(unsorted[:len(unsorted)/2], unsorted[len(unsorted)/2:])
	else:
		lsub = split(unsorted[:len(unsorted)/2])
		rsub = split(unsorted[len(unsorted)/2:])
	return merge(lsub, rsub)