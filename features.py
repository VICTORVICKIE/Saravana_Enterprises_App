



# class MyScreenManager(ScreenManager):
#     previous_screen = None

#     def set_screen(self, screen_name, side="left"):
#         self.previous_screen = {"name": self.current, "side": side}
#         self.transition.direction = side
#         self.current = screen_name

#     def goto_previous_screen(self):
#         self.set_screen(
#             self.previous_screen["name"],
#             side="right" if self.previous_screen["side"] == "left" else "left",
#         )
