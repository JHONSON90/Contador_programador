import reflex as rx

def imagenes_powerBi()->rx.Component:

# class State(rx.State):
#     dialog_1: bool = False
#     dialog_2: bool = False
#     dialog_3: bool = False

#     def toggle_dialog(self, dialog_number: int):
#         if dialog_number == 1:
#             self.dialog_1 = not self.dialog_1
#         elif dialog_number == 2:
#             self.dialog_2 = not self.dialog_2
#         elif dialog_number == 3:
#             self.dialog_3 = not self.dialog_3

    return rx.vstack(
        # Primer diálogo
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button("Muestras Power Bi")
            ),
            rx.dialog.content(
                rx.image(
                    src="/imagen1.jpg",
                    # Efecto hover para ampliar la imagen
                    style={
                        "transition": "width 0.3s ease",
                        "width": "200px",
                        "_hover": {
                            "width": "300px",
                        }
                    }
                ),
                rx.dialog.close(
                    rx.button("Cerrar")
                )
            ),
        ),
        # Segundo diálogo
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button("Abrir Galería 2")
            ),
            rx.dialog.content(
                rx.image(
                    src="/imagen2.jpg",
                    style={
                        "transition": "width 0.3s ease",
                        "width": "200px",
                        "_hover": {
                            "width": "300px",
                        }
                    }
                ),
                rx.dialog.close(
                    rx.button("Cerrar")
                )
            ),
        ),
    )