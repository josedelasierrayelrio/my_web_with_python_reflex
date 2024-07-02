import reflex as rx
import web.styles.styles as styles


def link_icon_button(url: str, color: str = "black") -> rx.Component:
    return rx.link(
        rx.icon(tag="link", color=color),
        href=url,
        is_external=True,
    )
