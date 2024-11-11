import reflex as rx

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
                ),
            ),
            rx.box(     
                rx.text("Name"),
                rx.input( 
                    placeholder="John",
                    type="text",
                    size="3"

                ),
            ),
            rx.box(
                rx.text("Password"),
                rx.input(
                    placeholder="******",
                    type="password",
                    size="3"

                ),
            ),
            rx.button("Login"),
            spacing="4",
            direction="column",
            justify="center",
            align="center",
        ),
        height="100vh",
    )
    
    
# vstack(
#         rx.link(
#                 rx.button("Go to reset password"),
#                 href="/reset-password",
#                 is_external=False,
#             ),
#         rx.link(
#                 rx.button("Go to signup"),
#                 href="/signup",
#                 is_external=False,
#             )
#     )