from movement import *
from planting import plantWood

change_hat(Hats.Tree_Hat)

while True:
	if can_harvest():
		harvest()
	plantWood()
	cycle()