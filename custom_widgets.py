from kivymd.uix.card import MDCard
from kivymd.app import MDApp

from kivy.properties import NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder

from kivymd.uix.behaviors import FakeRectangularElevationBehavior, CircularRippleBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.button import BaseFlatIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel


class Toolbar(ThemableBehavior, FakeRectangularElevationBehavior, MDFloatLayout):	# ToolBar
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = 0, 0, 0, 0



class CarouselItem(MDCarousel):														# Carousel
	source = StringProperty()
	name_product = StringProperty()

class CarouselContainer(MDFloatLayout,ButtonBehavior,RectangularRippleBehavior,Image):# Carousel Container
	pass

class ChartContainer(MDFloatLayout,ButtonBehavior,RectangularRippleBehavior,Image):	# Chart
	pass


class CustomImageIconButton(CircularRippleBehavior, ButtonBehavior, MDLabel):		# Iamge Icon Button
	user_font_size = NumericProperty()
	icon = StringProperty("android")
	source = StringProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Appbar(ThemableBehavior, FakeRectangularElevationBehavior, MDFloatLayout):	# AppBar
	position = StringProperty('Top')
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = 1, 1, 1, 1

class CustomIconFlatButton(BaseFlatIconButton):
	user_font_size = NumericProperty()
	icon = StringProperty()


Builder.load_file("custom_widgets.kv")