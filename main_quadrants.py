from lib import *
from farm import *
from movement import *

def forever(action, size):
	while True:
		action(size)

world_size = get_world_size()
edge = world_size // 4
farm_size = (edge, edge*2)

origins = [
	(
		(0, 0),
		farmSunflower,
	),
	(
		(edge, 0),
		farmCarrot,
	),
	(
		(edge*2, 0),
		farmCarrot,
	),
	(
		(edge*3, 0),
		farmCarrot,
	),
	(
		(0, farm_size[1]),
		farmCarrot,
	),
	(
		(edge, farm_size[1]),
		farmCarrot,
	),
	(
		(edge*2, farm_size[1]),
		farmCarrot,
	),
	(
		(edge*3, farm_size[1]),
		farmWood,
	),
]

for origin, farm in origins:
	goto(origin)
	if num_drones() < max_drones():
		spawn_drone(forever, farm, farm_size)
	else:
		forever(farm, farm_size)
