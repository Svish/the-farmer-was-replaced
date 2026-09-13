from lib import *

world_size = get_world_size()
mid = world_size / 2

# Goto next square, return true if back to 0,0
def cycle():
	if get_pos_x() == world_size - 1:
		move(North)
	move(East)
	return get_pos_x() == 0 and get_pos_y() == 0

# Goto next square, serpentine style
def serpentine():
	x, y = get_pos_x(), get_pos_y()
	if get_pos_y() % 2 == 0:
		if get_pos_x() == world_size - 1:
			move(North)
		else:
			move(East)
	else:
		if get_pos_x() == 0:
			move(North)
		else:
			move(West)
	return get_pos_x() == 0 and get_pos_y() == 0

# Goto without wrap
def goto(xy):
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
def goto2(xy):
	x, y = xy

	dx = when((x - get_pos_x()) % world_size > mid, West, East)
	dy = when((y - get_pos_y()) % world_size > mid, South, North)

	while x != get_pos_x():
		move(dx)

	while y != get_pos_y():
		move(dy)
