from utils import mobile_screen_sim, product_pic_dict
mobile_screen_sim(0.25)

# kivy
from kivy.properties import ColorProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp

# kivymd
from kivymd.uix.behaviors import FakeRectangularElevationBehavior, CircularRippleBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import BaseFlatIconButton
from kivymd.uix.carousel import MDCarousel
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.app import MDApp

from kivymd_extensions.akivymd.uix.piechart import AKPieChart

# Paths
from pathlib import Path
import sys
import os

if getattr(sys, "frozen", False):
	os.environ["SE_BILL_BOOK"] = sys._MEIPASS
else:
	os.environ["SE_BILL_BOOK"] = str(Path(__file__).parent)

PRODUCTS_DIR = os.path.join(os.environ["SE_BILL_BOOK"],'assets','images','Products')

class Toolbar(ThemableBehavior, FakeRectangularElevationBehavior, MDFloatLayout):  # Toolbar
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = 0, 0, 0, 0

class Appbar(ThemableBehavior, FakeRectangularElevationBehavior, MDFloatLayout):  # Toolbar
	position = StringProperty('Top')
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = 1, 1, 1, 1

class CarouselItem(MDCarousel):  # Carousel
	source = StringProperty()
	name_product = StringProperty()

class ChartContainer(MDFloatLayout,ButtonBehavior,RectangularRippleBehavior,Image):
	pass
class CarouselContainer(MDFloatLayout):
	pass

class CustomImageIconButton(CircularRippleBehavior, ButtonBehavior, MDLabel):
	user_font_size = NumericProperty()
	icon = StringProperty("android")
	source = StringProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
class CustomIconFlatButton(BaseFlatIconButton):
	user_font_size = NumericProperty()
	icon = StringProperty()
class BillBook(MDApp):

	product_pic_dict = product_pic_dict(PRODUCTS_DIR)
	items = [{"Credit": 50, "Overdue": 50}]
	custom_colors = [{"Credit": '#45a63c',"Overdue":'#db3d43'}]
	shop_dialog = ObjectProperty(None)
	shop_balance = NumericProperty()
	shop_name = StringProperty()
	source = StringProperty()

	gray = get_color_from_hex("000000")
	gray[3] = 0.12
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.kv = Builder.load_file("main.kv")

	def product_carousel(self, *args):
		for product_image_name in os.listdir(PRODUCTS_DIR):
			path_to_product_image = os.path.join(PRODUCTS_DIR, product_image_name)

			self.kv.ids.carousel_container.ids.product_carousel.add_widget(
				CarouselItem(
					source=path_to_product_image,
					name_product=self.product_pic_dict[product_image_name],
				)
			)

	# Carousel AutoPlay Scheduler
	def product_carousel_autoplay(self):
		self.product_carousel_event = Clock.schedule_interval(
			self.product_carousel_callback, 5
		)

	# Carousel AutoPlay
	def product_carousel_callback(self, dt):
		self.kv.ids.carousel_container.ids.product_carousel.load_next()
	
	def sales_chart(self):


		self.piechart = AKPieChart(
			items=self.items,
			pos_hint={"center_x": .5},
			size_hint=[None, None],
			size=(dp(180), dp(180)),
			color_mode='Custom',
			custom_colors = self.custom_colors
		)
		self.kv.ids.chart_container.ids.chart_box.add_widget(self.piechart)
		
	def on_pause(self):
			return True

	def on_resume(self):
		return True

	def build(self):
		return self.kv

	def on_start(self):
		self.product_carousel()
		self.product_carousel_autoplay()
		self.sales_chart()

if __name__ == "__main__":

	app = BillBook()
	app.run()
