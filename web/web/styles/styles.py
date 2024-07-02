import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH: str = "600px"
MEDIUM_WIDTH: str = ""
MIN_WIDTH: str = ""


# Sizes
class Size(Enum):
    HUGE="3em"
    BIG = "2em"
    MEDIUM = "0.8em"
    SMALL = "0.5em"
    LITTLE_BIGGER = ("1.2em")
    MEDIUM_BIGGER = ("1.5em")
    BIG_BIGGER = ("1.8em")
    DEFAULT = "1em"


class Icon_size(Enum):
    BIG = 30
    MEDIUM = 25
    SMALL = 15
    DEFAULT = 20

class Spacing_size(Enum):
    BIG = "9"
    LITTLE_BIGGER = "8"
    DEFAULT = "7"
    MEDIUM = "5"
    SMALL = "3"
    LITTLE_SMALLER = "2"
    TINY = "1"
    MINIMUM = "0"


class Colors(Enum):
    RED = "#CD5151"
    BLACK = "#2B2A26"
    ORANGE = "#F79A00"
    YELLOW = "#FFB901"
    WHITE = "#FFEEC3"


# Styles
BASE_STYLE: dict = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
    rx.link: {"text_decoration": "none", "_hover": {}},
    rx.text: {
        "font_size": Size.DEFAULT.value,
    },
}

title_style: dict = dict(
    font_size=Size.MEDIUM_BIGGER.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style: dict = dict(
    font_size=Size.LITTLE_BIGGER.value,
)

button_body_style: dict = dict(
    font_size=Size.MEDIUM.value,
)
