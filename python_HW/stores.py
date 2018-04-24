

def create_dict(file_name):
    stores = {}
    with open(file_name, encoding='utf-8') as fd:
        for line in fd:
            store_name, shelf_number, product = line.split()
            shelves = stores.setdefault(store_name, {})
            shelf = shelves.setdefault(shelf_number,set())
            shelf.add(product)
    return stores

def find_product(stores, product_name):
	for store, shelves in stores.items():
		for shelf, products in shelves.items():
			if product_name in products:
				return store, shelf
	return None

if __name__ == '__main__':
	stores = create_dict("table.csv")
	print(find_product(stores, "ПЕРФОФАЙЛЫ"))
	print(find_product(stores, "ПАПКА"))
