import reflex as rx


def link_button(text: str, text_color: str, bg_color: str, url: str) -> rx.Component:
    return rx.link(rx.button(text, color=text_color, color_scheme=bg_color), href=url, is_external=True)
