import reflex as rx
from app.layouts.auth_layout import auth_layout
from app.components.labeled_input import labeled_input

def forgot_password() -> rx.Component:
    return auth_layout(
        title="Forgot Password",
        form_content=[
            labeled_input("Email", "john-doe@example.com", "email"),
            rx.link(
                "← login",
                href="/login",
                color=rx.color("blue", 11),  
                text_decoration="underline",
                font_size="sm",
            ),
        ],
        button_text="Reset Password",
    )