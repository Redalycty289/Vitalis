import flet as ft

def main(page: ft.Page):
    page.title = "Menú Principal - Adulto Mayor"
    page.bgcolor = ft.colors.WHITE
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
   
    def navegar(e):
        destino = e.control.data
        if destino == "memoria":
            try:
                # Importación tardía para evitar importación circular
                import juegomemoria
                page.clean()
                juegomemoria.main(page)
            except Exception as e:
                print(f"Error al cargar juego de memoria: {e}")
                page.snack_bar = ft.SnackBar(content=ft.Text(f"Error al cargar: {str(e)}"))
                page.snack_bar.open = True
                page.update()
        elif destino == "relajacion":
            try:
                # Importación tardía para evitar importación circular
                import relajacion
                page.clean()
                relajacion.main(page)
            except Exception as e:
                print(f"Error al cargar relajación: {e}")
                page.snack_bar = ft.SnackBar(content=ft.Text(f"Error al cargar: {str(e)}"))
                page.snack_bar.open = True
                page.update()
        elif destino == "llamadas":
            pantalla_llamadas(page)
        elif destino == "medicamentos":
            # Importación tardía para evitar importación circular
            import medicamentos
            page.clean()
            medicamentos.main(page)
        elif destino == "citas":
            pantalla_citas(page)
    
    # Título y bienvenida
    titulo = ft.Text(
        "¡Bienvenido!",
        size=32,
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    subtitulo = ft.Text(
        "¿Qué desea hacer hoy?",
        size=22,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )
    
    # Crear tarjetas para cada opción del menú
    opciones = [
        {
            "titulo": "Juego de Memoria",
            "descripcion": "Ejercite su mente con juegos divertidos",
            "icono": ft.icons.PSYCHOLOGY,
            "color": "#7b37b9",
            "destino": "memoria"
        },
        {
            "titulo": "Ejercicios de Relajación",
            "descripcion": "Encuentre paz y tranquilidad con ejercicios guiados",
            "icono": ft.icons.SPA,
            "color": "#9C27B0",
            "destino": "relajacion"
        },
        {
            "titulo": "Llamadas Familiares",
            "descripcion": "Mantenga contacto con sus seres queridos",
            "icono": ft.icons.CALL,
            "color": "#2196F3",
            "destino": "llamadas"
        },
        {
            "titulo": "Mis Medicamentos",
            "descripcion": "Gestione sus medicamentos y recordatorios",
            "icono": ft.icons.MEDICATION,
            "color": "#4CAF50",
            "destino": "medicamentos"
        },
        {
            "titulo": "Citas Médicas",
            "descripcion": "Vea sus próximas citas médicas",
            "icono": ft.icons.CALENDAR_TODAY,
            "color": "#FF9800",
            "destino": "citas"
        }
    ]
    
    tarjetas = []
    for opcion in opciones:
        tarjeta = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(opcion["icono"], size=40, color=ft.colors.WHITE),
                    ft.Text(
                        opcion["titulo"],
                        size=20,
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text(
                    opcion["descripcion"],
                    size=16,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            width=300,
            height=150,
            bgcolor=opcion["color"],
            border_radius=10,
            padding=20,
            margin=10,
            ink=True,
            on_click=navegar,
            data=opcion["destino"]
        )
        tarjetas.append(tarjeta)
    
    # Crear grid adaptativo para las tarjetas
    def create_grid(e=None):
        grid.controls = []
        screen_width = page.width or 600
        
        # Determinar número de columnas según ancho de pantalla
        columns = 2
        if screen_width < 600:
            columns = 1
            
        # Dividir tarjetas en filas
        for i in range(0, len(tarjetas), columns):
            row_cards = tarjetas[i:i+columns]
            grid.controls.append(
                ft.Row(
                    controls=row_cards,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True
                )
            )
        page.update()
    
    grid = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        width=page.width if page.width else 600,
    )
    
    # Perfil del usuario
    perfil = ft.Container(
        content=ft.Row([
            ft.CircleAvatar(
                content=ft.Text("AM", size=24, weight=ft.FontWeight.BOLD),
                bgcolor=ft.colors.TEAL,
                radius=30
            ),
            ft.Column([
                ft.Text("Adulto Mayor", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Último acceso: Hoy", size=14, color=ft.colors.GREY_700)
            ])
        ], spacing=15),
        padding=15,
        border_radius=10,
        bgcolor=ft.colors.TEAL_50,
        border=ft.border.all(1, ft.colors.TEAL_200),
        margin=ft.margin.only(bottom=20)
    )
    
    # Botón para cerrar sesión
    def volver_seleccion(e):
        # Importación tardía para evitar importación circular
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)
        
    cerrar_sesion = ft.ElevatedButton(
        "Cerrar Sesión",
        icon=ft.icons.LOGOUT,
        bgcolor=ft.colors.RED_400,
        color=ft.colors.WHITE,
        on_click=volver_seleccion
    )
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                perfil,
                titulo,
                subtitulo,
                ft.Divider(height=2, color=ft.colors.TEAL_200),
                grid,
                cerrar_sesion
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )
    )
    
    # Hacer que el diseño sea responsivo
    page.on_resize = create_grid
    create_grid()  # Inicializar grid

# Funciones para las diferentes pantallas
def pantalla_llamadas(page: ft.Page):
    page.title = "Llamadas Familiares"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Datos de ejemplo para las llamadas
    contactos = [
        {"nombre": "María (Hija)", "ultimo_contacto": "Hace 2 días", "racha": 3, "imagen": None},
        {"nombre": "Juan (Hijo)", "ultimo_contacto": "Hace 5 días", "racha": 1, "imagen": None},
        {"nombre": "Ana (Nieta)", "ultimo_contacto": "Hoy", "racha": 7, "imagen": None},
        {"nombre": "Carlos (Sobrino)", "ultimo_contacto": "Hace 1 semana", "racha": 0, "imagen": None},
    ]
    
    def llamar(e, contacto):
        # Simular una llamada
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Llamando a {contacto['nombre']}..."),
            bgcolor=ft.colors.GREEN
        )
        page.snack_bar.open = True
        page.update()
    
    def volver_menu(e):
        main(page)
    
    # Crear tarjetas de contactos
    lista_contactos = []
    for contacto in contactos:
        # Determinar color según la racha
        color_racha = ft.colors.RED
        if contacto["racha"] >= 3:
            color_racha = ft.colors.ORANGE
        if contacto["racha"] >= 5:
            color_racha = ft.colors.GREEN
            
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.CircleAvatar(
                            content=ft.Text(contacto["nombre"][0], weight=ft.FontWeight.BOLD),
                            bgcolor=ft.colors.BLUE
                        ),
                        title=ft.Text(contacto["nombre"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Último contacto: {contacto['ultimo_contacto']}")
                    ),
                    ft.Row([
                        ft.Text(f"Racha: {contacto['racha']} días", color=color_racha),
                        ft.ElevatedButton(
                            "Llamar",
                            icon=ft.icons.CALL,
                            on_click=lambda e, c=contacto: llamar(e, c),
                            bgcolor=ft.colors.BLUE,
                            color=ft.colors.WHITE
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, padding=15)
                ]),
                width=400,
                padding=10
            )
        )
        lista_contactos.append(tarjeta)
    
    # Título y explicación
    titulo = ft.Text(
        "Llamadas Familiares",
        size=28,
        color=ft.colors.BLUE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    explicacion = ft.Container(
        content=ft.Column([
            ft.Text(
                "¡Mantenga el contacto con sus seres queridos!",
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Cada día que hable con un familiar aumentará su racha de llamadas.",
                size=14,
                text_align=ft.TextAlign.CENTER
            )
        ]),
        padding=15,
        border_radius=10,
        bgcolor=ft.colors.BLUE_50,
        border=ft.border.all(1, ft.colors.BLUE_200),
        margin=10
    )
    
    # Botón para volver al menú
    boton_volver = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                explicacion,
                ft.Divider(height=2, color=ft.colors.BLUE_200),
                *lista_contactos,
                boton_volver
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )
    )

def pantalla_citas(page: ft.Page):
    page.title = "Mis Citas Médicas"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Datos de ejemplo para citas médicas
    citas = [
        {"especialista": "Dr. García - Cardiología", "fecha": "15 de Mayo, 2023", "hora": "10:30", "lugar": "Hospital Central, Consultorio 302"},
        {"especialista": "Dra. Rodríguez - Neurología", "fecha": "22 de Mayo, 2023", "hora": "9:00", "lugar": "Clínica San José, Piso 2"},
        {"especialista": "Dr. Martínez - Geriatría", "fecha": "5 de Junio, 2023", "hora": "11:15", "lugar": "Centro Médico Aurora, Consultorio 105"},
    ]
    
    def ver_detalles(e, cita):
        # Mostrar detalles de la cita
        detalles_dialog.title = ft.Text(cita["especialista"])
        detalles_dialog.content = ft.Column([
            ft.Text(f"Fecha: {cita['fecha']}"),
            ft.Text(f"Hora: {cita['hora']}"),
            ft.Text(f"Lugar: {cita['lugar']}"),
            ft.Text("Notas: Llevar resultados de análisis previos y lista de medicamentos actuales.")
        ], spacing=10)
        detalles_dialog.open = True
        page.update()
    
    def volver_menu(e):
        main(page)
    
    # Diálogo para mostrar detalles de la cita
    detalles_dialog = ft.AlertDialog(
        title=ft.Text(""),
        content=ft.Column([]),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: setattr(detalles_dialog, "open", False))
        ]
    )
    
    # Crear tarjetas de citas
    lista_citas = []
    for cita in citas:
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.CALENDAR_TODAY, color=ft.colors.ORANGE),
                        title=ft.Text(cita["especialista"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"{cita['fecha']} - {cita['hora']}")
                    ),
                    ft.Row([
                        ft.Text(cita["lugar"], size=14, color=ft.colors.GREY_700),
                        ft.TextButton(
                            "Ver detalles",
                            icon=ft.icons.INFO,
                            on_click=lambda e, c=cita: ver_detalles(e, c)
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, padding=15)
                ]),
                width=400
            )
        )
        lista_citas.append(tarjeta)
    
    # Título y explicación
    titulo = ft.Text(
        "Mis Citas Médicas",
        size=28,
        color=ft.colors.ORANGE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    explicacion = ft.Container(
        content=ft.Column([
            ft.Text(
                "Gestione sus próximas citas médicas",
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Vea los detalles de cada cita para estar preparado.",
                size=14,
                text_align=ft.TextAlign.CENTER
            )
        ]),
        padding=15,
        border_radius=10,
        bgcolor=ft.colors.ORANGE_50,
        border=ft.border.all(1, ft.colors.ORANGE_200),
        margin=10
    )
    
    # Botón para volver al menú
    boton_volver = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                explicacion,
                ft.Divider(height=2, color=ft.colors.ORANGE_200),
                *lista_citas,
                boton_volver
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )
    )
    
    # Agregar el diálogo a la página
    page.dialog = detalles_dialog
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

