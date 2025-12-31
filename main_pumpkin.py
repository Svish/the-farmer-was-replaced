from watering import *
from movement import *

def cycle_2():
	cycle()
	return get_pos_x() == 0 and get_pos_y() == 0

goal = get_world_size()**2
current = 0

while True:
	if get_entity_type() != Entities.Pumpkin:
		if can_harvest():
			harvest()
			
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		water()
	elif can_harvest():
		current += 1
	else:
		water()
	
	if cycle_2():
		if current == goal and can_harvest():
			harvest()
		current = 0