import reflex as rx
from app.layouts.app_layout import app_layout

def chat() -> rx.Component:
    return app_layout(
        rx.flex(
            rx.heading(
                "Welcome to TechBuddy Chatbot! 👋",
                size="8",
                color="black"
            ),
            rx.text(
                "This chatbot provides a GPT-4o-powered chat interface to facilitate enhanced information retrieval using our sample user manuals. 📚",
                size="3",
                color="black"
            ),
            rx.divider(
                size="4",
                color_scheme="orange",
                height="2px"
            ),
            rx.text(
                "This chatbot was built by DataSentics. By using this application in the testing phase, you agree that all questions and answers will be collected and used to further improve this application. For more AI solutions and AI-related questions and answers, visit DataSentics' webpage.",
                size="3",
                color="black"   
            ),
            align="strech",
            direction="column",
            gap="16px",
            max_width="800px",
            # background_color="orange",
            margin_x="auto",
            margin_top="200px"
        )
    )