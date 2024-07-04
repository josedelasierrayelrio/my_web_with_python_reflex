import reflex as rx
import web.styles.styles as styles


def link_button(
    title: str,
    body: str,
    text_color: str,
    bg_color: str,
    url: str,
    font_size: float = styles.Size.SMALL.value,
) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    "minus",
                    size=styles.Icon_size.SMALL.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align="start",
                    spacing="1",
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
