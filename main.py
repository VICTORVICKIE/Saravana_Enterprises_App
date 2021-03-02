# IMPORT
from imports.Imports import *

# CONFIG
config = ConfigParser()
config.read("main.ini")

# CONSTANTS
AREA = literal_eval(config.get("STORAGE", "area"))
PRODUCTS = literal_eval(config.get("STORAGE", "products"))

# Paths
APP_DIR = dirname(__file__)
IMAGE_DIR = join(APP_DIR, "assets", "images")
PRODUCTS_DIR = join(IMAGE_DIR, "Products")

# SIZE
if platform == "win":
    Window.size = (300, 600)

# APP
class BillingApp(MDApp):

    # App Constants
    product_pic_dict = product_pic_dict(PRODUCTS_DIR)
    float_button_icons = {"cart": "Product", "store": "shop"}

    # Properties
    shop_dialog = ObjectProperty(None)
    shop_balance = NumericProperty()
    shop_name = StringProperty()
    source = StringProperty()

    white = ColorProperty([1, 1, 1, 1])
    black = ColorProperty([0, 0, 0, 1])
    gray = get_color_from_hex("000000")
    gray[3] = 0.12

    # Init
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_file("main.kv")

    # Navigation Drawer
    def set_nav_state(self, state):
        self.root.ids.nav_drawer.set_state(state)

    def animate(self, widget, angle):
        anim = Animation(angle=angle, duration=0.3, t="out_cubic")
        anim.start(widget)

    # Carousel
    def product_carousel(self, *args):
        for product_image_name in listdir(PRODUCTS_DIR):
            path_to_product_image = join(PRODUCTS_DIR, product_image_name)

            self.kv.ids.product_carousel.add_widget(
                CustomCarouselItem(
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
        self.kv.ids.product_carousel.load_next()

    # Callbacks
    def float_button_callback(self, button):
        print(button.icon)

    # Search Bar Menu
    def search_menu(self, text="", search=False):
        search_list = AREA + PRODUCTS
        search_menu_items = []
        if text:
            for search_term in search_list:
                if search:
                    condition = (
                        text in search_term
                        or text in search_term.lower()
                        or text in search_term.upper()
                    )
                    if condition:
                        search_menu_items.append({"text": f"{search_term}"})

        self.search_drop_menu = MDDropdownMenu(
            caller=self.kv.ids.search_menu_center_button,
            items=search_menu_items,
            position="center",
            max_height=150,
            width_mult=10,
        )
        self.search_drop_menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.kv.ids.cus.ids.search_bar.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.25)

    def set_search_mode(self, mode):

        if mode:

            size = 0

            self.kv.ids.cus.ids.search_bar.opacity = 1
            self.kv.ids.cus.ids.search_bar.disabled = False
            self.kv.ids.cus.ids.search_bar.focus = True
            self.kv.ids.cus.ids.search_bar.line_color_focus = self.white

            self.kv.ids.mag.opacity = 0
            self.kv.ids.mag.disabled = True

            Animation(opacity=1, d=0.2).start(self.kv.ids.cus.ids.search_bar)
            Animation(size=(size, size), opacity=0, d=0.2).start(self.kv.ids.mag)
            Animation(size=(size, size), opacity=0, d=0.2).start(self.kv.ids.tune)

        else:

            size = dp(42)

            self.kv.ids.cus.ids.search_bar.opacity = 0
            self.kv.ids.cus.ids.search_bar.disabled = True

            self.kv.ids.mag.opacity = 1
            self.kv.ids.mag.disabled = False

            Animation(opacity=0, d=0.2).start(self.kv.ids.cus.ids.search_bar)
            Animation(size=(size, size), opacity=1, d=0.2).start(self.kv.ids.mag)
            Animation(size=(size, size), opacity=1, d=0.2).start(self.kv.ids.tune)

    # Area Menu
    def area_menu(self):
        area_list = [{"text": area} for area in AREA]
        self.area_menu = MDDropdownMenu(
            caller=self.kv.ids.area_menu,
            items=area_list,
            width_mult=4,
            position="bottom",
        )
        self.kv.ids.area_menu.text = "Pick an Area"
        self.area_menu.bind(on_release=self.set_area)

    def set_area(self, instance_menu, instance_menu_item):
        self.current_area = instance_menu_item.text
        self.kv.ids.area_menu.set_item(self.current_area)
        self.area_menu.dismiss()

    # Shop Dialog
    def add_shop_dialog(self):
        if not self.shop_dialog:
            self.shop_dialog = MDDialog(
                title="Add :",
                type="custom",
				overlay_color=(0, 0, 0, 0),
                content_cls=AddShopDialog(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_shop_dialog,
                    ),
                    MDFlatButton(
                        text="ADD",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.get_shop_details,
                    ),
                ],
            )
        self.shop_dialog.set_normal_height()
        self.shop_dialog.open()

    def get_shop_details(self, inst):
        try:
            if not self.shop_dialog.content_cls.children[2].text == "":
                self.shop_name = self.shop_dialog.content_cls.children[2].text
                self.shop_balance = self.shop_dialog.content_cls.children[1].text
                print(self.current_area, self.shop_name, self.shop_balance)
                self.shop_dialog.content_cls.children[2].text = ""
                self.shop_dialog.content_cls.children[1].text = "0"
                self.shop_dialog.content_cls.children[0].text = "+91"
                self.shop_dialog.dismiss()

        except Exception as e:
            print(e)
            self.shop_dialog.dismiss()

    def close_shop_dialog(self, inst):
        self.shop_dialog.content_cls.children[2].text = ""
        self.shop_dialog.content_cls.children[1].text = "0"
        self.shop_dialog.content_cls.children[0].text = "+91"
        self.shop_dialog.dismiss()

    def show_fps(self, show):
        condition = instance_in_children(Window, FpsMonitor)[0]
        children = instance_in_children(Window, FpsMonitor)[1]
        if show:
            if not condition:
                monitor = FpsMonitor()
                Window.remove_widget(monitor)
                monitor.start()
                Window.add_widget(monitor)
        else:
            if condition:
                Window.remove_widget(children)

    # Initializing App
    def on_start(self):
        self.data_storage = Storage()
        self.search_menu()
        self.product_carousel()
        self.product_carousel_autoplay()
        self.area_menu()

    # Building App
    def build(self):
        return self.kv


if __name__ == "__main__":

    app = BillingApp()
    print(kivymd.__version__)
    app.run()
