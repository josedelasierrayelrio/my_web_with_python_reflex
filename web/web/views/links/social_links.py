import reflex as rx
import web.styles.styles as styles

from web.components.link_button import link_button


def social_links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Twitch", "white", "purple", "https://www.twitch.tv/lasierrayelrio",  styles.Size.BIG.value
        ),
        link_button(
            "YouTube | Canal secundario",
            "white",
            "tomato",
            "https://www.youtube.com/channel/UCO7sVCoQg9-AqEf-h_8e4Qw",
        ),
        link_button("Twitter", "white", "cyan", "https://x.com/lasierrayelrio"),
        link_button("Patreon", "white", "gray", "mailto:lasierrayelrio@gmail.com"),
        link_button("Kofi", "white", "gray", "mailto:lasierrayelrio@gmail.com"),
        link_button("Contacto", "white", "gray", "mailto:lasierrayelrio@gmail.com"),
        align="center",
        width="100%",
    )
