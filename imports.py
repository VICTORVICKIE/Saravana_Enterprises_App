# KIVYMD IMPORTS
from kivymd.uix.list import MDList, IconLeftWidget, OneLineListItem
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.utils.fpsmonitor import FpsMonitor
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.card import MDSeparator
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


# KIVY IMPORTS
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp

# STORAGE IMPORTS
from storage import *
from ultils import *

# OTHER IMPORTS
from os.path import dirname, join
from configparser import ConfigParser
from ast import literal_eval
from os import listdir

# CLASS IMPORTS
class ContentNavigationDrawer(BoxLayout): #NavigationDrawer
	pass

class DrawerList(ThemableBehavior, 
				 MDList):                 #NavigationDrawer
	pass

class AddShopDialog(BoxLayout):			  #Dialog
	pass

class CustomToolbar(ThemableBehavior,
	  				RectangularElevationBehavior,
	  				MDBoxLayout):		  #Toolbar
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.md_bg_color = 0,0,0,0

class CustomCarouselItem(MDCarousel):	  #Carousel
	source = StringProperty()
	name_product = StringProperty()

