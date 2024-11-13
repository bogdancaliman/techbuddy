import reflex as rx
from app.layouts.auth_layout import auth_layout
from app.components.labeled_input import labeled_input
# import requests

# API_URL = "http://127.0.0.1:8000/login"

# class LoginState(rx.State):
#     email: str = ""
#     name: str = ""
#     password: str = ""
#     login_message: str = ""
    
#     jwt_token: str = rx.LocalStorage(name="auth_token", sync=True)

#     def handle_login(self):
#         """Function to handle login API call."""
#         login_data = {
#             "email": self.email,
#             "name": self.name,
#             "password": self.password,
#         }

#         try:
#             response = requests.post(API_URL, json=login_data)
            
#             if response.status_code == 200:
#                 self.jwt_token = response.cookies.get("access_token") or response.json().get("token")
#                 self.login_message = "Login successful!"
#             else:
#                 self.login_message = f"Login failed: {response.json().get('detail', 'Unknown error')}"
#         except Exception as e:
#             self.login_message = f"An error occurred: {str(e)}"
    
#     def logout(self):
#         self.jwt_token = ""  
#         self.login_message = "Logged out successfully"

# def labeled_input(label: str, placeholder: str, input_type: str = "text") -> rx.Component:
#     return rx.box(
#         rx.text(label),
#         rx.input(
#             placeholder=placeholder,
#             type=input_type,
#             size="3",
#         ),
#     )

def login() -> rx.Component:
    return auth_layout(
        title="Login",
        form_content=[
            labeled_input("Email", "john-doe@email.com", "email"),
            labeled_input("Password", "******", "password"),
            rx.box(    
                rx.text("Don't have an account? "),
                rx.flex(
                    rx.link("Sign Up", href="/signup", color=rx.color("blue", 11), text_decoration="underline"),
                    rx.spacer(),
                    rx.link("Forgot Password?", href="/forgot-password", color=rx.color("blue", 11), text_decoration="underline"),
                    spacing="4",
                ),
            ),
        ],
        button_text="Login"
    )


    

# Example protected page
# def protected_page() -> rx.Component:
#     """Protected page component to display only if logged in."""
#     return rx.container(
#         rx.flex(
#             rx.heading("Protected Page"),
#             rx.text("You are logged in and can access this page!"),
#             rx.button("Logout", on_click=LoginState.logout),
#             spacing="4",
#             direction="column",
#             justify="center",
#             align="center",
#         ),
#         height="100vh",
#     )
