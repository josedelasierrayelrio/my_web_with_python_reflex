import reflex as rx
import web.styles.styles as styles

from web.components.navbar import navbar
from web.components.footer import footer
from web.views.header.header import header
from web.views.links.social_links import social_links


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                social_links(),
                max_width=styles.MAX_WIDTH,
                margin_y=styles.Size.BIG.value,
                align="center",
                width="100%",
            ),
        ),
        footer(),
    )


# App
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
app._compile()
