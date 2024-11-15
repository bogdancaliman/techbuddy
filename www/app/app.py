"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .pages.chat_page import chat_page
from .pages.forgot_password import forgot_password
from .pages.login import login
from .pages.signup import signup
from .pages.home import home


# class ScreenState(rx.State):
#     screen_type: str = "Desktop"  # Default

#     @rx.event
#     def detect_screen_size(self, width: int):
#         if width >= 1024:
#             self.screen_type = "Desktop"
#         elif width >= 768:
#             self.screen_type = "Tablet"
#         else:
#             self.screen_type = "Mobile"


# def index() -> rx.Component:
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.desktop_only(
#                 rx.heading("Welcome to Desktop!", size="9")
#             ),
#             rx.tablet_only(
#                 rx.heading("Welcome to Tablet!", size="9")
#             ),
#             rx.mobile_only(
#                 rx.heading("Welcome to Mobile!", size="9")
#             ),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#         rx.logo(),
#     )


app = rx.App()
app.add_page(home, route="/")
app.add_page(chat_page, route="/chat")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(forgot_password, route="/forgot-password")
