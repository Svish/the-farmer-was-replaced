def heap_push(heap, item, mode = 'min'):
	# item is typically a tuple: (priority, data)
	heap.append(item)
	idx = len(heap) - 1

	# Sift Up
	while idx > 0:
		parent = (idx - 1) // 2
		if (mode == 'min' and heap[idx][0] < heap[parent][0]) or (mode == 'max' and heap[idx][0] > heap[parent][0]):
			heap[idx], heap[parent] = heap[parent], heap[idx]
			idx = parent
		else:
			break

def heap_pop(heap, mode = 'min'):
	if len(heap) == 0:
		return None
	if len(heap) == 1:
		return heap.pop()

	root = heap[0]
	heap[0] = heap.pop()
	idx = 0
	size = len(heap)

	# Sift Down
	while True:
		left = 2 * idx + 1
		right = 2 * idx + 2
		best = idx

		if left < size:
			if (mode == 'min' and heap[left][0] < heap[best][0]) or (mode == 'max' and heap[left][0] > heap[best][0]):
				best = left
		if right < size:
			if (mode == 'min' and heap[right][0] < heap[best][0]) or (mode == 'max' and heap[right][0] > heap[best][0]):
				best = right

		if best != idx:
			heap[idx], heap[best] = heap[best], heap[idx]
			idx = best
		else:
			break

	return root
