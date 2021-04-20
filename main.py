from utils import *
mobile_screen_sim('samsung')


from kivy.properties import NumericProperty, StringProperty, \
	ObjectProperty

from kivy.uix.screenmanager import ShaderTransition
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

PRODUCTS_DIR = os.path.join(os.environ['BillBook'],'assets','images','products')
AVATAR_DIR = os.path.join(os.environ['BillBook'],'assets','images','avatars')
ICON_DIR = os.path.join(os.environ['BillBook'],'assets','images','icons')
BG_DIR = os.path.join(os.environ['BillBook'],'assets','images','bg')

config = ConfigParser()
config.read("main.cfg")

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
			app().kv.ids.screens.transition.direction = 'up'
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
			
			app().kv.ids.screens.transition.direction = 'down'
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
					"source": "assets/images/avatars/T.png",
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


class Area:
	def set_area_list(self):
		for area in sorted(AREAS):
			source = os.path.join(AVATAR_DIR,f'{area[0]}.png')
			
			avatar = ImageLeftWidget(source=source)
			area_container_item = OneLineAvatarListItem(text=f"{area}",on_release=lambda area:print(area.text))
			area_container_item.add_widget(avatar)
			app().kv.ids.area_container.add_widget(area_container_item)

class Shop:
	def set_shop_list(self):
		for shop in SHOPS:
			source = os.path.join(AVATAR_DIR,f'{shop[0]}.png')

			avatar = ImageLeftWidget(source=source)
			shop_container_item = OneLineAvatarListItem(text=f"{shop}",on_release=lambda area:print(shop.text))
			shop_container_item.add_widget(avatar)
			app().kv.ids.shop_container.add_widget(shop_container_item)


class CustomAddButton(MDBoxLayout, ButtonBehavior, RectangularRippleBehavior, Image):
	""" Custom Add Button """


class WriteTransition(ShaderTransition):
	WRITE_TRANSITION_FS = '''$HEADER$
	uniform float t;
	uniform sampler2D tex_in;
	uniform sampler2D tex_out;

	void main(void) {
		vec4 cin = texture2D(tex_in, tex_coord0);
		vec4 cout = texture2D(tex_out, tex_coord0);
		gl_FragColor = mix(cout, cin, clamp((-1.5 - 1.5*tex_coord0.y + 2.5*t),
			0.0, 1.0));
	}
	'''
	fs = StringProperty(WRITE_TRANSITION_FS)




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

	# def configure(self):
	# 	if FIRST:
	# 		for area in AREAS:
	# 			create_avatar(avatar_name=area,AVATAR_DIR=AVATAR_DIR)
	# 			config['APP']['first_time'] = "False"
	# 			with open('main.cfg','w') as config_file:
	# 				config.write(config_file)

	def update(self, *args):
		self.pad = \
			self.kv.ids.custom_carousel.ids.car.children[0].children[0].ids.lab.pos[0]
		self.chart_size = \
			self.kv.ids.custom_chart.ids.chart_box.size[1] - 4 \
			* self.kv.ids.custom_chart.ids.label.font_size

	def build(self):
		self.kv = Builder.load_file('main.kv')
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

		self.Area = Area()
		self.Area.set_area_list()

	def on_pause(self):
		return True

	def on_resume(self):
		return True
	
	def on_stop(self):
		return True
		
	def switch_screen(self,from_screen, to_screen):
		if from_screen == 'product_carousel_screen' and to_screen == 'area_screen':
			self.kv.ids.screens.transition = WriteTransition()
			self.kv.ids.screens.current = to_screen


if __name__ == '__main__':
	BillBookApp().run()