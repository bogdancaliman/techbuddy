import reflex as rx
from app.layouts.app_layout import app_layout
# from app.state import State
from .components.chat import chat_view, action_bar

def chat() -> rx.Component:
    return app_layout(
        rx.flex(
            chat_view(),
            action_bar(),
            # align="strech",
            direction="column",
            gap="16px",
            max_width="800px",
            # background_color="orange",
            justify="between",
            # position="relative"
            # margin_x="auto",
            # margin_top="200px",
            
            # height="100%"
        )
    )