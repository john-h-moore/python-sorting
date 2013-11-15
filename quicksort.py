'''
TO DO:
- make quicksort accept 0 and -1 as default left and right
- create alternate choosePivot methods (random, first, mid, etc)
'''
import random

# Random pivot
def chooseRandPivot(array):
	return random.choice(array)

# Median-of-three pivot choosing method
# array = array to be sorted
# left = left index of array (default: 0)
# right = right index of array (default: last element)
def choosePivot(array, left=0, right=-1):
	first = array[left]
	middle = array[len(array[left:right])/2]
	last = array[right]
	if first <= middle <= last:
		return array.index(middle)
	elif middle <= first <= last:
		return left
	else:
		return right

# Partition - used for in-place quicksort
# array = array to be sorted
# left = left index of array
# right = right index of array
# pivotIndex = pivot index (chosen with choosePivot, called from quicksort)
def partition(array, left, right, pivotIndex):
	pivot = array[pivotIndex]
	array[pivotIndex], array[right] = array[right], array[pivotIndex]
	boundary = left # index < boundary --> item < pivot (and vice versa)
	for element in range(left, right):
		if array[element] <= pivot:
			array[element], array[boundary] = array[boundary], array[element]
			boundary +=1
	array[boundary], array[right] = array[right], array[boundary]
	return boundary

# Returns sorted copy of original list; use in case you need the original list
def qsort(unsorted):
	quicksorted = []
	if len(unsorted) < 2:
		quicksorted += unsorted
	else:
		pivot = unsorted[choosePivot(unsorted)]
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
		quicksorted += qsort(lt)
		quicksorted.append(pivot)
		quicksorted += qsort(gt)
	return quicksorted

# In-place quicksort
# array = array to be sorted
# left = left index of array
# right = right index of array
def quicksort(array, left, right):
	if left < right:
		p = choosePivot(array, left, right)
		pNew = partition(array, left, right, p)
		quicksort(array, left, pNew-1)
		quicksort(array, pNew+1, right)
