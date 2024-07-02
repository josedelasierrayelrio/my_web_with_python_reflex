import reflex as rx
from web.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "lasierrayelrio",
        ),
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
    )
