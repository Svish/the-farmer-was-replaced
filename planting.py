def water():
	if num_items(Items.Water) > 0:
		if get_water() < 1:
			return use_item(Items.Water)
	return False


def harvest_when_ready():
	while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
		continue
	return harvest()


def plantHay():
	if get_ground_type() != Grounds.Grassland:
		till()
	return Entities.Grass


def plantWood():
	x = get_pos_x()
	y = get_pos_y()
	if (x + y) % 2 == 0:
		plant(Entities.Tree)
		return Entities.Tree
	else:
		plant(Entities.Bush)
		return Entities.Bush


def plantCarrot():
	if get_ground_type() != Grounds.Soil:
		till()
	if not plant(Entities.Carrot):
		return plantRandom([Items.Hay, Items.Wood])
	return Entities.Carrot


def plantPumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Carrot) < get_cost(Entities.Pumpkin)[Items.Carrot] or not plant(Entities.Pumpkin):
		plantCarrot()
		return Entities.Carrot
	return Entities.Pumpkin


def plantSunflower():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	return Entities.Sunflower

def plantRandom(options):
	option = random() * len(options) // 1
	return plantMap[options[option]]()

plantMap = {
	Items.Hay: plantHay,
	Items.Wood: plantWood,
	Items.Carrot: plantCarrot,
	Items.Pumpkin: plantPumpkin,
	Items.Power: plantSunflower,
}
