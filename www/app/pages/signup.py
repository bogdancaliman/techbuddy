import reflex as rx
from app.layouts.auth_layout import auth_layout
from app.components.labeled_input import labeled_input

def signup() -> rx.Component:
    return auth_layout(
        title="Signup",
        form_content=[
            labeled_input("Email", "john-doe@example.com", "email"),
            labeled_input("Name", "John", "text"),
            labeled_input("Password", "******", "password"),
            rx.link(
                "← login",
                href="/login",
                color=rx.color("blue", 11),  
                text_decoration="underline",
                font_size="sm",
            ),
        ],
        button_text="Signup",
    )