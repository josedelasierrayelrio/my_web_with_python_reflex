import reflex as rx
from web.components.navbar import navbar

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        
    )


#NavBar


# App
app = rx.App()
app.add_page(index)
app._compile()
