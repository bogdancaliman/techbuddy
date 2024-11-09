import reflex as rx

def signup() -> rx.Component:
    return rx.vstack(
        rx.link(
                rx.button("Go to login"),
                href="/login",
                is_external=False,
            ),
        rx.link(
                rx.button("Go to reset password"),
                href="/reset-password",
                is_external=False,
            )
    )