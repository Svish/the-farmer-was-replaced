from movement import *
from watering import *
from planting import *

while True:
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin or can_harvest():
		harvest()
		plantRandom()
	water()
	cycle()
	
