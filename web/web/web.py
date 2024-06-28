import reflex as rx
from web.components.navbar import navbar
from web.views.header.header import header
from web.views.links.social_links import social_links
from web.views.links.contact_links import contact_links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        social_links(),
        contact_links(),
        align="center",
    )

# App
app = rx.App()
app.add_page(index)
app._compile()
