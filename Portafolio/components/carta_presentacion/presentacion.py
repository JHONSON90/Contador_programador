import reflex as rx
from Portafolio.style.sizes import Size

def componente_carta() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(     
                    rx.heading("Acerca de mi", 
                        font_weight="800",
                        margin_bottom="1.5rem",
                        font_size="4.5rem",
                        line_height="1",
                        color="#ffffff",
                        letter_spacing="-0.05em",
                        as_="h1",
                        align = "center",
                        ),
                        
                    rx.text("Soy un profesional versátil con una sólida formación en contabilidad y una creciente pasión por la tecnología. ",
                            rx.text.strong("Mis 10 años "),
                            " de experiencia en el sector contable me han proporcionado una base sólida en análisis financiero y gestión de costos.", padding_left= Size.BIG.value,
                            width="100%",
                            text_align = "center"
                            ),
                    rx.text("Actualmente, estoy ampliando mis horizontes hacia la ",
                            rx.text.strong("ciencia de datos y el desarrollo web. "),
                            " Esta combinación me permite abordar problemas complejos desde diferentes perspectivas y ofrecer soluciones integrales.", padding_left= Size.BIG.value,
                            width="100%",
                            text_align = "center"
                            ),
                    rx.text("Busco oportunidades donde pueda aplicar mis conocimientos para optimizar procesos, crear herramientas de análisis y desarrollar aplicaciones web que agreguen ",
                            rx.text.strong("valor a las organizaciones y a la sociedad en general."),
                            width="100%",
                            padding_left= Size.BIG.value,
                            text_align = "center"
                            ),
                align="center",
                text_align="center",
                padding = Size.DEFAULT.value,
                margin = Size.DEFAULT.value,
                    ),
        ),
        rx.mobile_and_tablet(
            rx.flex(
                rx.container(height="1em"),
                rx.heading("Acerca de mi!!", align="center"),
                    rx.spacer(),
                rx.text("Soy un profesional versátil con una sólida formación en contabilidad y una creciente pasión por la tecnología. ",
                            rx.text.strong("Mis 10 años "),
                            " de experiencia en el sector contable me han proporcionado una base sólida en análisis financiero y gestión de costos.", padding_left= Size.BIG.value,
                            width="100%"
                            ),
                    rx.spacer(),
                    rx.text("Actualmente, estoy ampliando mis horizontes hacia la ",
                            rx.text.strong("ciencia de datos y el desarrollo web. "),
                            " Esta combinación me permite abordar problemas complejos desde diferentes perspectivas y ofrecer soluciones integrales.", padding_left= Size.BIG.value,
                            width="100%"),
                    rx.spacer(),
                    rx.text("Busco oportunidades donde pueda aplicar mis conocimientos para optimizar procesos, crear herramientas de análisis y desarrollar aplicaciones web que agreguen ",
                            rx.text.strong("valor a las organizaciones y a la sociedad en general."),
                            width="100%",
                            padding_left= Size.BIG.value
                            ),   
                    text_align="center",
                    padding= Size.BIG.value,
                    wrap= "nowrap",
                    align="center",
                    justify="center",
                    direction="column"
                ),
        ), 
       
    )
    
