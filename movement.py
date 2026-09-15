from lib import *



# Goto without wrap
def goto_simple(xy):
	x, y = xy

	while get_pos_x() > x:
		move(West)
	while get_pos_x() < x:
		move(East)
	while get_pos_y() > y:
		move(South)
	while get_pos_y() < y:
		move(North)



# Goto with wrap
def goto(target):
	world_size = get_world_size()
	mid = world_size / 2

	x, y = target

	dx = when((x - get_pos_x()) % world_size > mid, West, East)
	dy = when((y - get_pos_y()) % world_size > mid, South, North)

	while x != get_pos_x():
		move(dx)

	while y != get_pos_y():
		move(dy)



# Cycle through rows, left to right, bottom to top
def rows(action = None, origin = (0, 0), size = (get_world_size(), get_world_size()), return_to_origin = True):
	origin_x, origin_y = origin
	width, height = size
	x, y = get_pos()
	is_last = x == origin_x + width - 1 and y == origin_y + height - 1

	if action:
		action()

	if is_last:
		if return_to_origin:
			goto(origin)
		return False

	if x == origin_x + width - 1:
		move(North)
		while get_pos_x() > origin_x:
			move(West)
	else:
		move(East)
	return True



# Cycle through columns, bottom to top, left to right
def columns(action = None, origin = (0, 0), size = (get_world_size(), get_world_size()), return_to_origin = True):
	origin_x, origin_y = origin
	width, height = size
	x, y = get_pos()
	is_last = x == origin_x + width - 1 and y == origin_y + height - 1

	if action:
		action()

	if is_last:
		if return_to_origin:
			goto(origin)
		return False

	if y == origin_y + height - 1:
		move(East)
		while get_pos_y() > origin_y:
			move(South)
	else:
		move(North)
	return True



# Cycle through rows in a serpentine pattern
def serpentine_rows(action = None, origin = (0, 0), size = (get_world_size(), get_world_size()), return_to_origin = True):
	origin_x, origin_y = origin
	width, height = size
	x, y = get_pos()
	last_x = when(height % 2 == 1, origin_x + width - 1, origin_x)
	last_y = origin_y + height - 1
	is_last = x == last_x and y == last_y

	if action:
		action()

	if is_last:
		if return_to_origin:
			goto(origin)
		return False

	if (y - origin_y) % 2 == 0:
		if x == origin_x + width - 1:
			move(North)
		else:
			move(East)
	else:
		if x == origin_x:
			move(North)
		else:
			move(West)
	return True



# Cycle through columns in a serpentine pattern
def serpentine_columns(action = None, origin = (0, 0), size = (get_world_size(), get_world_size()), return_to_origin = True):
	origin_x, origin_y = origin
	width, height = size
	x, y = get_pos()
	last_x = origin_x + width - 1
	last_y = when(width % 2 == 1, origin_y + height - 1, origin_y)
	is_last = x == last_x and y == last_y

	if action:
		action()

	if is_last:
		if return_to_origin:
			goto(origin)
		return False

	if (x - origin_x) % 2 == 0:
		if y == origin_y + height - 1:
			move(East)
		else:
			move(North)
	else:
		if y == origin_y:
			move(East)
		else:
			move(South)
	return True



# Cycle through outward growing rectangles in a serpentine pattern
def serpentine_rectangles(action = None, origin = (0, 0), size = (get_world_size(), get_world_size()), return_to_origin = True):
	origin_x, origin_y = origin
	width, height = size
	x, y = get_pos()
	dx = x - origin_x
	dy = y - origin_y
	last_dx, last_dy = serpentine_rectangles_last(width, height)
	is_last = dx == last_dx and dy == last_dy

	if action:
		action()

	if is_last:
		if return_to_origin:
			goto(origin)
		return False

	next_dx, next_dy = serpentine_rectangles_next(dx, dy, width, height)
	goto_simple((origin_x + next_dx, origin_y + next_dy))
	return True

# First tile of the ring at distance k from the origin corner
def serpentine_rectangles_start(k, width, height):
	if k % 2 == 0:
		if k < height:
			return (0, k)
		return (k, height - 1)
	if k < width:
		return (k, 0)
	return (width - 1, k)

# Last tile of the outermost ring
def serpentine_rectangles_last(width, height):
	k = max(width, height) - 1
	if k % 2 == 0:
		if k < width:
			return (k, 0)
		return (width - 1, k)
	if k < height:
		return (0, k)
	return (k, height - 1)

# Tile following (dx, dy), relative to the origin
def serpentine_rectangles_next(dx, dy, width, height):
	k = max(dx, dy)
	if k % 2 == 0:
		if dy == k:
			# West to East along the northern edge
			if dx < min(k, width - 1):
				return (dx + 1, dy)
			if k > 0 and k < width:
				return (k, k - 1)
		else:
			# North to South along the eastern edge
			if dy > 0:
				return (k, dy - 1)
	else:
		if dx == k:
			# South to North along the eastern edge
			if dy < min(k, height - 1):
				return (dx, dy + 1)
			if k < height:
				return (k - 1, k)
		else:
			# East to West along the northern edge
			if dx > 0:
				return (dx - 1, k)
	return serpentine_rectangles_start(k + 1, width, height)
