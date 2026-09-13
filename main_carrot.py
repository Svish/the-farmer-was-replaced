from movement import *
from planting import plantCarrot

change_hat(Hats.Carrot_Hat)

while True:
	if can_harvest():
		harvest()
	plantCarrot()
	cycle()
