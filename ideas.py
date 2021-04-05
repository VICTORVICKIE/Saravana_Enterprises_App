# from kivy.app import App
# from kivy.clock import mainthread
# from kivy.lang import Builder
# from kivy.uix.floatlayout import FloatLayout
# from time import sleep
# from threading import Thread
# from kivy.properties import ColorProperty

# KV = """
# FloatLayout


# <ColorfulLayout>
#     canvas.before:
#         Color:
#             rgba:
#                 self.color
#         Rectangle:
#             size: self.size
#             pos: self.pos
# """


# class ColorfulLayout(FloatLayout):
#     color = ColorProperty([1, 1, 1, 1])


# class ExampleApp(App):
#     some_widget = None

#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):

#         self.some_widget = ColorfulLayout(size=[100, 100], center=self.root.center)
#         self.root.add_widget(self.some_widget)
#         Thread(target=self.calculate, daemon=True).start()

#     def calculate(self):
#         for _ in range(1):
#             sleep(1)

#         self.change()

#     @mainthread
#     def change(self):
#         self.root.remove_widget(self.some_widget)
#         self.some_widget = ColorfulLayout(color=[.5, .1, .3, 1], size=[200, 200], center=self.root.center)
#         self.root.add_widget(self.some_widget)


# ExampleApp().run()

# from kivy.core.window import Window
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.modules import inspector

# class Demo(App):
#     def build(self):
#         button = Button(text="Test")
#         inspector.create_inspector(Window, button)
#         return button

# Demo().run()

# from kivy.lang import Builder
# from kivy.properties import ListProperty
# from kivy.app import App

# from random import gauss

# KV = '''
# #:import Animation kivy.animation.Animation
# #:import chain itertools.chain
# #:import gauss random.gauss
# #:import Clock kivy.clock.Clock
# <Graph@Widget>:
#     max: 100
#     values: []
#     canvas:
#         Line:
#             points:
#                 list(chain(*
#                 [[
#                 self.x + x * self.width / len(self.values),
#                 self.y + y * self.height / self.max
#                 ] for x, y in enumerate(self.values)])) if self.values else []
# GridLayout:
#     cols: 2
#     Graph:
#         max: 100
#         values: app.values
#     Button:
#         text: 'push me'
#         size_hint_x: None
#         on_press:
#             Animation(
#             values=[gauss(50, 10) for x in enumerate(app.values)],
#             t='out_quad').start(app)
#     Graph:
#         max: 1
#         values: app.running_values
#     ToggleButton:
#         text: 'push me'
#         size_hint_x: None
#         on_state:
#             if self.state == 'down': Clock.schedule_interval(app.add_running_values, 0)
#             else: Clock.unschedule(app.add_running_values)
# '''  # noqa


# class Graph(App):
#     values = ListProperty([x for x in range(100)])
#     running_values = ListProperty([])

#     def build(self):
#         return Builder.load_string(KV)

#     def add_running_values(self, dt):
#         self.running_values.append(gauss(.5, .1))
#         self.running_values = self.running_values[-100:]

# if __name__ == '__main__':
#     Graph().run()
# <CustomImageIconButton>:
    
#     font_style: "Icon"
#     text: u"{}".format(md_icons[self.icon]) if self.icon in md_icons else ""
    
#     font_size: root.user_font_size \
#         if root.user_font_size \
#         else self.font_size
    
#     halign:'center'
#     size_hint: None, None
#     size: (dp(56), dp(56))
#     pos_hint: {"center_x": .5, "center_y": .5}
#     canvas.before:
#         Ellipse:
#             source: self.source
#             pos: self.pos
#             size: self.size
# Screen:
#     CustomImageIconButton:
#         icon:'minus'
#         source:f"assets/images/bg/bg_toolbar.png"
#         on_release:print(self.source)
#     MDFloatingActionButton:
#         icon:'plus'
#         pos_hint: {"center_x": .5, "center_y": .6}

# <CustomIconFlatButton>
# 	width: label_txt.texture_size[0]
# 	height: 24 + 15
#     padding: (dp(12), dp(12))
#     markup: False
#     FloatLayout:
#         id: item_container
#         spacing:dp(10)
#         MDIcon:
#             id: label_txt_icon
#             icon: root.icon
#             size_hint_x: None
#             text_size: (None, root.height)
#             height: self.texture_size[1]
#             theme_text_color: 'Custom'
#             text_color:
#                 (root.theme_cls.primary_color if not root.text_color else root.text_color) \
#                 if not root.disabled else root.theme_cls.disabled_hint_text_color
#             valign: 'middle'
#             halign: 'center'
#             opposite_colors: root.opposite_colors
#             pos: [self.pos[0], self.pos[1]]
#             font_size: dp(24)
#             pos_hint: {'center_x': .5, 'center_y': .8}

#         MDLabel:
#             id: label_txt
#             text: root.text
#             font_style: 'Caption'
#             size_hint_x: None
#             text_size: (None, root.height)
#             height: self.texture_size[1]
#             theme_text_color: 'Custom'
#             # text_color: root._text_color_normal
#             valign: 'bottom'
#             halign: 'center'
#             opposite_colors: root.opposite_colors
#             # font_size: root.label_txt_font_size
#             pos_hint: {'center_x': .5, 'center_y': .5}
#             markup: root.markup

# MDScreen:
# 	CustomIconFlatButton:
# 		pos_hint:{'center_x':.5,'center_y':.5}
# 		icon:'cart'
# 		markup:True
# 		text:'[b]ORDERS[b]'
# 		on_release:print(self.height)

# from kivy.lang import Builder
# from kivy.uix.behaviors import ButtonBehavior
# from kivymd.app import MDApp
# from kivymd.uix.label import MDIcon
# from kivymd.uix.behaviors import RectangularRippleBehavior
# from kivy.properties import NumericProperty, StringProperty
# from kivymd.uix.button import BaseFlatIconButton

# KV='''
# #:import md_icons kivymd.icon_definitions.md_icons

# '''




# class CustomIconFlatButton(BaseFlatIconButton):
# 	user_font_size = NumericProperty()
# 	l_icon = StringProperty("android")
# 	r_icon = StringProperty("")
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)


# class Example(MDApp):
# 	def build(self):
# 		return Builder.load_string(KV)


# Example().run()
