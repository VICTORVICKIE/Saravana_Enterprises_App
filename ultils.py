from os import listdir

def product_pic_dict(PRODUCTS_DIR):

		products_pic = {}
		for product_name in listdir(PRODUCTS_DIR):
			products_pic[product_name] = product_name.split(".")[1]

		return products_pic