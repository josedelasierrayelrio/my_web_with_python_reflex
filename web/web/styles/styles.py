import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH: str = "600px"
MEDIUM_WIDTH: str = ""
MIN_WIDTH: str = ""


# Sizes
class Size(Enum):
    BIG = ("2em",)
    SMALL = ("0.5em",)
    DEFAULT = "1em"


# Styles
BASE_STYLE: dict = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}
