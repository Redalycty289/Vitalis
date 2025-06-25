import flet as ft

def medico_page(page: ft.Page):
    page.title = "Inicio de Sesión - Médico"
    page.bgcolor = ft.colors.WHITE
    
    def login(e):
        # Verificar que todos los campos personales estén completos
        personal_fields_filled = all([
            nombres.value, apellidos.value, edad.value, 
            ciudadania.value, telefono.value, dni.value, correo.value
        ])
        
        # Verificar que todos los campos de ocupación estén completos
        ocupacion_fields_filled = all([
            trabajo.value, ocupacion.value, certificacion.value, organizacion.value
        ])
        
        if personal_fields_filled and ocupacion_fields_filled:
            mensaje.value = "Registro exitoso. Bienvenido al sistema médico."
            mensaje.color = ft.colors.GREEN
            mensaje.update()
            
            # Mostrar mensaje de éxito y opciones
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Registro completado exitosamente. El sistema médico estará disponible próximamente."),
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            page.update()
        else:
            mensaje.value = "Por favor, complete todos los campos"
            mensaje.color = ft.colors.RED
        
        mensaje.update()
  
    def volver_seleccion(e):
        # Importación tardía para evitar importación circular
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)

    # Título principal
    titulo = ft.Text(
        "Inicio de Sesión - Médico", 
        size=24, 
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Campos de datos personales
    nombres = ft.TextField(
        label="Nombres", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE)
    )
    apellidos = ft.TextField(
        label="Apellidos", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE)
    )
    edad = ft.TextField(
        label="Edad", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE),
        keyboard_type=ft.KeyboardType.NUMBER
    )
    ciudadania = ft.TextField(
        label="Ciudadanía", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE)
    )
    telefono = ft.TextField(
        label="Número de Teléfono", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE),
        keyboard_type=ft.KeyboardType.PHONE
    )
    dni = ft.TextField(
        label="DNI", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE)
    )
    correo = ft.TextField(
        label="Correo Electrónico", 
        width=350, 
        border_color=ft.colors.PURPLE,
        label_style=ft.TextStyle(color=ft.colors.PURPLE),
        keyboard_type=ft.KeyboardType.EMAIL
    )

    # Campos de registro de ocupación
    trabajo = ft.TextField(
        label="Lugar de Trabajo", 
        width=330, 
        border_color=ft.colors.BLUE_300
    )
    ocupacion = ft.TextField(
        label="Especialidad médica", 
        width=330, 
        border_color=ft.colors.BLUE_300
    )
    certificacion = ft.TextField(
        label="Número de Certificación", 
        width=330, 
        border_color=ft.colors.BLUE_300
    )
    organizacion = ft.TextField(
        label="Organización médica a la que pertenece", 
        width=330, 
        border_color=ft.colors.BLUE_300
    )

    # Contenedor para el registro de ocupación
    registro_ocupacion = ft.Container(
        content=ft.Column([
            ft.Text(
                "Registro de Ocupación", 
                size=20, 
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            trabajo,
            ocupacion,
            certificacion,
            organizacion,
        ], spacing=15, alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.LIGHT_BLUE_50,
        border=ft.border.all(2, ft.colors.LIGHT_BLUE_300),
        width=350
    )

    # Botón de registro
    boton_login = ft.ElevatedButton(
        "Registrar", 
        bgcolor=ft.colors.TEAL,
        color=ft.colors.WHITE, 
        on_click=login, 
        width=200, 
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    
    # Mensaje de estado
    mensaje = ft.Text("", size=16)

    # Botón para volver a la selección de usuario
    boton_volver = ft.TextButton(
        "Volver a selección de usuario",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_seleccion
    )

    # Make sure the page has scrolling enabled
    page.scroll = ft.ScrollMode.AUTO

    # Wrap the content in a scrollable container
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    titulo, 
                    ft.Divider(height=1, color=ft.colors.GREY_400),
                    ft.Text("Datos Personales", size=18, weight=ft.FontWeight.BOLD),
                    nombres, 
                    apellidos, 
                    edad, 
                    ciudadania, 
                    telefono, 
                    dni, 
                    correo, 
                    registro_ocupacion, 
                    boton_login, 
                    mensaje,
                    boton_volver
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                width=400,
                scroll=ft.ScrollMode.AUTO,
            ),
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.padding.only(top=20, bottom=20),
        )
    )

if __name__ == "__main__":
    ft.app(target=medico_page)
