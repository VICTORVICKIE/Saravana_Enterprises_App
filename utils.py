from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
from os import listdir, environ
from kivy.utils import platform
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock

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

    fps_value = StringProperty()

    def start(self):
        Clock.schedule_interval(self.update_fps, self.updated_interval)

    def update_fps(self, *args):
        self.fps_value = f"FPS: {round(Clock.get_fps(),0)}"


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
            
def mobile_screen_sim(scale):
    if platform == 'win':
        density = 2.625
        dpi = 420
        width = 1080
        height = 2340
        scale = scale
        environ['KIVY_METRICS_DENSITY'] = str(density * scale)
        environ['KIVY_DPI'] = str(dpi * scale)
        Config.set('graphics', 'width', str(int(width * scale)))
        Config.set('graphics', 'height', str(int(height * scale - 25 * density)))
        Config.set('graphics', 'fullscreen', '0')
        Config.set('graphics', 'show_mousecursor', '1')