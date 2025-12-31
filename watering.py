def water():
	if num_items(Items.Water) > 0:
		if get_water() < 1:
			use_item(Items.Water)