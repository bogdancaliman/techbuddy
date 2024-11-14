import reflex as rx

def sidebar_button(label: str, icon_src: str, href: str = None) -> rx.Component:
    return rx.link(
        rx.flex(
            rx.image(
                src=icon_src,
                width="20px",
                height="20px",
            ),
            rx.text(label, size="3", color="white",),
            gap="8px",
            align="center",
            padding_y="8px",
            padding_x="16px",
            opacity=1,
            style={"transition": "background-color 0.1s ease-in-out"},
            _hover={
                "background-color": rx.color("gray", 8),
            },
            border_radius="16px",
        ),
        href=href,
    )
