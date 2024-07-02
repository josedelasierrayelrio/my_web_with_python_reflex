import reflex as rx
import datetime as dt


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="favicon.ico", width="10%", height="auto"),
            rx.link(
                rx.text(
                    f"© 2021-{dt.date.today().year} lasierrayelrio by José de la Sierra v1",
                    color="black",
                ),
                is_external=True,
                href="#",
            ),
            align="center",
            justify="center",
        ),
        rx.text("⚒️ DESARROLLO DE VIDEOJUEGOS CON CONCIENCIA DE CLASE ⚒️", 
                align="center"),
        align="center",
    )
