import reflex as rx
import web.styles.styles as styles

from web.components.link_icon import link_icon_button
from web.components.info_text import info_text
from web.utils.statics_method import Utils


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="/perfil.jpg", fallback="JS", size="9", radius="small"),
            rx.vstack(
                rx.heading("José de la Sierra", size="8"),
                rx.text(
                    "@lasierrayelrio",
                    margin_top="-10px !important",
                    font_size=styles.Size.DEFAULT.value,
                ),
                rx.hstack(
                    link_icon_button("https://www.twitch.tv/lasierrayelrio"),
                    link_icon_button(
                        "https://www.youtube.com/channel/UCO7sVCoQg9-AqEf-h_8e4Qw"
                    ),
                    link_icon_button("https://x.com/lasierrayelrio"),
                    link_icon_button("https://ko-fi.com/lasierrayelrio"),
                    link_icon_button("mailto:lasierrayelrio@gmail.com"),
                    align="center",
                    justify="center",
                    spacing="9",
                    margin_top=styles.Size.HUGE.value,
                    width="100%",
                ),
                align="start",
            ),
            spacing=styles.Spacing_size.MEDIUM.value,
        ),
        # AÑOS DE EXP rx.flex(info_text(f"+{Utils.calcular_anios_experiencia(2024, 3):.2f}", "años de experiencia")),
        rx.flex(
            info_text(
                f"+{Utils.calcular_anios_experiencia(2024, 3):.2f}",
                "años de experiencia",
            ),
            rx.spacer(),
            info_text(
                f"+{Utils.calcular_anios_experiencia(2024, 3):.2f}",
                "años de experiencia",
            ),
            rx.spacer(),
            info_text(
                f"+{Utils.calcular_anios_experiencia(2024, 3):.2f}",
                "años de experiencia",
            ),
            width="100%",
        ),
        rx.text(
            """Soy desarrollador de videojuegos independiente y desarrollador backend. 
                Además, creo contenido sobre mis proyectos en redes para motivar y ayudar a los demás y a mí mismo. 
                Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenide!""",
        ),
        align="start",
        spacing=styles.Spacing_size.MEDIUM.value,
    )
