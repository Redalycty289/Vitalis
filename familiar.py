import flet as ft

def familiar_page(page: ft.Page):
    page.title = "Inicio de Sesión - Familiares"
    page.bgcolor = ft.colors.WHITE
    
    def on_submit(e):
        # Verificar que todos los campos estén completos
        user_fields_filled = all(input_field.value for input_field in user_inputs)
        relative_fields_filled = all(input_field.value for input_field in relative_inputs)
        
        if user_fields_filled and relative_fields_filled:
            mensaje.value = "Registro exitoso"
            mensaje.color = ft.colors.GREEN
            
            # Recopilar datos del familiar para pasarlos al menú
            datos_familiar = {
                "nombres": nombres.value,
                "apellidos": apellidos.value,
                "telefono": telefono.value,
                "correo": correo.value,
                "adulto_mayor": {
                    "nombre": nombre_adulto.value,
                    "dni": dni_adulto.value,
                    "relacion": relacion.value
                }
            }
            
            # Mostrar mensaje de éxito y redirigir al menú de familiares
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Registro exitoso. Accediendo al panel de familiares..."),
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            page.update()
        
            # Redirigir al menú de familiares
            from menu_familiares import menu_familiares_page
            page.clean()
            menu_familiares_page(page, datos_familiar)
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
        "Inicio de Sesión - Familiares", 
        size=28, 
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Campos para información del usuario
    nombres = ft.TextField(
        label="Nombres", 
        hint_text="Ingrese sus nombres", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.PERSON
    )
    
    apellidos = ft.TextField(
        label="Apellidos", 
        hint_text="Ingrese sus apellidos", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.PERSON_OUTLINE
    )
    
    telefono = ft.TextField(
        label="Número de Teléfono", 
        hint_text="Ingrese su número de teléfono", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.PHONE,
        keyboard_type=ft.KeyboardType.PHONE
    )
    
    correo = ft.TextField(
        label="Correo Electrónico", 
        hint_text="Ingrese su correo electrónico", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.EMAIL,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    # Campos para información del adulto mayor
    nombre_adulto = ft.TextField(
        label="Nombre del Adulto Mayor", 
        hint_text="Ingrese el nombre del adulto mayor", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.ELDERLY
    )
    
    dni_adulto = ft.TextField(
        label="DNI del Adulto Mayor", 
        hint_text="Ingrese el DNI del adulto mayor", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.BADGE
    )
    
    relacion = ft.TextField(
        label="Relación", 
        hint_text="Ingrese su relación con el adulto mayor", 
        border_color=ft.colors.BLUE,
        label_style=ft.TextStyle(color=ft.colors.BLUE),
        width=350,
        prefix_icon=ft.icons.FAMILY_RESTROOM
    )
    
    # Agrupar inputs para verificación
    user_inputs = [nombres, apellidos, telefono, correo]
    relative_inputs = [nombre_adulto, dni_adulto, relacion]
    
    # Mensaje de estado
    mensaje = ft.Text("", size=16)
    
    # Botón para volver a la selección de usuario
    boton_volver = ft.TextButton(
        "Volver a selección de usuario",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_seleccion
    )

    # Botón de inicio de sesión
    submit_button = ft.ElevatedButton(
        text="Registrarse", 
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        width=200,
        on_click=on_submit,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    
    # Sección explicativa
    informacion = ft.Container(
        content=ft.Column([
            ft.Text(
                "¿Por qué registrarse como familiar?",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE
            ),
            ft.Text(
                "• Acceda a telemedicina y diagnóstico preliminar",
                size=14,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "• Contrate cuidadores profesionales verificados",
                size=14
            ),
            ft.Text(
                "• Reciba notificaciones sobre medicamentos y citas médicas",
                size=14
            ),
            ft.Text(
                "• Monitoree la actividad diaria del adulto mayor",
                size=14
            ),
            ft.Text(
                "• Comuníquese con médicos y cuidadores",
                size=14
            ),
        ]),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLUE_50,
        border=ft.border.all(1, ft.colors.BLUE_200),
        width=350
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
                    ft.Text("Sus datos", size=18, weight=ft.FontWeight.BOLD),
                    nombres,
                    apellidos,
                    telefono,
                    correo,
                    ft.Divider(height=1, color=ft.colors.GREY_400),
                    ft.Text("Datos del Adulto Mayor", size=18, weight=ft.FontWeight.BOLD),
                    nombre_adulto,
                    dni_adulto,
                    relacion,
                    informacion,
                    submit_button,
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
    ft.app(target=familiar_page)
