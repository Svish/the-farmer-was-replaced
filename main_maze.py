from movement import goto
from maze import *

change_hat(Hats.Gold_Hat)

while True:
	create_maze()
	find_treasure_naive()
	harvest()
