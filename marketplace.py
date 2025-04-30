import flet as ft
import random
from menu_adulto_mayor import main as menu_principal

def marketplace_page(page: ft.Page, datos_familiar=None):
    page.title = "Marketplace de Cuidadores"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Función para volver a la selección de usuario
    def volver_seleccion(e):
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)
    
    # Datos de ejemplo para cuidadores
    cuidadores = [
        {
            "id": 1,
            "nombre": "María López",
            "edad": 35,
            "especialidad": "Enfermería geriátrica",
            "experiencia": "8 años",
            "calificacion": 4.8,
            "precio": "$25/hora",
            "descripcion": "Enfermera profesional con especialidad en cuidado de adultos mayores. Experiencia en manejo de pacientes con Alzheimer y Parkinson.",
            "comentarios": [
                {"usuario": "Juan Pérez", "texto": "Excelente atención y muy puntual.", "calificacion": 5},
                {"usuario": "Ana Gómez", "texto": "Muy profesional y cariñosa con mi padre.", "calificacion": 5},
                {"usuario": "Carlos Ruiz", "texto": "Buena atención, pero a veces llega tarde.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Viernes, 8:00 - 18:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.BLUE_100
        },
        {
            "id": 2,
            "nombre": "Roberto Sánchez",
            "edad": 42,
            "especialidad": "Fisioterapia",
            "experiencia": "12 años",
            "calificacion": 4.5,
            "precio": "$30/hora",
            "descripcion": "Fisioterapeuta especializado en rehabilitación de adultos mayores. Experiencia en recuperación post-operatoria y movilidad reducida.",
            "comentarios": [
                {"usuario": "Marta Silva", "texto": "Excelente trabajo con la rehabilitación de mi madre.", "calificacion": 5},
                {"usuario": "Pedro Díaz", "texto": "Muy profesional, pero sus sesiones son algo cortas.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Sábado, 9:00 - 20:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.GREEN_100
        },
        {
            "id": 3,
            "nombre": "Carmen Rodríguez",
            "edad": 38,
            "especialidad": "Cuidado general",
            "experiencia": "6 años",
            "calificacion": 4.9,
            "precio": "$22/hora",
            "descripcion": "Cuidadora con amplia experiencia en acompañamiento y asistencia en actividades diarias. Especializada en cuidado nocturno y pacientes con demencia.",
            "comentarios": [
                {"usuario": "Laura Torres", "texto": "Carmen es como de la familia, mi madre la adora.", "calificacion": 5},
                {"usuario": "Miguel Ángel", "texto": "Muy atenta y dedicada, siempre pendiente de todo.", "calificacion": 5},
                {"usuario": "Sofía Martín", "texto": "Excelente trato y muy responsable.", "calificacion": 5}
            ],
            "disponibilidad": "Todos los días, turnos de 12 horas",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.PURPLE_100
        },
        {
            "id": 4,
            "nombre": "Javier Morales",
            "edad": 45,
            "especialidad": "Enfermería y primeros auxilios",
            "experiencia": "15 años",
            "calificacion": 4.7,
            "precio": "$28/hora",
            "descripcion": "Enfermero con experiencia en hospitales y cuidado domiciliario. Especializado en manejo de medicamentos y control de enfermedades crónicas.",
            "comentarios": [
                {"usuario": "Elena Vega", "texto": "Muy profesional y meticuloso con los medicamentos.", "calificacion": 5},
                {"usuario": "Ricardo Flores", "texto": "Excelente atención, aunque a veces es muy estricto.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Viernes, turnos de 8 horas",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.AMBER_100
        },
        {
            "id": 5,
            "nombre": "Lucía Fernández",
            "edad": 32,
            "especialidad": "Terapia ocupacional",
            "experiencia": "5 años",
            "calificacion": 4.6,
            "precio": "$26/hora",
            "descripcion": "Terapeuta ocupacional especializada en mantener la autonomía de adultos mayores. Experiencia en actividades cognitivas y motricidad fina.",
            "comentarios": [
                {"usuario": "Daniel Castro", "texto": "Ha ayudado mucho a mi padre a mantenerse activo.", "calificacion": 5},
                {"usuario": "Isabel Ramos", "texto": "Muy creativa con las actividades, mi madre ha mejorado mucho.", "calificacion": 5},
                {"usuario": "Fernando Gil", "texto": "Buena profesional, aunque a veces las actividades son repetitivas.", "calificacion": 4}
            ],
            "disponibilidad": "Martes a Sábado, 10:00 - 18:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.TEAL_100
        }
    ]
    
    # Título principal
    titulo = ft.Text(
        "Marketplace de Cuidadores",
        size=32,
        color=ft.colors.BLUE_700,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Subtítulo con bienvenida personalizada si hay datos del familiar
    subtitulo_texto = "Encuentra el cuidador ideal para tu ser querido"
    if datos_familiar and datos_familiar.get("nombres"):
        subtitulo_texto = f"Bienvenido/a, {datos_familiar['nombres']}! {subtitulo_texto}"
    
    subtitulo = ft.Text(
        subtitulo_texto,
        size=18,
        color=ft.colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )
    
    # Función para mostrar detalles del cuidador
    def mostrar_detalles(e, cuidador):
        # Crear estrellas para la calificación
        estrellas = ft.Row(spacing=0)
        for i in range(5):
            if i < int(cuidador["calificacion"]):
                estrellas.controls.append(ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=20))
            elif i < cuidador["calificacion"]:  # Para medias estrellas
                estrellas.controls.append(ft.Icon(ft.icons.STAR_HALF, color=ft.colors.AMBER, size=20))
            else:
                estrellas.controls.append(ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER, size=20))
        
        # Crear lista de comentarios
        comentarios_lista = ft.Column(spacing=10)
        for comentario in cuidador["comentarios"]:
            comentario_estrellas = ft.Row(spacing=0)
            for i in range(5):
                if i < comentario["calificacion"]:
                    comentario_estrellas.controls.append(ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=16))
                else:
                    comentario_estrellas.controls.append(ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER, size=16))
            
            comentario_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(comentario["usuario"], weight=ft.FontWeight.BOLD),
                        comentario_estrellas
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text(comentario["texto"])
                ]),
                padding=10,
                border_radius=5,
                bgcolor=ft.colors.GREY_100
            )
            comentarios_lista.controls.append(comentario_card)
        
        # Crear contenido del diálogo
        detalles_content = ft.Column([
            ft.Row([
                ft.Image(src=cuidador["imagen"], width=120, height=120, fit=ft.ImageFit.COVER, border_radius=ft.border_radius.all(60)),
                ft.Column([
                    ft.Text(cuidador["nombre"], size=24, weight=ft.FontWeight.BOLD),
                    ft.Row([estrellas, ft.Text(f"{cuidador['calificacion']}/5", weight=ft.FontWeight.BOLD)]),
                    ft.Text(f"Especialidad: {cuidador['especialidad']}", size=16),
                    ft.Text(f"Experiencia: {cuidador['experiencia']}", size=16),
                    ft.Text(f"Precio: {cuidador['precio']}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
                ], spacing=5)
            ]),
            ft.Divider(),
            ft.Text("Descripción", weight=ft.FontWeight.BOLD, size=18),
            ft.Text(cuidador["descripcion"]),
            ft.Divider(),
            ft.Text("Disponibilidad", weight=ft.FontWeight.BOLD, size=18),
            ft.Text(cuidador["disponibilidad"]),
            ft.Divider(),
            ft.Text("Comentarios y Valoraciones", weight=ft.FontWeight.BOLD, size=18),
            comentarios_lista
        ], scroll=ft.ScrollMode.AUTO, spacing=15)
        
        # Función para contratar
        def contratar_cuidador(e, cuidador_id):
            # Aquí iría la lógica para contratar al cuidador
            dialogo_detalles.open = False
            
            # Mostrar mensaje de confirmación
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Has contratado a {cuidador['nombre']}. Te contactaremos pronto para coordinar detalles."),
                bgcolor=ft.colors.GREEN_700,
                action="OK"
            )
            page.snack_bar.open = True
            page.update()
        
        # Crear diálogo de detalles
        dialogo_detalles = ft.AlertDialog(
            title=ft.Text("Detalles del Cuidador"),
            content=detalles_content,
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: setattr(dialogo_detalles, "open", False)),
                ft.ElevatedButton(
                    "Contratar",
                    bgcolor=ft.colors.BLUE_700,
                    color=ft.colors.WHITE,
                    on_click=lambda e, id=cuidador["id"]: contratar_cuidador(e, id)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        page.dialog = dialogo_detalles
        dialogo_detalles.open = True
        page.update()
    
    # Función para filtrar cuidadores
    def filtrar_cuidadores(e):
        texto_busqueda = busqueda.value.lower() if busqueda.value else ""
        especialidad_seleccionada = filtro_especialidad.value
        
        # Filtrar por texto de búsqueda y especialidad
        cuidadores_filtrados = cuidadores
        if texto_busqueda:
            cuidadores_filtrados = [c for c in cuidadores_filtrados if 
                                   texto_busqueda in c["nombre"].lower() or 
                                   texto_busqueda in c["especialidad"].lower() or 
                                   texto_busqueda in c["descripcion"].lower()]
        
        if especialidad_seleccionada and especialidad_seleccionada != "Todas":
            cuidadores_filtrados = [c for c in cuidadores_filtrados if 
                                   c["especialidad"] == especialidad_seleccionada]
        
        # Actualizar la lista de cuidadores
        actualizar_lista_cuidadores(cuidadores_filtrados)
    
    # Campo de búsqueda
    busqueda = ft.TextField(
        label="Buscar por nombre o especialidad",
        prefix_icon=ft.icons.SEARCH,
        on_change=filtrar_cuidadores,
        width=400
    )
    
    # Filtro de especialidad
    especialidades = ["Todas"] + list(set([c["especialidad"] for c in cuidadores]))
    filtro_especialidad = ft.Dropdown(
        label="Filtrar por especialidad",
        options=[ft.dropdown.Option(especialidad) for especialidad in especialidades],
        value="Todas",
        on_change=filtrar_cuidadores,
        width=300
    )
    
    # Contenedor para la lista de cuidadores
    lista_cuidadores = ft.Column(spacing=15)
    
    # Función para actualizar la lista de cuidadores
    def actualizar_lista_cuidadores(cuidadores_mostrados):
        lista_cuidadores.controls = []
        
        if not cuidadores_mostrados:
            lista_cuidadores.controls.append(
                ft.Container(
                    content=ft.Text(
                        "No se encontraron cuidadores con los criterios seleccionados",
                        text_align=ft.TextAlign.CENTER,
                        size=16
                    ),
                    padding=20
                )
            )
        
        for cuidador in cuidadores_mostrados:
            # Crear estrellas para la calificación
            estrellas = ft.Row(spacing=0)
            for i in range(5):
                if i < int(cuidador["calificacion"]):
                    estrellas.controls.append(ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=16))
                elif i < cuidador["calificacion"]:  # Para medias estrellas
                    estrellas.controls.append(ft.Icon(ft.icons.STAR_HALF, color=ft.colors.AMBER, size=16))
                else:
                    estrellas.controls.append(ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER, size=16))
            
            # Crear tarjeta de cuidador
            tarjeta = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Container(
                                content=ft.Image(
                                    src=cuidador["imagen"],
                                    width=80,
                                    height=80,
                                    fit=ft.ImageFit.COVER,
                                    border_radius=ft.border_radius.all(40)
                                ),
                                margin=ft.margin.only(right=15)
                            ),
                            ft.Column([
                                ft.Text(cuidador["nombre"], size=18, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Especialidad: {cuidador['especialidad']}", size=14),
                                ft.Row([
                                    estrellas,
                                    ft.Text(f"{cuidador['calificacion']}/5", size=14, weight=ft.FontWeight.BOLD)
                                ]),
                                ft.Text(f"Precio: {cuidador['precio']}", size=14, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
                            ], spacing=5, expand=True),
                            ft.Column([
                                ft.ElevatedButton(
                                    "Ver detalles",
                                    icon=ft.icons.INFO,
                                    on_click=lambda e, c=cuidador: mostrar_detalles(e, c),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                    ),
                                ),
                                ft.ElevatedButton(
                                    "Contratar",
                                    icon=ft.icons.CHECK_CIRCLE,
                                    bgcolor=ft.colors.BLUE_700,
                                    color=ft.colors.WHITE,
                                    on_click=lambda e, c=cuidador: mostrar_detalles(e, c),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                    ),
                                )
                            ], spacing=5)
                        ]),
                        ft.Container(
                            content=ft.Text(
                                cuidador["descripcion"][:100] + "..." if len(cuidador["descripcion"]) > 100 else cuidador["descripcion"],
                                size=14
                            ),
                            margin=ft.margin.only(top=10)
                        )
                    ]),
                    padding=15,
                    bgcolor=cuidador["color"]
                ),
                elevation=2
            )
            lista_cuidadores.controls.append(tarjeta)
        
        page.update()
    
    # Botón para volver
    boton_volver = ft.ElevatedButton(
        "Volver a selección de usuario",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_seleccion
    )
    
    # Inicializar la lista de cuidadores
    actualizar_lista_cuidadores(cuidadores)
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                subtitulo,
                ft.Divider(height=2, color=ft.colors.BLUE_200),
                ft.Row([
                    busqueda,
                    filtro_especialidad
                ], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=20),
                lista_cuidadores,
                boton_volver
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )
    )

if __name__ == "__main__":
    def main(page: ft.Page):
        marketplace_page(page)
    
    ft.app(target=main)
