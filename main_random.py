from stats import *
from movement import *
from watering import *
from planting import plantRandom

change_hat(Hats.Brown_Hat)

items = [
	Items.Hay,
	Items.Hay,
	Items.Wood,
	Items.Carrot,
	Items.Carrot,
	Items.Pumpkin,
]

stats_interval = 30
next_stats = get_time() + stats_interval
initial_stats = get_initial_stats()

while True:
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin or can_harvest():
		harvest()
		plantRandom(items)
	serpentine_rows()

	if get_time() >= next_stats:
		print_stats(initial_stats)
		next_stats = next_stats + stats_interval
