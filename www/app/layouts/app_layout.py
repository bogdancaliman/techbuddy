import reflex as rx
from app.components.sidebar import sidebar


def app_layout(content: rx.Component) -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.box(
            content,  
            background_color="orange",
            width="100%",
            padding="16px"
        ),
        height="100vh",
        width="100vw",
    )