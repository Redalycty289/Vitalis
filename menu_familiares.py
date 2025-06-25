import flet as ft

def menu_familiares_page(page: ft.Page, datos_familiar=None):
    page.title = "Panel de Familiares"
    page.bgcolor = ft.colors.WHITE
    page.padding = 20
    
    # Habilitar scroll en la página principal
    page.scroll = ft.ScrollMode.AUTO
    
    # Función para navegar a diferentes secciones
    def navegar(e):
        destino = e.control.data
        if destino == "telemedicina":
            from chatbot_diagnostico import chatbot_diagnostico_page
            page.clean()
            chatbot_diagnostico_page(page, datos_familiar)
        elif destino == "marketplace":
            from marketplace_cuidadores import marketplace_page
            page.clean()
            marketplace_page(page, datos_familiar)
        elif destino == "monitoreo":
            pantalla_monitoreo(page, datos_familiar)
        elif destino == "comunicacion":
            pantalla_comunicacion(page, datos_familiar)
    
    # Título y bienvenida personalizada
    nombre_usuario = datos_familiar.get("nombres", "Usuario") if datos_familiar else "Usuario"
    nombre_adulto = datos_familiar.get("adulto_mayor", {}).get("nombre", "Adulto Mayor") if datos_familiar else "Adulto Mayor"
    
    titulo = ft.Text(
        f"¡Bienvenido/a, {nombre_usuario}!",
        size=32,
        color=ft.colors.BLUE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    subtitulo = ft.Text(
        f"Panel de cuidado para {nombre_adulto}",
        size=22,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )
    
    # Crear tarjetas para cada opción del menú
    opciones = [
        {
            "titulo": "Telemedicina",
            "descripcion": "Diagnóstico preliminar y consulta médica virtual",
            "icono": ft.icons.MEDICAL_SERVICES,
            "color": "#E91E63",
            "destino": "telemedicina"
        },
        {
            "titulo": "Contrata a tu Cuidador",
            "descripcion": "Encuentra y contrata cuidadores profesionales certificados",
            "icono": ft.icons.PEOPLE,
            "color": "#2196F3",
            "destino": "marketplace"
        },
        {
            "titulo": "Monitoreo de Salud",
            "descripcion": "Seguimiento de medicamentos y citas médicas",
            "icono": ft.icons.MONITOR_HEART,
            "color": "#4CAF50",
            "destino": "monitoreo"
        },
        {
            "titulo": "Comunicación",
            "descripcion": "Contacto con médicos y cuidadores",
            "icono": ft.icons.CHAT,
            "color": "#FF9800",
            "destino": "comunicacion"
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
                content=ft.Text("FAM", size=24, weight=ft.FontWeight.BOLD),
                bgcolor=ft.colors.BLUE,
                radius=30
            ),
            ft.Column([
                ft.Text(f"{nombre_usuario}", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(f"Cuidando a: {nombre_adulto}", size=14, color=ft.colors.GREY_700),
                ft.Text("Último acceso: Hoy", size=14, color=ft.colors.GREY_700)
            ])
        ], spacing=15),
        padding=15,
        border_radius=10,
        bgcolor=ft.colors.BLUE_50,
        border=ft.border.all(1, ft.colors.BLUE_200),
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
                ft.Divider(height=2, color=ft.colors.BLUE_200),
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
def pantalla_monitoreo(page: ft.Page, datos_familiar):
    page.title = "Monitoreo de Salud"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    nombre_adulto = datos_familiar.get("adulto_mayor", {}).get("nombre", "Adulto Mayor") if datos_familiar else "Adulto Mayor"
    
    # Datos simulados de monitoreo
    medicamentos_pendientes = [
        {"nombre": "Paracetamol", "hora": "14:00", "tomado": False},
        {"nombre": "Losartán", "hora": "20:00", "tomado": True},
        {"nombre": "Vitamina D", "hora": "08:00", "tomado": True}
    ]
    
    proximas_citas = [
        {"especialista": "Dr. García - Cardiología", "fecha": "15 de Mayo", "hora": "10:30"},
        {"especialista": "Dra. Rodríguez - Neurología", "fecha": "22 de Mayo", "hora": "9:00"}
    ]
    
    def volver_menu(e):
        menu_familiares_page(page, datos_familiar)
    
    # Título
    titulo = ft.Text(
        f"Monitoreo de Salud - {nombre_adulto}",
        size=28,
        color=ft.colors.GREEN,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Sección de medicamentos
    medicamentos_cards = []
    for med in medicamentos_pendientes:
        color = ft.colors.GREEN if med["tomado"] else ft.colors.RED_400
        estado = "Tomado" if med["tomado"] else "Pendiente"
        
        card = ft.Card(
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(ft.icons.MEDICATION, color=color),
                    title=ft.Text(med["nombre"], weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(f"Hora: {med['hora']} - Estado: {estado}"),
                    trailing=ft.Icon(
                        ft.icons.CHECK_CIRCLE if med["tomado"] else ft.icons.PENDING,
                        color=color
                    )
                ),
                width=400
            )
        )
        medicamentos_cards.append(card)
    
    # Sección de citas
    citas_cards = []
    for cita in proximas_citas:
        card = ft.Card(
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(ft.icons.CALENDAR_TODAY, color=ft.colors.BLUE),
                    title=ft.Text(cita["especialista"], weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(f"{cita['fecha']} - {cita['hora']}")
                ),
                width=400
            )
        )
        citas_cards.append(card)
    
    # Botón para volver
    boton_volver = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Agregar elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                ft.Divider(height=2, color=ft.colors.GREEN_200),
                ft.Text("Medicamentos de Hoy", size=20, weight=ft.FontWeight.BOLD),
                *medicamentos_cards,
                ft.Divider(height=2, color=ft.colors.BLUE_200),
                ft.Text("Próximas Citas Médicas", size=20, weight=ft.FontWeight.BOLD),
                *citas_cards,
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

def pantalla_comunicacion(page: ft.Page, datos_familiar):
    page.title = "Centro de Comunicación"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    nombre_adulto = datos_familiar.get("adulto_mayor", {}).get("nombre", "Adulto Mayor") if datos_familiar else "Adulto Mayor"
    
    # Datos simulados de contactos
    contactos = [
        {"nombre": "Dr. García", "tipo": "Cardiólogo", "ultimo_contacto": "Hace 2 días", "disponible": True},
        {"nombre": "María López", "tipo": "Cuidadora", "ultimo_contacto": "Hoy", "disponible": True},
        {"nombre": "Dra. Rodríguez", "tipo": "Neuróloga", "ultimo_contacto": "Hace 1 semana", "disponible": False}
    ]
    
    def contactar(e, contacto):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Contactando a {contacto['nombre']}..."),
            bgcolor=ft.colors.BLUE
        )
        page.snack_bar.open = True
        page.update()
    
    def volver_menu(e):
        menu_familiares_page(page, datos_familiar)
    
    # Título
    titulo = ft.Text(
        f"Centro de Comunicación - {nombre_adulto}",
        size=28,
        color=ft.colors.ORANGE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Crear tarjetas de contactos
    contactos_cards = []
    for contacto in contactos:
        color_disponibilidad = ft.colors.GREEN if contacto["disponible"] else ft.colors.GREY_400
        texto_disponibilidad = "Disponible" if contacto["disponible"] else "No disponible"
        
        card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.CircleAvatar(
                            content=ft.Text(contacto["nombre"][0], weight=ft.FontWeight.BOLD),
                            bgcolor=ft.colors.ORANGE
                        ),
                        title=ft.Text(contacto["nombre"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"{contacto['tipo']} - {contacto['ultimo_contacto']}")
                    ),
                    ft.Row([
                        ft.Text(texto_disponibilidad, color=color_disponibilidad),
                        ft.ElevatedButton(
                            "Contactar",
                            icon=ft.icons.CHAT,
                            on_click=lambda e, c=contacto: contactar(e, c),
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            disabled=not contacto["disponible"]
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, padding=15)
                ]),
                width=400
            )
        )
        contactos_cards.append(card)
    
    # Botón para volver
    boton_volver = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Agregar elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                ft.Text("Contactos Médicos y Cuidadores", size=16, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=2, color=ft.colors.ORANGE_200),
                *contactos_cards,
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

if __name__ == "__main__":
    def main(page: ft.Page):
        menu_familiares_page(page)
    
    ft.app(target=main)
