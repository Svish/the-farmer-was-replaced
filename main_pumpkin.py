from stats import *
from watering import *
from movement import *
from planting import plantPumpkin

change_hat(Hats.Pumpkin_Hat)

initial_stats = get_initial_stats()

while True:
	goto((0,0))

	# Plant whole area
	unknown = []
	while True:
		if get_entity_type() != Entities.Pumpkin:
			unknown.append((get_pos_x(), get_pos_y()))
			harvest()
			plantPumpkin()
		if serpentine():
			break

	# Check unknowns until none left
	while len(unknown) > 0:
		next = unknown.pop(0)
		goto(next)
		if get_entity_type() == Entities.Pumpkin:
			if not can_harvest():
				unknown.append(next)
			continue

		harvest()
		if len(unknown) < 10:
			water()
		plantPumpkin()
		unknown.append(next)

	# Harvest big pumpkin
	harvest()
	print_stats(initial_stats)
