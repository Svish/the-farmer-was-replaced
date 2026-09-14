from stats import *
from movement import *
from watering import *
from planting import *

change_hat(Hats.Brown_Hat)

coord = (3, 3)
items = [
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Hay,
	Items.Wood,
	Items.Carrot,
	Items.Carrot,
	Items.Carrot,
	Items.Carrot,
	Items.Carrot,
	Items.Carrot,
	Items.Carrot,
]
fertilize = [
	Entities.Tree,
	Entities.Carrot,
]

stats_interval = 30
next_stats = get_time() + stats_interval
initial_stats = get_initial_stats()


goto(coord)


neighbors = [
	(coord[0], coord[1] + 1),
	(coord[0] + 1, coord[1]),
	(coord[0], coord[1] - 1),
	(coord[0] - 1, coord[1]),
]
companions = {}

while True:
	planted = plantRandom(items)
	water()

	if planted == Entities.Tree:
		for n in neighbors:
			goto(n)
			if get_entity_type() == Entities.Tree:
				harvest()
				companions[n] = get_entity_type()
		goto(coord)

	companion = get_companion()
	if companion != None:
		c_entity, c_coords = companion
		if not c_coords in companions or companions[c_coords] != c_entity:
			goto(c_coords)
			if can_harvest():
				harvest()
			ground_type = get_ground_type()
			if (c_entity == Entities.Carrot and ground_type != Grounds.Soil) or (c_entity != Entities.Carrot and ground_type != Grounds.Grassland):
				till()
			plant(c_entity)
			companions[c_coords] = c_entity
			goto(coord)

	fertilized = False
	while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
		if not fertilized and planted in fertilize:
			fertilized = True
			use_item(Items.Fertilizer)
	harvest()

	if get_time() >= next_stats:
		print_stats(initial_stats)
		next_stats = next_stats + stats_interval
