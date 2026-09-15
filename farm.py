from lib import *
from movement import *
from planting import *
from maze import *



# Farms one cycle of hay of given size, starting from the current position
def farmHay(size):
	change_hat(Hats.Straw_Hat)

	def action():
		harvest_when_ready()
		plantHay()

	origin = get_pos()
	while serpentine_rows(action, origin, size):
		continue



# Farms one cycle of wood of given size, starting from the current position
def farmWood(size):
	change_hat(Hats.Tree_Hat)

	def action():
		harvest_when_ready()
		plantWood()
		water()

	origin = get_pos()
	while serpentine_rows(action, origin, size):
		continue



# Farms one cycle of carrot of given size, starting from the current position
def farmCarrot(size):
	change_hat(Hats.Carrot_Hat)

	def action():
		harvest_when_ready()
		plantCarrot()
		water()

	origin = get_pos()
	while serpentine_rows(action, origin, size):
		continue



# Farms one cycle of pumpkin, starting from the current position
def farmPumpkin(size):
	change_hat(Hats.Pumpkin_Hat)

	# Plant whole area
	unknown = []
	origin = get_pos()
	def action():
		if get_entity_type() != Entities.Pumpkin:
			harvest()
			plantPumpkin()
			unknown.append((get_pos_x(), get_pos_y()))
	while serpentine_rectangles(action, origin, size, False):
		continue

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
	goto(origin)



# Farms one cycle of sunflower of given size, starting from the current position
def farmSunflower(size):
	change_hat(Hats.Sunflower_Hat)

	queue = []
	queue_mode = 'max'
	origin = get_pos()
	def action():
		if get_entity_type() != Entities.Sunflower:
			harvest()
			plantSunflower()
		heap_push(queue, (measure(), (get_pos_x(), get_pos_y())), queue_mode)

	while serpentine_rows(action, origin, size):
		continue

	next = heap_pop(queue, queue_mode)
	while next != None:
		goto(next[1])
		harvest()
		next = heap_pop(queue, queue_mode)
	goto(origin)
