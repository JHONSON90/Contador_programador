import reflex as rx
from Portafolio.components.detalles.experiencia import titulos, experiencia, estudios, habilidades, habilidades_personales, hobies
from Portafolio.style.sizes import Size

class State(rx.State):
    power_bi: bool = False
    excel: bool = False
    automatizacion: bool = False
    
    def abrir_dialog(self, dialog_number: int):
        if dialog_number == 1:
            self.power_bi = not self.power_bi
        elif dialog_number == 2:
            self.excel = not self.excel
        elif dialog_number == 3:
            self.automatizacion = not self.automatizacion


def contador()->rx.Component:
    return rx.flex(
        rx.box(
            rx.vstack(
            titulos("HABILIDADES DE SOFTWARE"),
            rx.spacer(spacing="2", direction="row"),
            habilidades("Excel", 80),
            habilidades("Python", 70),
            habilidades("Pandas", 60),
            habilidades("Numpy", 50),
            habilidades("Power Bi", 70),
            habilidades("SQL", 70),
            ),
            rx.vstack(
                rx.spacer(spacing="4", direction="row"),
            titulos("LENGUAJES"),
            rx.spacer(spacing="2", direction="row"),
            habilidades("Español", 99),
            habilidades("Ingles", 60),
            rx.spacer(spacing="2", direction="row"),
            ),
            rx.vstack(
                rx.spacer(spacing="4", direction="row"),
            titulos("VALORES"),
            rx.spacer(spacing="2", direction="row"),
            habilidades_personales("- Responsabilidad"),
            habilidades_personales("- Integridad"),
            habilidades_personales("- Objetividad"),
            habilidades_personales("- Confidencialidad"),
            habilidades_personales("- Proactividad"),
            habilidades_personales("- Aprendizaje continuo"),
            spacing="1"            
            ),
            width=["100%", "100%", "33%"],
            margin="1rem",
            padding="1rem"            
        ),
        rx.box(
            titulos("EXPERIENCIA LABORAL"),
            rx.spacer(spacing="6", direction="row"),
            experiencia("01-2021","08-2024", "Proinsalud S.A", "Coordinador de Costos", "Realizar un análisis de costos exhaustivo, cubriendo el 95% de los costos y gastos totales, con una distribución por unidad funcional y centro de costo. Además, determinar el costo del 70% de los procedimientos."),
            rx.spacer(spacing="3", direction="row"),
            experiencia("02-2017","11-2017", "Cooperativa Multiactiva Social Mayorista","Contador","Control y seguimiento exhaustivo al 100% de los movimientos contables, garantizando la precisión en la presentación de informes a la junta directiva y a entidades regulatorias. Elaboración oportuna de ajustes contables, reduciendo el margen de error a 7%." ),
            rx.spacer(spacing="3", direction="row"),
            experiencia("02-2017", "11-2017","Carnes del Sebastián (SUMAR)","Auxiliar Contable", "Realizar un control exhaustivo del 100% del inventario en la planta de producción y en los 3 puntos de venta, actualizando los registros diariamente. Esto incluye inventario de materias primas, productos en proceso, productos terminados."),
            rx.spacer(spacing="3", direction="row"),
            experiencia("01-2009","12-2015","Proinsalud S.A.", "Coordinador de suministros", "Acompañamiento activo en las actividades logísticas y operativas, optimizando procesos a través de la gestión documental eficiente, elaboración de planes de compras estratégicos, control de inventarios preciso y presentación de informes que permitan la toma de decisiones basadas en datos. Impulsar la mejora continua en los procesos de adquisición de insumos y equipos médicos."),
            #experiencia()
            width=["100%", "100%", "33%"],
            padding="1rem",           
            margin="1rem" 
        ),
        rx.box(
            titulos("ESTUDIOS"),
            estudios("CONTADOR PUBLICO","Fundación Universitaria San Martín"),
            estudios("ESPECIALISTA EN GERENCIA FINANCIERA", "Fundación Universitaria del Area Andina"),
            
            titulos("HOBBIES"),
            rx.spacer(spacing="2", direction="row"),
            hobies("book-open-check", "Leer"),
            hobies("dribbble","Jugar Futbol"),
            hobies("music", "Escuchar música"),
            hobies("code-xml", "Aprender a programar"),
            hobies("dumbbell", "Hacer ejercicio"),
            rx.spacer(height="1rem"),
            
            titulos("ALGUNOS TRABAJOS"),
            rx.vstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            rx.icon("layout-dashboard"),
                            "Power Bi",
                                  variant = "outline",
                                  color_scheme = "gray",
                                  high_contrast = True,
                                  width = ["100%", "50%"]
                                  )
                            ),
                    rx.dialog.content(
                        rx.image(
                            src="/power_bi/gastos.JPG",
                            style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                            }
                        ),
                        rx.image(
                            src="/power_bi/honorarios_cuentas_medicas.JPG",
                            style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                        rx.image(
                            src="/power_bi/Nomina_2.JPG",
                            style={"width": "20%",
                            "max_width": "300px",
                            "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
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
                style = {"display": "flex", "flex_direction": ["column", "row"], "height": "50vh", "width": "50vw"}
            ),
                ),
                rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button(
                                rx.icon("sheet"),
                                "Excel",
                                  variant = "outline",
                                  color_scheme = "gray",
                                  high_contrast = True,
                                  width = ["100%", "50%"]
                                  ),   
                        ),
                        rx.dialog.content(
                          rx.image(
                              src="/excel/excel_1.JPG",
                              style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                              }
                          ),
                          rx.image(
                              src="/excel/excel_2.JPG",
                              style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                              }
                          ),
                          rx.image(
                              src="/excel/excel_3.JPG",
                              style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                                }
                              }
                          ),
                          rx.dialog.close(
                              rx.button("X",
                                        size = "1",
                                        variant="outline",
                                        color_scheme = "red",
                                        high_contrast = False,
                                        width = "2%"
                                    )
                                ),
                          max_width = ["90vw", "900px"],
                          max_height = ["90vh", "900px"],
                          style = {"display": "flex", "flex_direction": "row", "height": "50vh", "width": "50vw"}
                        ),
                    ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            rx.icon("bot"),
                            "Automatizaciones",
                            variant = "outline",
                            color_scheme = "gray",
                            high_contrast = True,
                            width = ["100%", "50%"]
                            )
                        ),
                    rx.dialog.content(
                        rx.image(
                            src="/automatizaciones/26shots_so.webp",
                            style={
                                "width": "20%",
                                "max_width": "300px",
                                "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                        rx.image(
                            src="/automatizaciones/39_1x_shots_so.webp",
                            style={"width": "20%",
                            "max_width": "300px",
                            "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                        rx.image(
                            src="/automatizaciones/64shots_so.webp",
                            style={"width": "20%",
                            "max_width": "300px",
                            "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                        rx.image(
                            src="/automatizaciones/323_1x_shots_so.webp",
                            style={"width": "20%",
                            "max_width": "300px",
                            "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                        rx.image(
                            src="/automatizaciones/913_1x_shots_so.webp",
                            style={"width": "20%",
                            "max_width": "300px",
                            "flex_grow": "1",
                                "object_fit": "cover",
                                "opacity": ".8",
                                "transition": ".5s ease",
                                "_hover": {
                                    "cursor": "crosshair",
                                    "width": "100%",
                                    "opacity": "1",
                                    "filter": "contrast(120%)"
                            }
                        }
                    ),
                rx.dialog.close(
                    rx.button("X",
                    size = "1",
                    variant="outline",
                    color_scheme = "red",
                    high_contrast = False,
                    width = "2%"
                    )
                        ),
                max_width = ["90vw", "900px"],
                max_height = ["90vh", "900px"],
                style = {"display": "flex", "flex_direction": "row", "height": "50vh", "width": "50vw"}
                    ),
                ),
            ),
            width=["100%", "100%", "33%"],
            margin="1rem",
            padding="1rem"    
        ),
    #spacing="1rem",
    flex_direction=["column", "column", "row"],
    width=["100%", "100%", "100%"],
    margin=["0 auto", "0 auto", Size.DEFAULT.value],
    #max_width=["100vw", "1200px"], 
    padding=["0.5rem", "0.5rem", "0.5rem"]
    )