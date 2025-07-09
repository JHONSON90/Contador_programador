from turtle import width
import reflex as rx
from Portafolio.components.detalles.experiencia import habilidades
from Portafolio.style.sizes import Size


def srprogramador() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.vstack(
                rx.heading("Hola, soy Edison!!!", 
                        size=rx.breakpoints(initial="7", sm="8", lg="9"),
                        weight="bold",
                        ),
                rx.text.strong("Desarrollador Full Stack apasionado por crear experiencias web únicas y memorables", 
                        size=rx.breakpoints(initial="3", sm="4", lg="5"),
                        ),
                rx.hstack(
                    rx.button(
                        rx.icon("at-sign", tag = "Email"),
                        "Email",
                        variant="ghost",
                        size="2",
                        color_scheme="gray",
                        high_contrast=True,
                        on_click= rx.redirect("mailto:edisonportillal@gmail.com", is_external=True)
                        ),
                    rx.button(
                        rx.icon("github", tag = "GitHub", size=30),
                        "GitHub",
                        size="2",
                        variant="ghost",
                        color_scheme="gray",
                        high_contrast=True,
                        on_click= rx.redirect("https://github.com/JHONSON90", is_external=True)
                    ),
                    align="center",
                    justify="center",
                    width=["100%", "80%", "50%"],
                ),
                align="center",
                justify="center",
                width= "100%",
                padding=["1rem", "1.5rem", "2rem"],
                text_align="center",
                min_height=["100vh", "100vh", "100vh"],
                margin_bottom="2rem",
            ),
            rx.vstack(
                rx.heading("Sobre Mi", 
                    size=rx.breakpoints(initial="7", sm="8", lg="9"),
                    margin_bottom= Size.LARGE.value
                    ),
                rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.icon("code-xml", size=60, color= rx.color("indigo",11)),
                        rx.text("Desarrollo Web",
                        weight="bold",
                        size=rx.breakpoints(initial="5", sm="6", lg="7"),
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Me especializo en crear aplicaciones web modernas y responsivas usando las últimas tecnologías"),
                        spacing="2"
                    ),
                    width=["100%", "45%", "30%"],
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("heart", size=60,color= rx.color("indigo",11)),
                        rx.text("Diseño UI/UX",
                        weight="bold",
                        size=rx.breakpoints(initial="5", sm="6", lg="7"),
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Creo interfaces intuitivas y atractivas que mejoran la experiencia del usuario")
                    ),
                    width=["100%", "45%", "30%"],
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("coffee", size=60, color= rx.color("indigo",11)),
                        rx.text("Siempre Aprendiendo",
                        weight="bold",
                        size=rx.breakpoints(initial="5", sm="6", lg="7"),
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Constantemente explorando nuevas tecnologías y mejores prácticas")
                    ),
                    width=["100%", "45%", "30%"],

                ),
                flex_direction=["column","column","row"],
                spacing="2",
                width="100%",
                justify="center",
            ),
                align="center",
                justify="center",
                width= "100%",
                min_height=["auto", "auto", "100vh"],
                text_align="center",
                margin_y=["2rem", "2.5rem", "3rem"],

            ),
            rx.vstack(
                rx.heading("Mejores Proyectos",
                           size=rx.breakpoints(initial="7", sm="8", lg="9"),
                           margin_bottom= Size.LARGE.value
                           ),
                rx.hstack(
                    rx.card(
                        rx.vstack(
                        rx.image(src="/programador/registro_diario.JPG", alt="Menú del proyecto y pendiente autorización para publicar el resto de componentes", height = "180px", width = "100%"),
                        rx.text("Segumiento a Consignaciones",
                                weight="bold",
                                size=rx.breakpoints(initial="4", sm="5", lg="6"),
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text.span("Aplicación moderna construida para gestionar y controlar las consignaciones recibidas de una empresa",
                                ),
                        rx.hstack(
                            rx.badge("Flet",
                                     color_scheme="indigo", variant="outline", high_contrast=True
                                     ),
                            rx.badge("MySQL",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Firebase",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                                     spacing="2"
                            ),
                            spacing="2"
                        ),
                        width=["100%", "45%", "30%"],
                        height = "auto"
                    ),
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.card(
                        rx.vstack(
                        rx.image(src="/programador/281_1x_shots_so.webp",alt="Solicitando autorizacion para colocar imagenes del proyecto",height = "180px", width = "100%"),
                        rx.text("Seguimiento de Costos",
                                weight="bold",
                                size="6",
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text.span("Aplicación construida para controlar los costos de una empresa que se dedica al sector salud donde se puede obtener el detalle de los componentes de los costos"),
                        rx.hstack(
                            rx.badge("Streamlit",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Pandas",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Plotly",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Google Cloud",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            spacing="2"
                        ),
                        spacing="2"
                        ),
                        width=["100%", "45%", "30%"],
                        height = "auto",
                    ),

                        ),
                        rx.dialog.content(
                            rx.image(src="/programador/281_1x_shots_so.webp", alt="imagen del menu del proyecto de seguimiento de costos",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.image(src="/programador/205shots_so.webp", alt="imagen del menu del proyecto de seguimiento de costos",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.image(src="/programador/769shots_so.webp", alt="imagen del menu del proyecto de seguimiento de costos",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.image(src="/programador/856shots_so.webp", alt="imagen del menu del proyecto de seguimiento de costos",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.dialog.close(
                            rx.button("X",
                            size="1",
                            variant="outline",
                            color_scheme = "red",
                            high_contrast = False,
                            width = "2%"
                    )
                        ),
                        max_width = ["90vw", "900px"],
                        max_height = ["90vh", "900px"],
                        style = {"display": "flex", "flex_direction": ["column", "column", "row"], "height": "auto"}
                    ),
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.card(
                        rx.vstack(
                        rx.image(src="/programador/522_1x_shots_so.webp", alt="imagen donde esta el menu de una aplicacion web que permite hacer clasificacion a una poblacion", 
                                 height = "180px", width = "100%"),
                        rx.text("Clasificador de Poblacion",
                                weight="bold",
                                size="6",
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text.span("Aplicación construida para clasificar una poblacion entregada en una base de datos con el objetivo de clasificar la poblacion por curso de vida y municipios y sexo"),
                        rx.hstack(
                            rx.badge("Streamlit",   
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Pandas",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Numpy",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Plotly",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Excel",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            spacing="2"
                        ),
                        spacing="2"
                        ),
                        width=["100%", "45%", "30%"],
                        height = "auto"
                    ),

                        ),
                        rx.dialog.content(
                            rx.image(src="/programador/522_1x_shots_so.webp", alt="imagen del menu del proyecto de clasificacion de población",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),

                        rx.image(src="/programador/863shots_so.webp", alt="imagen del cargue de la base de datos a clasificar",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                            rx.image(src="/programador/800shots_so.webp", alt="Imagen de la clasificacion que realiza segun la base de datos recibida",
                            style={
                                "width": "100%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    #"width": "500px",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.dialog.close(
                            rx.button("X",
                            size="1",
                            variant="outline",
                            color_scheme = "red",
                            high_contrast = False,
                            width = "2%"
                    )
                        ),
                        max_width = ["90vw", "900px"],
                        max_height = ["90vh", "900px"],
                        style = {"display": "flex", "flex_direction": ["column","column","row",], "height": "auto"}
                    ),

                        ),
                    ),
                    
                    flex_direction=["column", "row", "row"],  # Apilar en móviles
                    spacing="2",
                    width="100%",
                    justify="center",
                ),
                align="center",
                justify="center",
                width= "100%",
                min_height=["auto", "auto", "100vh"],
                text_align="center",
                margin_y=["2rem", "2.5rem", "3rem"],

            ),
            rx.vstack(
                rx.heading("Habilidades",
                           size=rx.breakpoints(initial="7", sm="8", lg="9"),
                           margin_bottom = Size.LARGE.value,
                ),
                rx.grid(
                    rx.card(
                         rx.center(
                             rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                             habilidades("Python", 80 ),    
                             width = "100%",
                             height = "100%",
                         ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                          rx.center(
                              rx.image(src="/FLET_LOGO.png",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                              habilidades("Flet", 80 ),
                                    width = "100%",
                             height = "100%",),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ), 
                     rx.card(
                         rx.center(
                             rx.image(src="/REFLEX_LOGO.png",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                             habilidades("Reflex", 70 ),
                                   width = "100%",
                             height = "100%",
                                   ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("HTML/CSS", 60 ),
                              width = "100%",
                             height = "100%",
                             ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                     rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("Javascript", 60 ),
                              width = "100%",
                             height = "100%",
                             ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("React", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("Postgress", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                       rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("FastApi", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                        rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg",
                                 width = ["30px", "40px"],
                                 height = ["30px", "40px"]),
                        habilidades("MySQL", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="120px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      columns=rx.breakpoints(initial="2", sm="2", lg="3"),
                      spacing="2",
                      width="100%",
                     #margin= Size.MEDIUM.value
                ),
            
                align="center",
                justify="center",
                width= "100%",
                min_height=["auto", "auto", "100vh"],
                text_align="center",
                margin=["1rem", "1.5rem", "2rem"],
                margin_y=["2rem", "2.5rem", "3rem"],
            ),
            spacing="9",
            width="100%",
            align="center",
            justify="center",
        ),
        width="100%",
        max_width=rx.breakpoints(initial="100vw", sm="100vw", lg="1200px"),
        margin=["0 auto", "0 auto", Size.DEFAULT.value],
        padding=rx.breakpoints(initial="1rem", sm="1.5rem", lg="2rem"),
        flex_direction="column",
        spacing="4",
    )