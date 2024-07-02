import reflex as rx
import web.styles.styles as styles


def info_text(
    title: str, body_text: str, title_font_size_em: str = styles.Size.LITTLE_BIGGER.value, 
    body_font_size_em: str = styles.Size.DEFAULT.value, body_color: str = "black", title_color: str = "black"
) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            color=title_color,
            style={"font_size": title_font_size_em},
            as_="span",
        ),
        f" {body_text}",
        color=body_color,
        style={"font_size": body_font_size_em},
    )
