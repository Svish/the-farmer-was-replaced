def get_initial_stats():
	counts = {}
	for item in Items:
		counts[item] = num_items(item)
	return (get_time(), counts)

def print_stats(initial_stats):
	start_time, start_counts = initial_stats

	elapsed = get_time() - start_time
	if elapsed <= 0:
		return
		
	quick_print("--- Production after ", elapsed/60, "m")
	for item in start_counts:
		gained = num_items(item) - start_counts[item]
		if gained > 0 or gained < -0.1:
			quick_print(item, ": ", gained / elapsed, "/s (", gained, " total)")
