from lib import *

# Goto next square, return true if back to 0,0
def cycle():
	if get_pos_x() == get_world_size() - 1:
		move(North)
	move(East)
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
	mid = get_world_size() / 2
	
	dx = when(x - get_pos_x() > mid, West, East)
	dy = when(y - get_pos_y() > mid, South, North)		
	while x != get_pos_x():
		move(dx)
	
	while y != get_pos_y():
		move(dy)	