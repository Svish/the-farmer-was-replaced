from farm import *
from lib import *
from planting import *
from movement import *

def forever(action, size):
	while True:
		action(size)

world_size = get_world_size()
rect_size = world_size // 2
origins = [
	(
		(0, 0),
		farmSunflower,
	),
	(
		(0, rect_size),
		farmWood,
	),
	(
		(rect_size, rect_size),
		farmCarrot,
	),
	(
		(rect_size, 0),
		farmPumpkin,
	),
]

for origin, farm in origins:
	goto(origin)
	if num_drones() < max_drones():
		spawn_drone(forever, farm, (rect_size, rect_size))
	else:
		forever(farm, (rect_size, rect_size))
