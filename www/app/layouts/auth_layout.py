import reflex as rx

def auth_layout(
    title: str,
    form_content: list[rx.Component],
    button_text: str,
    button_action: str = None,
) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.flex(
                rx.heading(title),
                *form_content,
                rx.button(button_text, on_click=button_action),
                spacing="4",
                direction="column",
                justify="center",
                min_width="300px"
            )
        ),
        spacing="4",
        direction="column",
        justify="center",
        align="center",
        height="100vh",
        width="100vw",
    )
