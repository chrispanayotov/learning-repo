apartments_dict = {}

data_input = input()

while data_input != 'collectApartments':
	neighborhood, blocks_list = data_input.split(' -> ')
	blocks = blocks_list.split(',')

	if neighborhood not in apartments_dict.keys():
		apartments_dict[neighborhood] = {}
		for block in blocks:
			apartments_dict[neighborhood][block] = {'available_apartments': 0, 'price_for_apartment': None}
	else:
		for block in blocks:
			if not block in apartments_dict[neighborhood].keys():
				apartments_dict[neighborhood][block] = {'available_apartments': 0, 'price_for_apartment': None}

	data_input = input()


data_input = input()

while data_input != 'report':
	x, y = data_input.split(' -> ')
	neighborhood, block = x.split('&')
	available_apartments, price  = y.split('|')

	if neighborhood in apartments_dict.keys():
		if block in apartments_dict[neighborhood].keys():
			apartments_dict[neighborhood][block]['available_apartments'] = available_apartments
			apartments_dict[neighborhood][block]['price_for_apartment'] = price
	
	data_input = input()


sorted_apartments = sorted(apartments_dict.keys())
for neighborhood in sorted_apartments:
	print(f"Neighborhood: {neighborhood}")
	sorted_blocks = sorted(apartments_dict[neighborhood].keys())
	for block_num in sorted_blocks:
		print(f"* Block number: {block_num} -> {apartments_dict[neighborhood][block_num]['available_apartments']} apartments for sale. Price for one: {apartments_dict[neighborhood][block_num]['price_for_apartment']}")