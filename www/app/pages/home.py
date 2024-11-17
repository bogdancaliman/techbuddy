import reflex as rx
from app.layouts.app_layout import app_layout
from app.components.chat.chat import chat
from app.components.info_list import info_list

def home() -> rx.Component:
    key_points_dict = {
        "heading": "Key points",
        "items": [
            "Improvements in response to feedback.",
            "Expanded underlying documentation, utilizing the latest versions.",
            "Extended model context with user and external information, with options to enable or disable.",
            "Improved responses based on the extended context.",
            "Considering personal information in answering (demo).",
            "Considering external information in answers (demo).",
            "Filtering documents based on heat pump type and scope (user, technical).",
            "Enhanced feedback collection on the back-end.",
            "Using GPT-4o model and state of the art embedding (text-embedding-3-large) model.",
            "Several bug fixes."
        ]
    }
    
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
            rx.accordion.root(
                rx.accordion.item(
                    header="Release notes",
                    content=rx.box(
                        rx.heading("Version 0.9.5"),  
                        rx.text("Release date: 13.6. 2024"),  
                        info_list(key_points_dict["heading"], key_points_dict["items"])
                    ),
                ),
                collapsible=True,
                color_scheme="tomato"
            ),
            rx.accordion.root(
                rx.accordion.item(
                    header="Release notes",
                    content=rx.box(
                        rx.heading("Version 0.9.5"),  
                        rx.text("Release date: 13.6. 2024"),  
                        info_list(key_points_dict["heading"], key_points_dict["items"])
                    ),
                ),
                collapsible=True,
                color_scheme="tomato"
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