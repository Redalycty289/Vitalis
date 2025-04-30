import flet as ft

def adulto_mayor_page(page: ft.Page):
    page.title = "Registro - Adulto Mayor"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # función para registrar al adulto mayor
    def registrar(e):
        # Verificar campos personales
        personal_fields_filled = all([
            nombres.value, apellidos.value, edad.value, 
            dni.value, direccion.value, telefono.value
        ])
        
        # Verificar campos médicos
        medical_fields_filled = enfermedades.value or alergias.value or medicamentos.value
        
        # Verificar contacto de emergencia
        emergency_fields_filled = all([
            contacto_nombre.value, contacto_telefono.value, contacto_relacion.value
        ])
        
        if personal_fields_filled and emergency_fields_filled:
            mensaje.value = "Registro exitoso"
            mensaje.color = ft.colors.GREEN
            mensaje.update()
            
            # Crear usuario y contraseña automáticamente
            usuario_generado = f"{nombres.value.split()[0].lower()}{dni.value[-4:]}"
            contrasena_generada = f"{apellidos.value.split()[0].lower()}{edad.value}"
            
            # Mostrar credenciales generadas
            credenciales_dialog.content = ft.Column([
                ft.Text("Se han generado sus credenciales de acceso:", size=16),
                ft.Text(f"Usuario: {usuario_generado}", weight=ft.FontWeight.BOLD),
                ft.Text(f"Contraseña: {contrasena_generada}", weight=ft.FontWeight.BOLD),
                ft.Text("Por favor, guarde esta información en un lugar seguro.", size=14, color=ft.colors.RED_400),
                ft.Text("Puede cambiar su contraseña más adelante desde su perfil.", size=14)
            ], spacing=10)
            
            credenciales_dialog.open = True
            page.update()
        else:
            mensaje.value = "Por favor, complete todos los campos obligatorios (*)"
            mensaje.color = ft.colors.RED
            mensaje.update()
    
    # Función para continuar después de mostrar credenciales
    def continuar_menu(e):
        credenciales_dialog.open = False
        page.update()
        
        # Importación tardía para evitar importación circular
        from menu_adulto_mayor import main as menu_adulto_mayor
        # Redirigir al menú principal de adulto mayor
        page.clean()
        menu_adulto_mayor(page)
    
    def volver_seleccion(e):
        # Importación tardía para evitar importación circular
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)
    
    # Función para seleccionar archivos
    def on_file_picked(e):
        if e.files:
            file_names = [file.name for file in e.files]
            archivos_texto.value = f"Archivos seleccionados: {', '.join(file_names)}"
            archivos_texto.update()
    
    # Crear file picker
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    # Título principal
    titulo = ft.Text(
        "Registro de Adulto Mayor", 
        size=28, 
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Sección 1: Información Personal
    seccion_personal = ft.Text(
        "Información Personal", 
        size=20, 
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD
    )
    
    nombres = ft.TextField(
        label="Nombres *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.PERSON
    )
    
    apellidos = ft.TextField(
        label="Apellidos *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.PERSON_OUTLINE
    )
    
    edad = ft.TextField(
        label="Edad *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.CAKE,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    dni = ft.TextField(
        label="DNI/Documento de Identidad *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.BADGE
    )
    
    direccion = ft.TextField(
        label="Dirección *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.HOME
    )
    
    telefono = ft.TextField(
        label="Teléfono *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.PHONE,
        keyboard_type=ft.KeyboardType.PHONE
    )
    
    # Sección 2: Información Médica
    seccion_medica = ft.Text(
        "Información Médica", 
        size=20, 
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD
    )
    
    grupo_sanguineo = ft.Dropdown(
        label="Grupo Sanguíneo",
        width=350,
        options=[
            ft.dropdown.Option("A+"),
            ft.dropdown.Option("A-"),
            ft.dropdown.Option("B+"),
            ft.dropdown.Option("B-"),
            ft.dropdown.Option("AB+"),
            ft.dropdown.Option("AB-"),
            ft.dropdown.Option("O+"),
            ft.dropdown.Option("O-"),
            ft.dropdown.Option("No lo sé")
        ],
        border_color=ft.colors.TEAL,
    )
    
    enfermedades = ft.TextField(
        label="Enfermedades crónicas", 
        width=350, 
        multiline=True,
        min_lines=2,
        max_lines=4,
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.MEDICAL_SERVICES,
        hint_text="Ej: Diabetes, Hipertensión, etc."
    )
    
    alergias = ft.TextField(
        label="Alergias", 
        width=350, 
        multiline=True,
        min_lines=2,
        max_lines=4,
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.WARNING_AMBER,
        hint_text="Ej: Penicilina, Látex, etc."
    )
    
    medicamentos = ft.TextField(
        label="Medicamentos actuales", 
        width=350, 
        multiline=True,
        min_lines=2,
        max_lines=4,
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.MEDICATION,
        hint_text="Ej: Paracetamol 500mg, Losartán 50mg, etc."
    )
    
    # Sección para subir archivos médicos
    archivos_texto = ft.Text("No hay archivos seleccionados", color=ft.colors.GREY)
    
    archivos_medicos = ft.Container(
        content=ft.Column([
            ft.Text(
                "Historial Médico", 
                size=16, 
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "Puede subir documentos médicos relevantes (opcional)",
                size=14,
                color=ft.colors.WHITE
            ),
            ft.ElevatedButton(
                "Seleccionar archivos",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(
                    allow_multiple=True,
                    allowed_extensions=["pdf", "jpg", "jpeg", "png"]
                ),
                bgcolor=ft.colors.WHITE,
                color=ft.colors.TEAL,
            ),
            archivos_texto
        ]),
        bgcolor=ft.colors.TEAL,
        padding=20,
        border_radius=10,
        width=350
    )
    
    # Sección 3: Contacto de Emergencia
    seccion_emergencia = ft.Text(
        "Contacto de Emergencia", 
        size=20, 
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD
    )
    
    contacto_nombre = ft.TextField(
        label="Nombre completo *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.PERSON_SEARCH
    )
    
    contacto_telefono = ft.TextField(
        label="Teléfono *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.PHONE,
        keyboard_type=ft.KeyboardType.PHONE
    )
    
    contacto_relacion = ft.TextField(
        label="Relación/Parentesco *", 
        width=350, 
        border_color=ft.colors.TEAL,
        label_style=ft.TextStyle(color=ft.colors.TEAL),
        prefix_icon=ft.icons.FAMILY_RESTROOM
    )
    
    # Sección 4: Preferencias
    seccion_preferencias = ft.Text(
        "Preferencias", 
        size=20, 
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD
    )
    
    # Opciones de movilidad
    movilidad = ft.Dropdown(
        label="Nivel de movilidad",
        width=350,
        options=[
            ft.dropdown.Option("Completamente independiente"),
            ft.dropdown.Option("Necesita ayuda ocasional"),
            ft.dropdown.Option("Necesita ayuda frecuente"),
            ft.dropdown.Option("Dependiente de silla de ruedas"),
            ft.dropdown.Option("Encamado")
        ],
        border_color=ft.colors.TEAL,
    )
    
    # Opciones de notificaciones
    notificaciones = ft.Checkbox(
        label="Activar notificaciones de medicamentos",
        value=True
    )
    
    recordatorios = ft.Checkbox(
        label="Activar recordatorios de citas médicas",
        value=True
    )
    
    compartir_info = ft.Checkbox(
        label="Compartir información médica con mi médico",
        value=True
    )
    
    # Mensaje de estado
    mensaje = ft.Text("", size=16)
    
    # Botón de registro
    boton_registro = ft.ElevatedButton(
        "Registrarse", 
        bgcolor=ft.colors.TEAL,
        color=ft.colors.WHITE, 
        on_click=registrar, 
        width=200, 
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    
    # Botón para volver a la selección de usuario
    boton_volver = ft.TextButton(
        "Volver a selección de usuario",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_seleccion
    )
    
    # Diálogo para mostrar credenciales generadas
    credenciales_dialog = ft.AlertDialog(
        title=ft.Text("Credenciales de Acceso"),
        content=ft.Column([]),
        actions=[
            ft.ElevatedButton("Continuar", on_click=continuar_menu)
        ],
    )
    
    # Nota informativa
    nota_informativa = ft.Container(
        content=ft.Text(
            "Los campos marcados con * son obligatorios. La información médica proporcionada "
            "será tratada con confidencialidad y solo será accesible por usted y los profesionales "
            "médicos autorizados.",
            size=12,
            color=ft.colors.GREY_700,
            text_align=ft.TextAlign.CENTER
        ),
        padding=10,
        border_radius=5,
        bgcolor=ft.colors.TEAL_50,
        width=350
    )

    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    titulo,
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    # Sección 1: Información Personal
                    seccion_personal,
                    nombres,
                    apellidos,
                    edad,
                    dni,
                    direccion,
                    telefono,
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    # Sección 2: Información Médica
                    seccion_medica,
                    grupo_sanguineo,
                    enfermedades,
                    alergias,
                    medicamentos,
                    archivos_medicos,
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    # Sección 3: Contacto de Emergencia
                    seccion_emergencia,
                    contacto_nombre,
                    contacto_telefono,
                    contacto_relacion,
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    # Sección 4: Preferencias
                    seccion_preferencias,
                    movilidad,
                    notificaciones,
                    recordatorios,
                    compartir_info,
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    nota_informativa,
                    boton_registro,
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
    
    # Agregar el diálogo a la página
    page.dialog = credenciales_dialog
    page.update()

if __name__ == "__main__":
    ft.app(target=adulto_mayor_page)
