world_size = get_world_size()

def when(condition, true, false = None):
	if condition:
		return true
	return false

def toroidal_distance(x1, y1, x2, y2):
	dx = abs(x1 - x2)
	dx = min(dx, world_size - dx)
	dy = abs(y1 - y2)
	dy = min(dy, world_size - dy)
	return dx + dy
