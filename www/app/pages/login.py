import reflex as rx

def login() -> rx.Component:
    return rx.vstack(
        rx.link(
                rx.button("Go to reset password"),
                href="/reset-password",
                is_external=False,
            ),
        rx.link(
                rx.button("Go to signup"),
                href="/signup",
                is_external=False,
            )
    )