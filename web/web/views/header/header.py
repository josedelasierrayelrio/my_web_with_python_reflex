import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(src="/web/assets/perfil.jpg", fallback="JS", size="9"),
        rx.text("@lasierrayelrio"),
        rx.text("HOLA, MI NOMBRE ES JOSÉ DE LA SIERRA"),
        rx.text(
            """Soy desarrollador de videojuegos independiente y desarrollador backend. 
                Además, creo contenido sobre mis proyectos en redes para motivar y ayudar a los demás y a mí mismo. 
                Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenide!""",
        ),
        align="center",
    )
