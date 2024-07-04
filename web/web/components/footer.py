import reflex as rx
import datetime as dt
import web.styles.styles as styles


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", width="5%", height="auto"),
        rx.link(
            rx.text(
                f"© 2021-{dt.date.today().year} lasierrayelrio by José de la Sierra",
                color="black",
                font_size=styles.Size.MEDIUM,
            ),
            is_external=True,
            href="#",
        ),
        rx.text(
            "⚒️ DESARROLLO DE VIDEOJUEGOS CON CONCIENCIA DE CLASE ⚒️",
            align="center",
            font_size=styles.Size.MEDIUM,
            margin_top="-1em !important",
        ),
        align="center",
        justify="center",
        margin_bottom=styles.Size.BIG.value,
    )
