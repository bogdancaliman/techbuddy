import reflex as rx
from .sidebar_button import sidebar_button

def sidebar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.heading("TechBuddy", size="lg"),
                sidebar_button(label="Home", icon_src="/home.svg", href="/"),
                sidebar_button(label="Chat", icon_src="/chat.svg", href="/chat"),
                sidebar_button(label="Report", icon_src="/report.svg", href="/report"),
                direction="column",
                gap="16px",
            ),
            rx.flex(
                sidebar_button(label="Settings", icon_src="/settings.svg", href="/settings"),
                sidebar_button(label="Account", icon_src="/account.svg", href="/account"),
                sidebar_button(label="Logout", icon_src="/logout.svg", href="/logout"),
                direction="column",
                gap="16px",
            ),
            direction="column",
            justify="between",
            height="100%",
            width="100%",
            gap="16px",
        ),
        width="350px",
        padding_y="24px",
        padding_x="16px",
    )
