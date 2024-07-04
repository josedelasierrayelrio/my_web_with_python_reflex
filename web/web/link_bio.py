import reflex as rx
import web.styles.styles as styles

from web.components.navbar import navbar
from web.components.footer import footer
from web.components.title import title
from web.views.link_bio.header.header import header
from web.views.link_bio.links.social_links import social_links


@rx.page(route="/link_bio", title="Link_bio")
def index_link_bio() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                title("Comunidad"),
                social_links(),
                title("Comunidad"),
                social_links(),
                title("Comunidad"),
                social_links(),
                max_width=styles.MAX_WIDTH,
                margin_y=styles.Size.BIG.value,
                width="100%",
            ),
        ),
        footer(),
    )
