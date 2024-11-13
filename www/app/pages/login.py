import reflex as rx
import requests

# Endpoint URL of the FastAPI server
API_URL = "http://127.0.0.1:8000/login"

# State class to manage login state and handle the API call
class LoginState(rx.State):
    email: str = ""
    name: str = ""
    password: str = ""
    login_message: str = ""
    
    # Use LocalStorage to store JWT token between pages
    jwt_token: str = rx.LocalStorage(name="auth_token", sync=True)

    def handle_login(self):
        """Function to handle login API call."""
        login_data = {
            "email": self.email,
            "name": self.name,
            "password": self.password,
        }

        try:
            # Make a POST request to the login endpoint
            response = requests.post(API_URL, json=login_data)
            
            if response.status_code == 200:
                # Extract the JWT token from cookies or response JSON, depending on the implementation
                self.jwt_token = response.cookies.get("access_token") or response.json().get("token")
                self.login_message = "Login successful!"
            else:
                self.login_message = f"Login failed: {response.json().get('detail', 'Unknown error')}"
        except Exception as e:
            self.login_message = f"An error occurred: {str(e)}"
    
    def logout(self):
        """Clear the token and log out."""
        self.jwt_token = ""  # This removes the token from LocalStorage
        self.login_message = "Logged out successfully"

# Login component
def login() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.heading("Login"),
            rx.box(
                rx.text("Email"),
                rx.input(
                    placeholder="john-doe@email.com",
                    type="email",
                    size="3",
                    on_change=LoginState.set_email,
                ),
            ),
            rx.box(
                rx.text("Name"),
                rx.input(
                    placeholder="John",
                    type="text",
                    size="3",
                    on_change=LoginState.set_name,
                ),
            ),
            rx.box(
                rx.text("Password"),
                rx.input(
                    placeholder="******",
                    type="password",
                    size="3",
                    on_change=LoginState.set_password,
                ),
            ),
            rx.button("Login", on_click=LoginState.handle_login),
            rx.text(LoginState.login_message),
            spacing="4",
            direction="column",
            justify="center",
            align="center",
        ),
        height="100vh",
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
