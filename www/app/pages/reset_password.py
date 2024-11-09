import reflex as rx

def reset_password() -> rx.Component:
    return rx.vstack(
        rx.link(
                rx.button("Go to login"),
                href="/login",
                is_external=False,
            ),
        rx.link(
                rx.button("Go to signup"),
                href="/signup",
                is_external=False,
            )
    )