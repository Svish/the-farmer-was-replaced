from lib import *
from farm import *
from movement import *

def forever(action, size):
	while True:
		action(size)

world_size = get_world_size()
edge = world_size // 4
farm_size = (edge*2, edge)

farm = [
	farmSunflower,
	farmWood,
	farmHay,
	farmHay,
	farmCarrot,
	farmCarrot,
	farmCarrot,
	farmCarrot,
]

origins = [
	(0, 0),
	(0, edge),
	(0, edge*2),
	(0, edge*3),
	(farm_size[0], 0),
	(farm_size[0], edge),
	(farm_size[0], edge*2),
	(farm_size[0], edge*3),
]

for i in range(len(origins)):
	f = farm[i % len(farm)]
	o = origins[i]
	goto(o)
	if num_drones() < max_drones():
		spawn_drone(forever, f, farm_size)
	else:
		forever(f, farm_size)
