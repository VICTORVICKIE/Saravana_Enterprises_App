# KIVYMD IMPORTS
from ast import literal_eval
from configparser import ConfigParser
from os import listdir
# OTHER IMPORTS
from os.path import dirname, join

import kivymd
import kivymd_extensions.akivymd
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
# KIVY IMPORTS
from kivy.properties import (ColorProperty, NumericProperty, ObjectProperty,
                             StringProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex, platform
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.list import IconLeftWidget, MDList, OneLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
# KIVYMD EXTENSION IMPORTS
from kivymd_extensions.akivymd.uix.behaviors.labelanimation import \
    AKAnimationIconBehavior
from storage import *
from ultils import *


# CLASS IMPORTS
class ContentNavigationDrawer(BoxLayout):  # NavigationDrawer
    pass


class DrawerList(ThemableBehavior, MDList):  # NavigationDrawer
    pass


class AddShopDialog(BoxLayout):  # Dialog
    pass


class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout
):  # Toolbar
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = 0, 0, 0, 0


# class MDIconAnimationButton(MDIconButton, AKAnimationIconBehavior):
#     pass


class CustomCarouselItem(MDCarousel):  # Carousel
    source = StringProperty()
    name_product = StringProperty()
