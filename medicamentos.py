import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Mis Medicamentos"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Lista de medicamentos (simulando una base de datos)
    medicamentos = [
        {"id": 1, "nombre": "Paracetamol", "dosis": "500mg", "frecuencia": "Cada 8 horas", "hora": "8:00, 16:00, 00:00", "color": ft.colors.RED, "tomado_hoy": False},
        {"id": 2, "nombre": "Losartán", "dosis": "50mg", "frecuencia": "Una vez al día", "hora": "9:00", "color": ft.colors.BLUE, "tomado_hoy": False},
        {"id": 3, "nombre": "Vitamina D", "dosis": "1000 UI", "frecuencia": "Una vez al día", "hora": "8:00", "color": ft.colors.YELLOW, "tomado_hoy": True},
        {"id": 4, "nombre": "Aspirina", "dosis": "100mg", "frecuencia": "Una vez al día", "hora": "20:00", "color": ft.colors.ORANGE, "tomado_hoy": False},
    ]
    
    # Función para volver al menú principal
    def volver_menu(e):
        from menu_adulto_mayor import main as menu_principal
        page.clean()
        menu_principal(page)
    
    # Función para marcar medicamento como tomado
    def marcar_tomado(e, med_id):
        for med in medicamentos:
            if med["id"] == med_id:
                med["tomado_hoy"] = not med["tomado_hoy"]
                mensaje = f"¡{med['nombre']} marcado como {'tomado' if med['tomado_hoy'] else 'no tomado'}!"
                color = ft.colors.GREEN if med["tomado_hoy"] else ft.colors.RED
                
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=color
                )
                page.snack_bar.open = True
                actualizar_lista_medicamentos()
                break
        page.update()
    
    # Función para eliminar medicamento
    def eliminar_medicamento(e, med_id):
        # Mostrar diálogo de confirmación
        def confirmar_eliminacion(e):
            nonlocal medicamentos
            medicamentos = [med for med in medicamentos if med["id"] != med_id]
            dialogo_confirmacion.open = False
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Medicamento eliminado correctamente"),
                bgcolor=ft.colors.RED_400
            )
            page.snack_bar.open = True
            actualizar_lista_medicamentos()
            page.update()
        
        def cancelar_eliminacion(e):
            dialogo_confirmacion.open = False
            page.update()
        
        # Obtener nombre del medicamento
        nombre_med = next((med["nombre"] for med in medicamentos if med["id"] == med_id), "")
        
        # Diálogo de confirmación
        dialogo_confirmacion = ft.AlertDialog(
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text(f"¿Está seguro que desea eliminar {nombre_med}?"),
            actions=[
                ft.TextButton("Cancelar", on_click=cancelar_eliminacion),
                ft.ElevatedButton(
                    "Eliminar", 
                    on_click=confirmar_eliminacion,
                    bgcolor=ft.colors.RED_400,
                    color=ft.colors.WHITE
                )
            ]
        )
        
        page.dialog = dialogo_confirmacion
        dialogo_confirmacion.open = True
        page.update()
    
    # Función para agregar nuevo medicamento
    def mostrar_form_nuevo_med(e):
        # Limpiar campos del formulario
        nombre_input.value = ""
        dosis_input.value = ""
        frecuencia_dropdown.value = "Una vez al día"
        hora_input.value = ""
        
        dialogo_nuevo_med.open = True
        page.update()
    
    def agregar_medicamento(e):
        if not nombre_input.value or not dosis_input.value or not hora_input.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor complete todos los campos"),
                bgcolor=ft.colors.RED_400
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # Generar ID único (en una aplicación real usaríamos una base de datos)
        nuevo_id = max([med["id"] for med in medicamentos], default=0) + 1
        
        # Asignar color aleatorio
        colores = [ft.colors.RED, ft.colors.BLUE, ft.colors.GREEN, ft.colors.PURPLE, 
                  ft.colors.ORANGE, ft.colors.TEAL, ft.colors.PINK]
        import random
        color_aleatorio = random.choice(colores)
        
        # Crear nuevo medicamento
        nuevo_med = {
            "id": nuevo_id,
            "nombre": nombre_input.value,
            "dosis": dosis_input.value,
            "frecuencia": frecuencia_dropdown.value,
            "hora": hora_input.value,
            "color": color_aleatorio,
            "tomado_hoy": False
        }
        
        # Agregar a la lista
        medicamentos.append(nuevo_med)
        
        # Cerrar diálogo y actualizar lista
        dialogo_nuevo_med.open = False
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Medicamento agregado correctamente"),
            bgcolor=ft.colors.GREEN
        )
        page.snack_bar.open = True
        actualizar_lista_medicamentos()
        page.update()
    
    # Crear tarjetas de medicamentos
    def crear_tarjeta_medicamento(med):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.Container(
                            width=40,
                            height=40,
                            bgcolor=med["color"],
                            border_radius=40,
                            alignment=ft.alignment.center,
                            content=ft.Icon(ft.icons.MEDICATION, color=ft.colors.WHITE)
                        ),
                        title=ft.Text(med["nombre"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"{med['dosis']} - {med['frecuencia']}"),
                        trailing=ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.colors.RED_400,
                            tooltip="Eliminar medicamento",
                            on_click=lambda e, id=med["id"]: eliminar_medicamento(e, id)
                        )
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"Horario: {med['hora']}", size=14),
                            ft.Row([
                                ft.Text(
                                    "Estado: " + ("Tomado hoy" if med["tomado_hoy"] else "Pendiente"), 
                                    color=ft.colors.GREEN if med["tomado_hoy"] else ft.colors.RED_400
                                ),
                                ft.ElevatedButton(
                                    "Marcar como " + ("no tomado" if med["tomado_hoy"] else "tomado"),
                                    icon=ft.icons.CHECK if not med["tomado_hoy"] else ft.icons.CLOSE,
                                    on_click=lambda e, id=med["id"]: marcar_tomado(e, id),
                                    bgcolor=ft.colors.GREEN if not med["tomado_hoy"] else ft.colors.RED_400,
                                    color=ft.colors.WHITE
                                )
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ]),
                        padding=ft.padding.only(left=15, right=15, bottom=15)
                    )
                ]),
                width=400
            ),
            margin=10
        )
    
    # Actualizar lista de medicamentos
    def actualizar_lista_medicamentos():
        lista_med.controls = []
        for med in medicamentos:
            lista_med.controls.append(crear_tarjeta_medicamento(med))
        
        # Mostrar mensaje si no hay medicamentos
        if not medicamentos:
            lista_med.controls.append(
                ft.Container(
                    content=ft.Text(
                        "No tiene medicamentos registrados. Agregue uno nuevo con el botón +",
                        text_align=ft.TextAlign.CENTER,
                        size=16,
                        color=ft.colors.GREY_700
                    ),
                    padding=20
                )
            )
        
        page.update()
    
    # Campos para agregar nuevo medicamento
    nombre_input = ft.TextField(
        label="Nombre del medicamento",
        width=400,
        border_color=ft.colors.GREEN
    )
    
    dosis_input = ft.TextField(
        label="Dosis",
        width=400,
        border_color=ft.colors.GREEN,
        helper_text="Ejemplo: 500mg, 1 pastilla, 5ml, etc."
    )
    
    frecuencia_dropdown = ft.Dropdown(
        label="Frecuencia",
        width=400,
        options=[
            ft.dropdown.Option("Una vez al día"),
            ft.dropdown.Option("Cada 8 horas"),
            ft.dropdown.Option("Cada 12 horas"),
            ft.dropdown.Option("Cada semana"),
            ft.dropdown.Option("Cuando sea necesario")
        ],
        border_color=ft.colors.GREEN
    )
    
    hora_input = ft.TextField(
        label="Horario",
        width=400,
        border_color=ft.colors.GREEN,
        helper_text="Ejemplo: 8:00, 14:00, 20:00"
    )
    
    # Diálogo para agregar nuevo medicamento
    dialogo_nuevo_med = ft.AlertDialog(
        title=ft.Text("Agregar nuevo medicamento"),
        content=ft.Column([
            nombre_input,
            dosis_input,
            frecuencia_dropdown,
            hora_input
        ], 
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        height=300 if page.height < 600 else None,  # Altura máxima en pantallas pequeñas
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: setattr(dialogo_nuevo_med, "open", False)),
            ft.ElevatedButton(
                "Agregar", 
                on_click=agregar_medicamento,
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE
            )
        ],
    )
    
    # Contenedor para la lista de medicamentos
    lista_med = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO
    )
    
    # Título y explicación
    titulo = ft.Text(
        "Mis Medicamentos",
        size=28,
        color=ft.colors.GREEN,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Fecha actual
    fecha_actual = datetime.datetime.now().strftime("%d de %B, %Y")
    subtitulo = ft.Text(
        f"Hoy es {fecha_actual}",
        size=16,
        color=ft.colors.GREY_700,
        text_align=ft.TextAlign.CENTER
    )
    
    explicacion = ft.Container(
        content=ft.Column([
            ft.Text(
                "Gestione sus medicamentos diarios",
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Agregue, elimine o marque como tomados sus medicamentos.",
                size=14,
                text_align=ft.TextAlign.CENTER
            )
        ]),
        padding=15,
        border_radius=10,
        bgcolor=ft.colors.GREEN_50,
        border=ft.border.all(1, ft.colors.GREEN_200),
        margin=10
    )
    
    # Botón para volver al menú
    boton_volver = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Botón flotante para agregar medicamento
    boton_agregar = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREEN,
        on_click=mostrar_form_nuevo_med
    )
    
    # Inicializar lista de medicamentos
    actualizar_lista_medicamentos()
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                subtitulo,
                explicacion,
                ft.Divider(height=2, color=ft.colors.GREEN_200),
                lista_med,
                boton_volver
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=ft.padding.only(bottom=80, left=20, right=20, top=20)  # Espacio para el FAB
        )
    )
    
    # Agregar botón flotante
    page.floating_action_button = boton_agregar
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
