import reflex as rx
import web.styles.styles as styles

from web.components.link_button import link_button


def social_links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Twitch",
            "Directos de vez en cuando",
            "white",
            "purple",
            "https://www.twitch.tv/lasierrayelrio",
        ),
        link_button(
            "YouTube",
            "Devlogs y análisis sobre diseño",
            "white",
            "red",
            "https://www.youtube.com/channel/UCO7sVCoQg9-AqEf-h_8e4Qw",
        ),
        link_button(
            "Twitter",
            "Donde comparto el avance de mis proyectos",
            "white",
            "cyan",
            "https://x.com/lasierrayelrio",
        ),
        link_button(
            "Kofi",
            "Apóyame por menos de lo que cuesta un café",
            "white",
            "tomato",
            "https://ko-fi.com/lasierrayelrio",
        ),
        link_button(
            "Contacto",
            "Contacto profesional",
            "white",
            "gray",
            "mailto:lasierrayelrio@gmail.com",
        ),
        align="center",
        width="100%",
    )
