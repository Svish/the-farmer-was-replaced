def plantHay():
	if get_ground_type() != Grounds.Grassland:
		till()

def plantWood():
	x = get_pos_x()
	y = get_pos_y()
	if (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0):
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def plantCarrot():
	if get_ground_type() != Grounds.Soil:
		till()
	if not plant(Entities.Carrot):
		plantRandom([plantHay, plantWood])

def plantPumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	if not plant(Entities.Pumpkin):
		plantCarrot()

def plantRandom(options = [
	plantHay,
	plantHay,
	plantWood,
	plantCarrot,
	plantCarrot,
	plantPumpkin,
]):
	option = random() * len(options) // 1
	options[option]()

	