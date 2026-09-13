from movement import *
from watering import *
from planting import plantRandom

change_hat(Hats.Brown_Hat)

while True:
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin or can_harvest():
		harvest()
		plantRandom()
	cycle()
	
