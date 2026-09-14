from stats import *
from movement import *
from queue import *
from planting import plantSunflower

change_hat(Hats.Sunflower_Hat)

initial_stats = get_initial_stats()

while True:
	goto((0,0))

	# Plant whole area
	queue = []
	while True:
		if get_entity_type() != Entities.Sunflower:
			harvest()
			plantSunflower()

		heap_push(queue, (measure(), (get_pos_x(), get_pos_y())), 'max')

		if serpentine():
			break

	# Harvest
	next = heap_pop(queue, 'max')
	while next != None:
		goto(next[1])
		harvest()
		next = heap_pop(queue, 'max')

	# Stats
	print_stats(initial_stats)
