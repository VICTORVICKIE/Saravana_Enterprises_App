from os import listdir
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label

Builder.load_string(
    """
<FpsMonitor>:
    size_hint_y: None
    height: self.texture_size[1]
    text: root._fps_value
    pos_hint: {"top": 1}

    canvas.before:
		Rectangle:
			pos: self.pos
			size: self.size
			source: f"assets/images/bg/bg_toolbar.png"
"""
)


class FpsMonitor(Label):
    updated_interval = NumericProperty(0.5)
    """FPS refresh rate."""

    _fps_value = StringProperty()

    def start(self):
        Clock.schedule_interval(self.update_fps, self.updated_interval)

    def update_fps(self, *args):
        self._fps_value = f"{round(Clock.get_fps(),0)}"


def product_pic_dict(PRODUCTS_DIR):

    products_pic = {}
    for product_name in listdir(PRODUCTS_DIR):
        products_pic[product_name] = product_name.split(".")[1]

    return products_pic


def instance_in_children(parent, instance):
    for children in parent.children:
        if isinstance(children, instance):
            return True, children
        else:
            return False, children
