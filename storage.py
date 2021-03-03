Goal = {
	"Redhills": [
		{
			"Shop1": [
				{
					"product1": "price1"
				},
				{
					"product2": "price2"
				}
			]
		},
		{
			"Shop2": [
				{
					"product1": "price1"
				},
				{
					"product2": "price2"
				}
			]
		}
	],
	"Madhavaram": [
		{
			"Shop3": [
				{
					"product3": "price1"
				},
				{
					"product4": "price2"
				}
			]
		},
		{
			"Shop4": [
				{
					"product3": "price1"
				},
				{
					"product4": "price2"
				}
			]
		}
	]
}


class Storage(dict):

	self = dict()

	def __init__(self, data=None):

		self.FIRST_INDEX = 0

		if data:
			self.Dict_to_Storage(data)

	def Dict_to_Storage(self, data):

		AREAS = list(data.keys())

		for area in AREAS:
			SHOPS = data[area]
			self.add_area(area)

			for shop in SHOPS:
				shop = list(shop.keys())[self.FIRST_INDEX]
				self.add_shop(area, shop)
				index = self.get_index(area, shop)
				ITEMS = data[area][index][shop]

				for item in ITEMS:
					product = list(item.keys())[self.FIRST_INDEX]
					price = list(item.values())[self.FIRST_INDEX]
					self.add_product(area, shop, product, price)

	def get_index(self, area, shop, product=None):

		area_list = self[area]

		for search in area_list:
			search_shop = list(search.keys())[self.FIRST_INDEX]

			if search_shop == shop:
				return area_list.index(search)                  
	
	def add_area(self, area):

		if area not in self.keys():
			self[area] = []

	def add_shop(self, area, shop, balance = 0):

		area_list = self[area]
		tmp = {shop: [{"Balance":balance}]}
		area_list.append(tmp)
		self[area] = area_list

	def add_product(self, area, shop, product, price):

		index = self.get_index(area, shop)
		shop_list = self[area][index][shop]
		tmp = {product: price}
		shop_list.append(tmp)
		self[area][index][shop] = shop_list

	def remove_area(self,area):
		
		if area in self.keys():
			self.pop(area)

	def remove_shop(self,area,shop):
		
		shop_index = self.get_index(area, shop)
		self[area].pop(shop_index)

	def remove_product(self,area,shop,product):
		pass

	def change_area(self,old_area,new_area):
		self[new_area] = self.pop(old_area)

	def change_shop(self,area,old_shop,new_shop):

		shop_index = self.get_index(area, old_shop)
		self[area][shop_index][new_shop] = self[area][shop_index].pop(old_shop)

	def change_product(self,area,shop,old_product,new_product):
		pass

	def get_all_area(self):

		all_area = list(self.keys())
		return all_area

	def get_all_shop(self):

		all_area = self.get_all_area()
		all_shop = [f"{area} - {list(shop.keys())[self.FIRST_INDEX]}" 
					for area in all_area 
					for shop in self[area]
				   ]
		return all_shop


	def get_area_shop(self, area):

		area_shops = [f"{list(shop.keys())[self.FIRST_INDEX]}" 
					  for shop in self[area]
				     ]
		return area_shops


	def get_all_product(self):pass #product list file


	def get_shop_product(self, area, shop):
		
		shop_index = self.get_index(area, shop)
		shop_products = [(list(product.keys())[0],list(product.values())[0])
						 for product in self[area][shop_index][shop]
						 if list(product.keys())[0] != "Balance"
						]
		return shop_products



if __name__ == '__main__':

	a = Storage(Goal)
	
