import reflex as rx
from app.components.sidebar import sidebar


def app_layout(content: rx.Component) -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.box(
            rx.box(
                content,
                background_color=rx.color("gray", 12),
                height="100%",
                border_radius="16px",
                padding="32px"
            ),  
            # background_color="orange",
            width="100%",
            padding="16px"
        ),
        height="100vh",
        width="100vw",
    )