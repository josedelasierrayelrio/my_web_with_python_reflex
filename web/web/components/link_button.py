import reflex as rx
import web.styles.styles as styles


def link_button(text: str, text_color: str, bg_color: str, url: str, font_size: float = styles.Size.SMALL.value) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("plus"),
                rx.vstack(
                    rx.text(text),
                    rx.text(text),
                ),
                align="center",
            ),
            color=text_color,
            color_scheme=bg_color,
        ),
        href=url,
        is_external=True,
        width="100%",
    )
