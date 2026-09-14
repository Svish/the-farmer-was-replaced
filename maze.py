def create_maze(size = get_world_size()):
	if get_entity_type() != Entities.Hedge:
		if get_entity_type() != Entities.Treasure:
			if can_harvest():
				harvest()
			plant(Entities.Bush)
		substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
	return measure()

def find_treasure_naive():
	directions = [North, East, South, West]
	heading = 0
	while get_entity_type() != Entities.Treasure:
		while not move(directions[heading]):
			heading = (heading - 1) % 4

		heading = (heading + 1) % 4
	return True
