import reflex as rx
from app.layouts.app_layout import app_layout
from app.components.chat.chat import chat


def home() -> rx.Component:
    return app_layout(
        content=chat()
    )