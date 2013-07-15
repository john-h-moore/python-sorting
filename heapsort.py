import heapq

def heapsort(unsorted):
	unsorted_input = unsorted[:]
	heapq.heapify(unsorted)
	heapsorted = []
	for i in range(0, len(unsorted_input)):
		z = heapq.heappop(unsorted_input)
		heapq.heappush(heapsorted, z)
	return heapsorted