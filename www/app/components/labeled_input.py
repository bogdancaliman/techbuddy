import reflex as rx

def labeled_input(label: str, placeholder: str, input_type: str = "text") -> rx.Component:
    return rx.box(
        rx.text(label),
        rx.input(
            placeholder=placeholder,
            type=input_type,
            size="3",
        ),
    )
