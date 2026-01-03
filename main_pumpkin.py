from watering import *
from movement import *
from planting import plantPumpkin


while True:
	goto2((0,0))
	
	# Plant whole area
	unknown = []
	while True:
		if get_entity_type() != Entities.Pumpkin:
			unknown.append((get_pos_x(), get_pos_y()))
			harvest()
			plantPumpkin()
		if cycle():
			break
	
	# Check unknowns until none left
	while len(unknown) > 0:
		next = unknown.pop(0)
		goto2(next)
		if get_entity_type() == Entities.Pumpkin:
			if not can_harvest():
				unknown.append(next)
			continue
		
		harvest()
		plantPumpkin()
		unknown.append(next)
	
	# Harvest big pumpkin
	harvest()