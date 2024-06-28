import reflex as rx
from web.components.link_button import link_button

def social_links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "white", "purple", "https://www.twitch.tv/lasierrayelrio"), 
        link_button("YouTube", "white", "tomato", "https://www.youtube.com/channel/UCO7sVCoQg9-AqEf-h_8e4Qw"), 
        link_button("Twitter", "white", "cyan", "https://x.com/lasierrayelrio"), 
        align="center")


