from utils import *
mobile_screen_sim('samsung')


from kivy.properties import NumericProperty, StringProperty, \
	ObjectProperty, OptionProperty, ColorProperty

from kivy.uix.screenmanager import ShaderTransition, TransitionBase, AnimationTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp


from kivymd.uix.behaviors import FakeRectangularElevationBehavior, \
	CircularRippleBehavior, RectangularRippleBehavior

from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget, \
	OneLineListItem

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import BaseFlatIconButton
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


import kivymd_extensions.akivymd.uix


from configparser import ConfigParser
from ast import literal_eval
from pathlib import Path
import sys
import os

if getattr(sys, "frozen", False):
	os.environ["BillBook"] = sys._MEIPASS
else:
	os.environ["BillBook"] = str(Path(__file__).parent)

app = MDApp.get_running_app

BILLBOOK_DIR = os.environ["BillBook"]
PRODUCTS_DIR = os.path.join(BILLBOOK_DIR,'assets','images','products')
AVATAR_DIR = os.path.join(BILLBOOK_DIR,'assets','images','avatars')
ICON_DIR = os.path.join(BILLBOOK_DIR,'assets','images','icons')
SHADERS_DIR = os.path.join(BILLBOOK_DIR,'assets','shaders')
BG_DIR = os.path.join(BILLBOOK_DIR,'assets','images','bg')

config = ConfigParser()
config.read(f"{BILLBOOK_DIR}/main.cfg")

# CONSTANTS
FIRST = config.getboolean("APP", "first_time")
AREAS = literal_eval(config.get("STORAGE", "areas"))
PRODUCTS = literal_eval(config.get("STORAGE", "products"))

# ToolBar
class Toolbar(ThemableBehavior, FakeRectangularElevationBehavior,
			  MDFloatLayout):  

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = (0, 0, 0, 0)
	def set_search_mode(self, mode=False):
		if mode:
			app().kv.ids.screens.transition = SingleSlideTransition()
			app().kv.ids.screens.transition.Direction = 'up'
			app().kv.ids.screens.current = 'search_result_screen'
			size = 0

			self.ids.search_bar.opacity = 1
			self.ids.search_bar.size_hint_y = 0.6
			self.ids.search_bar.disabled = False
			self.ids.search_bar.focus = True

			self.ids.mag.disabled = True
			self.ids.app_icon.disabled = True

			Animation(size=(size, size), opacity=0,
					  d=0.1).start(self.ids.mag)
			Animation(size=(size, size), opacity=0,
					  d=0.1).start(self.ids.title)
			Animation(size=(size, size), opacity=0,
					  d=0.1).start(self.ids.app_icon)
			Animation(opacity=1, 
					  d=0.1).start(self.ids.search_bar)
		else:
			app().kv.ids.screens.transition = SingleSlideTransition()
			app().kv.ids.screens.transition.Direction = 'down'
			app().kv.ids.screens.current = 'product_carousel_screen'
			size = dp(42)

			self.ids.search_bar.opacity = 0
			self.ids.search_bar.size_hint_y = 0.1
			self.ids.search_bar.disabled = True
			self.ids.search_bar.focus = False

			self.ids.mag.opacity = 1
			self.ids.app_icon.disabled = False
			self.ids.mag.disabled = False

			Animation(size=(size, size), opacity=1,
					  d=0.1).start(self.ids.mag)
			Animation(size=(size, size), opacity=1,
					  d=0.1).start(self.ids.title)
			Animation(size=(size, size), opacity=1,
					  d=0.1).start(self.ids.app_icon)
			Animation(opacity=0, 
					  d=0.1).start(self.ids.search_bar)

	def set_search_list(self, text="", search=False):
		text = text.lower()
		def add_search_item(name_icon,callback):

			app().kv.ids.search_results_container.ids.rv.data.append(
				{
					"viewclass": "OneLineAvatarSearchListItem",
					"source": f"{AVATAR_DIR}/{callback[0].upper()}.png",
					"text": name_icon,
					"on_release":lambda:print(callback)
				}
			)

		app().kv.ids.search_results_container.ids.rv.data = []
		for name_icon in md_icons.keys():
			if search:
				if text in name_icon:
					callback_name = name_icon
					before_text = before(name_icon,text)
					after_text = after(name_icon, text)
					name_icon = before_text + f'[b]{text}[/b]' + after_text
					add_search_item(name_icon,callback_name)
			else:
				add_search_item(name_icon)

# AppBar
class Appbar(ThemableBehavior, FakeRectangularElevationBehavior,
			 MDFloatLayout):  

	left_icon = StringProperty()
	left_text = StringProperty()

	right_icon = StringProperty()
	right_text = StringProperty()

	right_callback = ObjectProperty(lambda x: None)


	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = (1, 1, 1, 1)

	def on_right_callback(self, instance, value):
		self.icon_right_widget.bind(on_release=value)

# Iamge Icon Button
class CustomImageIconButton(CircularRippleBehavior, ButtonBehavior,
							MDLabel):  

	user_font_size = NumericProperty()
	icon = StringProperty('android')
	source = StringProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)


# Icon Flat Button
class CustomIconFlatButton(BaseFlatIconButton):

	user_font_size = NumericProperty()
	icon = StringProperty()


class OneLineAvatarSearchListItem(OneLineAvatarListItem):
	source = StringProperty()

class CustomOneLineAvatarListItem(OneLineAvatarListItem, TouchBehavior):
	def on_long_touch(self, *args):
		print("<on_long_touch> event")

# Carousel Items
class CustomCarouselItem(MDFloatLayout):

	source = StringProperty()
	product = StringProperty()
	product_pic_dict = product_pic_dict(PRODUCTS_DIR)

	def product_carousel(self):
		for product_image_name in os.listdir(PRODUCTS_DIR):
			path_to_product_image = os.path.join(PRODUCTS_DIR,
					product_image_name)

			app().kv.ids.custom_carousel.ids.car.add_widget(CustomCarouselItem(source=path_to_product_image,
																			   product=self.product_pic_dict[product_image_name]))

		app().kv.ids.custom_carousel.ids.car.children[0].children[0].ids.lab.bind(pos=app().update)


# Carousel
class CustomCarousel(MDFloatLayout, ButtonBehavior,
					 RectangularRippleBehavior, Image):

	def product_carousel_autoplay(self):
		self.product_carousel_event = \
			Clock.schedule_interval(self.product_carousel_callback, 5)

	# Carousel AutoPlay

	def product_carousel_callback(self, dt):
		app().kv.ids.custom_carousel.ids.car.load_next()


# Chart
class CustomChart(MDFloatLayout, ButtonBehavior, 
				  RectangularRippleBehavior, Image):

	items = [{'Credit': 50, 'Due': 50}]
	custom_colors = [{'Credit': '#2ebd6f', 'Due': '#ce4f47'}]

	def chart(self):
		app().kv.ids.custom_chart.ids.pie.bind(size=app().update)


class set_list:
	def set_area_list(self):
		for area in sorted(AREAS):
			source = os.path.join(AVATAR_DIR,f'{area[0]}.png')
			
			avatar = ImageLeftWidget(source=source)
			area_container_item = CustomOneLineAvatarListItem(text=f"{area}",on_release=lambda area:print(dir(area)))
			area_container_item.add_widget(avatar)
			app().kv.ids.area_container.add_widget(area_container_item)

	def set_shop_list(self):
		for shop in SHOPS:
			source = os.path.join(AVATAR_DIR,f'{shop[0]}.png')

			avatar = ImageLeftWidget(source=source)
			shop_container_item = CustomOneLineAvatarListItem(text=f"{shop}",on_release=lambda area:print(shop.text))
			shop_container_item.add_widget(avatar)
			app().kv.ids.shop_container.add_widget(shop_container_item)

			app().kv.ids.shop_container.ids.rv.data.append(
				{
					"viewclass": "OneLineAvatarSearchListItem",
					"source": f"{AVATAR_DIR}/T.png",
					"text": name_icon,
					"on_release":lambda:print(callback)
				}
			)




class CustomAddButton(MDBoxLayout, ButtonBehavior, RectangularRippleBehavior, Image):
	""" Custom Add Button """


# Transitions
class PageCurlTransition(ShaderTransition):
	Direction = OptionProperty("bt", options=["bt", "tb"])

	page_curl = open(f'{SHADERS_DIR}/page_curl.frag','r').read()

	fs = StringProperty(page_curl)

	clearcolor = ColorProperty([0, 0, 0, 0])

	def add_screen(self, screen):
		super().add_screen(screen)
		self.render_ctx["resolution"] = list(map(float, screen.size))

		aspect_ratio = screen.size[0]/screen.size[1]
		
		self.render_ctx["aspect"] = 1.0 * (aspect_ratio > 1.0) + 2.0 * (1.0 >= aspect_ratio)

		self.render_ctx["direction"] = 1.0 if self.Direction == "bt" else 2.0


class SingleSlideTransition(ShaderTransition):
	Direction = OptionProperty("up", options=["up", "down"])
	
	slide_over = open(f'{SHADERS_DIR}/slide_over.frag','r').read()

	fs = StringProperty(slide_over)

	clearcolor = ColorProperty([0, 0, 0, 0])

	def add_screen(self, screen):
		super().add_screen(screen)
		self.render_ctx["resolution"] = list(map(float, screen.size))

		self.render_ctx["direction"] = 1.0 if self.Direction == "down" else 2.0


# App
class BillBookApp(MDApp):
	
	chart_size = NumericProperty()
	chart_pos = NumericProperty()
	pad = NumericProperty()
	
	Carousel = ObjectProperty()
	AutoPlay = ObjectProperty()
	Chart = ObjectProperty()
	Search = ObjectProperty()
	Area = ObjectProperty()

	def configure(self):
		if FIRST:
			for area in AREAS:
				create_avatar(avatar_name=area,AVATAR_DIR=AVATAR_DIR)
				config['APP']['first_time'] = "False"
				with open(f"{BILLBOOK_DIR}/main.cfg",'w') as config_file:
					config.write(config_file)

	def update(self, *args):
		self.pad = \
			self.kv.ids.custom_carousel.ids.car.children[0].children[0].ids.lab.pos[0]
		self.chart_size = \
			self.kv.ids.custom_chart.ids.chart_box.size[1] - 4 \
			* self.kv.ids.custom_chart.ids.label.font_size

	def build(self):
		self.kv = Builder.load_file(f'{BILLBOOK_DIR}/main.kv')
		inspector.create_inspector(Window, self.kv)
		return self.kv
	

	def on_start(self):
		self.configure()

		self.Carousel = CustomCarouselItem()
		self.Carousel.product_carousel()

		self.AutoPlay = CustomCarousel()
		self.AutoPlay.product_carousel_autoplay()

		self.Chart = CustomChart()
		self.Chart.chart()

		self.Search = Toolbar()
		self.Search.set_search_list(text="",search=True)

		self.set = set_list()
		self.set.set_area_list()

	def on_pause(self):
		return True

	def on_resume(self):
		return True
	
	def on_stop(self):
		return True
		
	def switch_screen(self,screen,transition):
		self.kv.ids.screens.transition = PageCurlTransition(duration=1, Direction=transition)
		self.kv.ids.screens.current = screen

if __name__ == '__main__':
	BillBookApp().run()