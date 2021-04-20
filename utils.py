from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
from os import listdir, environ, scandir
from os.path import join
from kivy.utils import platform
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from avatar_generator import Avatar

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

def mobile_data(mobile):
        if mobile == 'OP':
            return 2.625, 420, 1080, 2340, 0.25
        elif mobile == 'samsung':
            return 1.75, 280, 720, 1340, 0.5

def mobile_screen_sim(mobile):
    

    if platform == 'win':
        density, dpi, width, height, scale = mobile_data(mobile)
        environ['KIVY_METRICS_DENSITY'] = str(density * scale)
        environ['KIVY_DPI'] = str(dpi * scale)
        Config.set('graphics', 'width', str(int(width * scale)))
        Config.set('graphics', 'height', str(int(height * scale - 25 * density)))
        Config.set('graphics', 'fullscreen', '0')
        Config.set('graphics', 'show_mousecursor', '1')


def create_avatar(avatar_name,AVATAR_DIR=None):
    initial = avatar_name[0].upper()

    if any(scandir(AVATAR_DIR)):
        for avatar in listdir(AVATAR_DIR):
            if initial in avatar.split('.')[0]:
                return 'Exist'
            else:
                avatar = Avatar.generate(128, avatar_name, "PNG")

                with open(join(AVATAR_DIR,f"{initial}.png"),'wb') as f:
                    data = f.write(avatar)
    else:
        avatar = Avatar.generate(128, avatar_name, "PNG")
        with open(join(AVATAR_DIR,f"{initial}.png"),'wb') as f:
            data = f.write(avatar)

def before(value, a):
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def after(value, a):
    pos_a = value.find(a)
    if pos_a == -1: return ""
    adjusted_pos_a = pos_a + len(a)

    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

if __name__ == '__main__':
    create_avatar("Test")
    a = 't'
    before = before("test",a)
    after = after("test",a)
    new = before + f'[b]{a}[b]' + after
    print(new)