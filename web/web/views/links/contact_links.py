import reflex as rx
from web.components.link_button import link_button

def contact_links() -> rx.Component:
    return rx.vstack(
        link_button("Patreon", "white", "gray", "mailto:lasierrayelrio@gmail.com"), 
        link_button("Kofi", "white", "gray", "mailto:lasierrayelrio@gmail.com"), 
        link_button("Contacto", "white", "gray", "mailto:lasierrayelrio@gmail.com"), 
        align="center")


