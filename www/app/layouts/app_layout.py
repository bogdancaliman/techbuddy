import reflex as rx
from app.components.sidebar import sidebar


def app_layout(content: rx.Component) -> rx.Component:
    return rx.flex(
        rx.desktop_only(
            sidebar(),
        ),
        rx.box(
            rx.scroll_area(
                rx.flex(
                    content,
                    # background_color="gray",
                    justify="center",
                    align="between",
                    # width="calc(100vw - 400px)",
                    # width={"base": "100vw", "lg": "calc(100vw - 400px)"},
                    # width=rx.breakpoints({
                    #     "0px": "100%",        
                    #     "62em": "calc(100vw - 400px)",  
                    # }),
                    width=rx.breakpoints(
                        initial = "100%",
                        md = "calc(100vw - 400px)"
                    ),
                    height="100%",
                    # padding="1px"
                    # width="100vw"
                ),
                background_color=rx.color("gray", 12),
                height="100%",
                # border_radius="16px",
                border_radius=rx.breakpoints(
                    initial="0px",
                    md="16px"
                ),
                padding=rx.breakpoints(
                    initial="4px",
                    md="32px"
                ),
                # padding="32px",
                align_items="stretch",
                scrollbars="vertical",
                # background_color="blue",
                # width="100vw"

            ),  
            # background_color="green",
            width="100%",
            padding=rx.breakpoints(
                initial="0px",
                md="16px"
            ),
            # padding="16px",
            # overflow="hidden",
        ),
        height="100vh",
        width="100%",
    )