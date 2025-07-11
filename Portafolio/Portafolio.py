"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


from Portafolio.views.navbar import navbar
from Portafolio.components.carta_presentacion.presentacion import componente_carta
from Portafolio.views.title import indice
from Portafolio.views.contador import contador
from Portafolio.views.programador import srprogramador
from Portafolio.style.style_page import create_background_shapes, global_styles, fondo_about_me
import Portafolio.style.style_global as Style

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
   return rx.box(
        global_styles(),
        create_background_shapes(),
        rx.flex(
            indice(),
            position="absolute",
            display="flex",
            top="0",
            right="0",
            bottom="0",
            left="0",
            align_items="center",
            justify_content="center",
        ),
        background="linear-gradient(45deg, #19242B, #446074)", #"bg-gradient-to-br from-black via-[#19242B] to-[#446074]",
        height="100vh",
        overflow="hidden",
        position="relative",
        width="100%",
    )
    
def about() -> rx.Component:
    return rx.box(
        fondo_about_me(),
                navbar(), 
                rx.flex(
               componente_carta(),
                position="absolute",
                display="flex",
                top="0",
                right="0",
                bottom="0",
                left="0",
                align_items="center",
                justify_content="center",
            ),
            width="100%",
            align_items="center",
            justify_content="center",
        ),
    
def programadorsr() -> rx.Component:
        return rx.box(
        navbar(), 
            rx.flex(
            rx.vstack(
                srprogramador(),
                width="100%"
            ),
            width="100%",
            align_items="center",
            justify_content="center",
        ),
        background="linear-gradient(45deg, black, #446074)", 
        min_height="100vh",
        height="100%",
        width="100%",
        position="relative",
        padding_top="4em",
        overflow_y="auto"
    )

def hvcontador() -> rx.Component:
    return rx.box(
        navbar(),
        rx.flex(
            rx.vstack(
                contador(),
                width="100%"
            ),
            width="100%",
            align_items="center",
            justify_content="center",
        ),
        background="linear-gradient(45deg, #446074, black)",
        min_height="100vh",
        height="100%",
        width="100%",
        position="relative",
        padding_top="4em",  # Añadir padding superior para compensar el navbar fijo,
        overflow_y="auto"
    )


app = rx.App(
    stylesheets=Style.STYLESHEETS,
    style=Style.BASE_STYLE, 
)
app.add_page(index)
app.add_page(about)
app.add_page(hvcontador)
app.add_page(programadorsr)