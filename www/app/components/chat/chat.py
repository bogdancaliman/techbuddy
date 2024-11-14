import reflex as rx

def chat() -> rx.Component:
    return rx.box(
        "Chat",
        background_color="yellow",
        height="100%",
        border_radius="16px",
        padding="8px"
    )