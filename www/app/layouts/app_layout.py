import reflex as rx
from app.components.sidebar import sidebar


def app_layout(content: rx.Component) -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.box(
            rx.scroll_area(
                rx.flex(
                    content,
                    # background_color="gray",
                    justify="center",
                    align="between",
                    width="calc(100vw - 400px)",
                    height="100%"
                    # width="100vw"
                ),
                background_color=rx.color("gray", 12),
                height="100%",
                border_radius="16px",
                padding="32px",
                align_items="stretch",
                scrollbars="vertical",
                # background_color="blue",
                # width="100vw"

            ),  
            # background_color="green",
            width="100%",
            padding="16px",
            overflow="hidden",
        ),
        height="100vh",
        width="100%",
    )