import reflex as rx

def info_list(heading_text: str, list_items: list[str]) -> rx.Component:
    heading = rx.heading(heading_text)
    text_list = rx.list.unordered(
        *[rx.list.item(item) for item in list_items]
    )    
    return rx.box(
        heading,
        text_list
    )
