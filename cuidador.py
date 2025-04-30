import flet as ft

def cuidador_page(page: ft.Page):
    page.title = "Inicio de Sesión - Cuidadores"
    page.bgcolor = ft.colors.WHITE
    
    def on_submit(e):
        # Validate all fields are filled
        all_filled = all(input_field.value for input_field in inputs)
        
        if all_filled:
            mensaje.value = "Registro exitoso"
            mensaje.color = ft.colors.GREEN
        else:
            mensaje.value = "Por favor, complete todos los campos"
            mensaje.color = ft.colors.RED
        
        mensaje.update()
    
    # Función para seleccionar archivos
    def on_file_picked(e):
        if e.files:
            file_names = [file.name for file in e.files]
            files_text.value = f"Archivos seleccionados: {', '.join(file_names)}"
            files_text.update()
    
    def volver_seleccion(e):
        # Importación tardía para evitar importación circular
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)

    # Create file picker
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)
    
    # Campos del formulario
    form_fields = [
        ("Nombres", "Ingrese sus nombres"),
        ("Apellidos", "Ingrese sus apellidos"),
        ("Edad", "Ingrese su edad"),
        ("Ciudadanía", "Ingrese su ciudadanía"),
        ("Número de Teléfono", "Ingrese su número de teléfono"),
        ("DNI", "Ingrese su DNI"),
        ("Correo Electrónico", "Ingrese su correo electrónico"),
    ]
    
    # Entradas para cada campo
    inputs = []
    for label, hint in form_fields:
        input_field = ft.TextField(
            label=label, 
            hint_text=hint, 
            border_color=ft.colors.PURPLE,
            label_style=ft.TextStyle(color=ft.colors.PURPLE),
            width=350
        )
        inputs.append(input_field)
    
    # Texto para mostrar archivos seleccionados
    files_text = ft.Text("No hay archivos seleccionados", color=ft.colors.GREY)
    
    # Cuadro morado con la opción de subir archivos
    security_box = ft.Container(
        content=ft.Column([
            ft.Text(
                "LA SEGURIDAD ES PRIMERO", 
                size=18, 
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Por favor, suba su identificación oficial y certificado de antecedentes",
                size=14,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER
            ),
            ft.ElevatedButton(
                "Seleccionar archivos",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(
                    allow_multiple=True
                ),
                bgcolor=ft.colors.WHITE,
                color=ft.colors.PURPLE,
            ),
            files_text
        ]),
        bgcolor=ft.colors.PURPLE,
        padding=20,
        border_radius=10,
        width=350
    )
    
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
        on_click=on_submit
    )
    
    # Crear un contenedor para todos los elementos
    main_content = ft.Column(
        [
            ft.Text(
                "Inicio de Sesión - Cuidadores", 
                size=24, 
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=1, color=ft.colors.GREY_400),
            *inputs,  # Agregar todos los campos de entrada
            security_box,  # Agregar el cuadro de seguridad
            submit_button,  # Agregar el botón de inicio de sesión
            mensaje,  # Mensaje de estado
            boton_volver  # Botón para volver
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        width=400,
        scroll=ft.ScrollMode.AUTO,
    )

    # Envolver en un contenedor scrollable para dispositivos móviles
    page.clean()
    page.add(
        ft.Container(
            content=main_content,
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.padding.only(top=20, bottom=20),
        )
    )
    page.scroll = ft.ScrollMode.AUTO
    page.update()

if __name__ == "__main__":
    ft.app(target=cuidador_page)

