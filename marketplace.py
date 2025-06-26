import flet as ft
import random
from menu_adulto_mayor import main as menu_principal

def marketplace_page(page: ft.Page, datos_familiar=None):
    page.title = "Contrata a tu Cuidador"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Plan seleccionado por defecto
    plan_seleccionado = "estandar"
    
    # Función para volver a la selección de usuario
    def volver_seleccion(e):
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)
    
    # Función para volver al menú de familiares
    def volver_menu_familiares(e):
        from menu_familiares import menu_familiares_page
        page.clean()
        menu_familiares_page(page, datos_familiar)
    
    # Datos de ejemplo para cuidadores con rangos
    cuidadores = [
        # CUIDADORES ESTÁNDAR
        {
            "id": 1,
            "nombre": "Dr. Martín González",
            "edad": 45,
            "especialidad": "Geriatría General",
            "experiencia": "10 años",
            "calificacion": 4.5,
            "precio": "$20/hora",
            "descripcion": "Geriatra general con amplia experiencia en cuidado integral de adultos mayores. Especializado en atención básica y seguimiento médico.",
            "comentarios": [
                {"usuario": "María Pérez", "texto": "Muy profesional y atento con mi padre.", "calificacion": 5},
                {"usuario": "Carlos Ruiz", "texto": "Buen cuidado general, recomendado.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Viernes, 8:00 - 18:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.BLUE_100,
            "rango": "estandar",
            "vitalis": False
        },
        
        # CUIDADORES PREMIUM
        {
            "id": 2,
            "nombre": "María López",
            "edad": 35,
            "especialidad": "Enfermería Geriátrica",
            "experiencia": "8 años",
            "calificacion": 4.8,
            "precio": "$30/hora",
            "descripcion": "Enfermera profesional con especialidad en cuidado de adultos mayores. Experiencia en manejo de pacientes con Alzheimer y Parkinson.",
            "comentarios": [
                {"usuario": "Juan Pérez", "texto": "Excelente atención y muy puntual.", "calificacion": 5},
                {"usuario": "Ana Gómez", "texto": "Muy profesional y cariñosa con mi padre.", "calificacion": 5},
                {"usuario": "Carlos Ruiz", "texto": "Buena atención, pero a veces llega tarde.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Viernes, 8:00 - 18:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.GREEN_100,
            "rango": "premium",
            "vitalis": False
        },
        {
            "id": 3,
            "nombre": "Roberto Sánchez",
            "edad": 42,
            "especialidad": "Fisioterapia Geriátrica",
            "experiencia": "12 años",
            "calificacion": 4.5,
            "precio": "$35/hora",
            "descripcion": "Fisioterapeuta especializado en rehabilitación de adultos mayores. Experiencia en recuperación post-operatoria y movilidad reducida.",
            "comentarios": [
                {"usuario": "Marta Silva", "texto": "Excelente trabajo con la rehabilitación de mi madre.", "calificacion": 5},
                {"usuario": "Pedro Díaz", "texto": "Muy profesional, pero sus sesiones son algo cortas.", "calificacion": 4}
            ],
            "disponibilidad": "Lunes a Sábado, 9:00 - 20:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.ORANGE_100,
            "rango": "premium",
            "vitalis": False
        },
        {
            "id": 4,
            "nombre": "Carmen Rodríguez",
            "edad": 38,
            "especialidad": "Cuidado Psicológico",
            "experiencia": "6 años",
            "calificacion": 4.9,
            "precio": "$32/hora",
            "descripcion": "Psicóloga especializada en adultos mayores. Experiencia en terapia cognitiva y manejo de depresión y ansiedad en la tercera edad.",
            "comentarios": [
                {"usuario": "Laura Torres", "texto": "Carmen ha ayudado mucho a mi madre emocionalmente.", "calificacion": 5},
                {"usuario": "Miguel Ángel", "texto": "Muy empática y profesional.", "calificacion": 5}
            ],
            "disponibilidad": "Martes a Sábado, 10:00 - 18:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.PURPLE_100,
            "rango": "premium",
            "vitalis": False
        },
        
        # CUIDADORES PREMIUM VITALIS
        {
            "id": 5,
            "nombre": "Dr. Javier Morales",
            "edad": 45,
            "especialidad": "Enfermería Avanzada Vitalis",
            "experiencia": "15 años",
            "calificacion": 4.9,
            "precio": "$45/hora",
            "descripcion": "Enfermero certificado Vitalis con capacitación avanzada en administración de medicamentos y cuidados especializados. Autorizado para aplicar inyecciones y manejar equipos médicos.",
            "comentarios": [
                {"usuario": "Elena Vega", "texto": "Increíble profesional, puede hacer todo lo que necesita mi padre.", "calificacion": 5},
                {"usuario": "Ricardo Flores", "texto": "Vale cada peso, es como tener un médico en casa.", "calificacion": 5}
            ],
            "disponibilidad": "Todos los días, turnos de 12 horas",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.AMBER_100,
            "rango": "premium_vitalis",
            "vitalis": True
        },
        {
            "id": 6,
            "nombre": "Lucía Fernández",
            "edad": 32,
            "especialidad": "Terapia Integral Vitalis",
            "experiencia": "8 años",
            "calificacion": 4.8,
            "precio": "$42/hora",
            "descripcion": "Terapeuta certificada Vitalis con formación en fisioterapia, terapia ocupacional y administración de medicamentos. Especializada en cuidados integrales y rehabilitación avanzada.",
            "comentarios": [
                {"usuario": "Daniel Castro", "texto": "Lucía es excepcional, maneja todo tipo de cuidados.", "calificacion": 5},
                {"usuario": "Isabel Ramos", "texto": "La mejor inversión para el cuidado de mi madre.", "calificacion": 5}
            ],
            "disponibilidad": "Lunes a Sábado, 8:00 - 20:00",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.TEAL_100,
            "rango": "premium_vitalis",
            "vitalis": True
        },
        {
            "id": 7,
            "nombre": "Ana Patricia Ruiz",
            "edad": 40,
            "especialidad": "Cuidados Médicos Vitalis",
            "experiencia": "12 años",
            "calificacion": 4.9,
            "precio": "$48/hora",
            "descripcion": "Enfermera Vitalis con certificación en cuidados intensivos domiciliarios. Capacitada para manejar ventiladores, sondas, y administrar medicamentos complejos. Monitoreo 24/7.",
            "comentarios": [
                {"usuario": "Fernando Gil", "texto": "Ana salvó la vida de mi padre, increíble profesional.", "calificacion": 5},
                {"usuario": "Carmen López", "texto": "Nivel hospitalario en casa, excelente servicio.", "calificacion": 5}
            ],
            "disponibilidad": "Disponible 24/7, turnos flexibles",
            "imagen": "/placeholder.svg?height=150&width=150",
            "color": ft.colors.PINK_100,
            "rango": "premium_vitalis",
            "vitalis": True
        }
    ]
    
    # Título principal
    titulo = ft.Text(
        "Contrata a tu Cuidador",
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
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )
    
    # Descripción de planes
    descripciones_plan = {
        "estandar": "Acceso a cuidadores con formación en geriatría general.",
        "premium": "Acceso a todos los especialistas: enfermeros, fisioterapeutas, psicólogos especializados.",
        "premium_vitalis": "Acceso completo + Cuidadores Vitalis certificados que pueden administrar medicamentos y brindar cuidados médicos avanzados."
    }

    # Función para cambiar plan
    def cambiar_plan(e):
        nonlocal plan_seleccionado
        plan_seleccionado = e.control.data
        actualizar_lista_cuidadores()
        actualizar_botones_plan()
        actualizar_descripcion_plan()

    # Nueva función para actualizar descripción
    def actualizar_descripcion_plan():
        descripcion_plan_container.content.value = descripciones_plan[plan_seleccionado]
        page.update()
    
    # Función para actualizar botones de plan
    def actualizar_botones_plan():
        for btn in botones_plan:
            if btn.data == plan_seleccionado:
                btn.bgcolor = ft.colors.BLUE_700
                btn.color = ft.colors.WHITE
            else:
                btn.bgcolor = ft.colors.GREY_200
                btn.color = ft.colors.BLACK
        page.update()
    
    # Crear botones de plan
    botones_plan = [
        ft.ElevatedButton(
            "Estándar - $20/mes",
            data="estandar",
            on_click=cambiar_plan,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        ),
        ft.ElevatedButton(
            "Premium - $50/mes",
            data="premium",
            on_click=cambiar_plan,
            bgcolor=ft.colors.GREY_200,
            color=ft.colors.BLACK
        ),
        ft.ElevatedButton(
            "Premium Vitalis - $100/mes",
            data="premium_vitalis",
            on_click=cambiar_plan,
            bgcolor=ft.colors.GREY_200,
            color=ft.colors.BLACK
        )
    ]
    
    # Crear contenedor de descripción del plan
    descripcion_plan_container = ft.Container(
        content=ft.Text(
            descripciones_plan[plan_seleccionado],
            size=14,
            color=ft.colors.BLACK,
            text_align=ft.TextAlign.CENTER
        ),
        padding=10,
        bgcolor=ft.colors.BLUE_50,
        border_radius=5,
        margin=10
    )
    
    # Función para mostrar detalles del cuidador
    def mostrar_detalles(e, cuidador):
        # Crear estrellas para la calificación
        estrellas = ft.Row(spacing=0)
        for i in range(5):
            if i < int(cuidador["calificacion"]):
                estrellas.controls.append(ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=20))
            elif i < cuidador["calificacion"]:
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
                        ft.Text(comentario["usuario"], weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        comentario_estrellas
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text(comentario["texto"], color=ft.colors.BLACK)
                ]),
                padding=10,
                border_radius=5,
                bgcolor=ft.colors.GREY_100
            )
            comentarios_lista.controls.append(comentario_card)
        
        # Crear header con logo Vitalis si aplica
        header_content = [
            ft.Image(src=cuidador["imagen"], width=120, height=120, fit=ft.ImageFit.COVER, border_radius=ft.border_radius.all(60))
        ]
        
        # Información del cuidador
        info_cuidador = ft.Column([
            ft.Text(cuidador["nombre"], size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Row([estrellas, ft.Text(f"{cuidador['calificacion']}/5", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)]),
            ft.Text(f"Especialidad: {cuidador['especialidad']}", size=16, color=ft.colors.BLACK),
            ft.Text(f"Experiencia: {cuidador['experiencia']}", size=16, color=ft.colors.BLACK),
            ft.Text(f"Precio: {cuidador['precio']}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
        ], spacing=5)
        
        # Si es Vitalis, agregar logo
        if cuidador["vitalis"]:
            vitalis_badge = ft.Container(
                content=ft.Image(
                    src="./assets/Vitalis_logo.jpg",
                    width=25,
                    height=25,
                    fit=ft.ImageFit.CONTAIN
                ),
                bgcolor=ft.colors.WHITE,
                width=30,
                height=30,
                border_radius=15,
                alignment=ft.alignment.center,
                padding=2
            )
            info_cuidador.controls.insert(1, vitalis_badge)
        
        # Crear contenido del diálogo
        detalles_content = ft.Column([
            ft.Row(header_content + [info_cuidador]),
            ft.Divider(),
            ft.Text("Descripción", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.BLACK),
            ft.Text(cuidador["descripcion"], color=ft.colors.BLACK),
            ft.Divider(),
            ft.Text("Disponibilidad", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.BLACK),
            ft.Text(cuidador["disponibilidad"], color=ft.colors.BLACK),
            ft.Divider(),
            ft.Text("Comentarios y Valoraciones", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.BLACK),
            comentarios_lista
        ], scroll=ft.ScrollMode.AUTO, spacing=15)
        
        # Función para contratar
        def contratar_cuidador(e, cuidador_id):
            dialogo_detalles.open = False
            
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Has contratado a {cuidador['nombre']}. Te contactaremos pronto para coordinar detalles."),
                bgcolor=ft.colors.GREEN_700,
                action="OK"
            )
            page.snack_bar.open = True
            page.update()
        
        # Crear diálogo de detalles
        dialogo_detalles = ft.AlertDialog(
            title=ft.Text("Detalles del Cuidador", color=ft.colors.BLACK),
            content=detalles_content,
            bgcolor=ft.colors.WHITE,  # Fondo blanco para mejor contraste
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
        actualizar_lista_cuidadores()
    
    # Campo de búsqueda
    busqueda = ft.TextField(
        label="Buscar por nombre o especialidad",
        prefix_icon=ft.icons.SEARCH,
        on_change=filtrar_cuidadores,
        width=400
    )
    
    # Contenedor para la lista de cuidadores
    lista_cuidadores = ft.Column(spacing=15)
    
    # Función para actualizar la lista de cuidadores
    def actualizar_lista_cuidadores():
        lista_cuidadores.controls = []
        
        # Filtrar por plan
        cuidadores_filtrados = []
        if plan_seleccionado == "estandar":
            cuidadores_filtrados = [c for c in cuidadores if c["rango"] == "estandar"]
        elif plan_seleccionado == "premium":
            cuidadores_filtrados = [c for c in cuidadores if c["rango"] in ["estandar", "premium"]]
        elif plan_seleccionado == "premium_vitalis":
            cuidadores_filtrados = [c for c in cuidadores if c["rango"] in ["estandar", "premium", "premium_vitalis"]]
        
        # Filtrar por búsqueda
        texto_busqueda = busqueda.value.lower() if busqueda.value else ""
        if texto_busqueda:
            cuidadores_filtrados = [c for c in cuidadores_filtrados if 
                                   texto_busqueda in c["nombre"].lower() or 
                                   texto_busqueda in c["especialidad"].lower() or 
                                   texto_busqueda in c["descripcion"].lower()]
        
        if not cuidadores_filtrados:
            lista_cuidadores.controls.append(
                ft.Container(
                    content=ft.Text(
                        "No se encontraron cuidadores con los criterios seleccionados",
                        text_align=ft.TextAlign.CENTER,
                        size=16,
                        color=ft.colors.BLACK
                    ),
                    padding=20
                )
            )
        
        for cuidador in cuidadores_filtrados:
            # Crear estrellas para la calificación
            estrellas = ft.Row(spacing=0)
            for i in range(5):
                if i < int(cuidador["calificacion"]):
                    estrellas.controls.append(ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=16))
                elif i < cuidador["calificacion"]:
                    estrellas.controls.append(ft.Icon(ft.icons.STAR_HALF, color=ft.colors.AMBER, size=16))
                else:
                    estrellas.controls.append(ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER, size=16))
            
            # Crear contenido de la imagen con badge Vitalis si aplica
            imagen_container = ft.Stack([
                ft.Container(
                    content=ft.Image(
                        src=cuidador["imagen"],
                        width=80,
                        height=80,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(40)
                    ),
                    margin=ft.margin.only(right=15)
                )
            ])
            
            if cuidador["vitalis"]:
                vitalis_badge = ft.Container(
                    content=ft.Image(
                        src="./assets/Vitalis_logo.jpg",
                        width=25,
                        height=25,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    bgcolor=ft.colors.WHITE,
                    width=30,
                    height=30,
                    border_radius=15,
                    alignment=ft.alignment.center,
                    padding=2
                )
                imagen_container.controls.append(
                    ft.Container(
                        content=vitalis_badge,
                        alignment=ft.alignment.top_right,
                        margin=ft.margin.only(top=5, right=20)
                    )
                )
            
            # Crear tarjeta de cuidador
            tarjeta = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            imagen_container,
                            ft.Column([
                                ft.Text(cuidador["nombre"], size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                ft.Text(f"Especialidad: {cuidador['especialidad']}", size=14, color=ft.colors.BLACK),
                                ft.Row([
                                    estrellas,
                                    ft.Text(f"{cuidador['calificacion']}/5", size=14, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
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
                                size=14,
                                color=ft.colors.BLACK
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
        "Volver al Panel de Familiares",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu_familiares
    )
    
    # Inicializar la lista de cuidadores
    actualizar_lista_cuidadores()
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                subtitulo,
                ft.Divider(height=2, color=ft.colors.BLUE_200),
                ft.Text("Selecciona tu Plan:", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Row(botones_plan, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                descripcion_plan_container,
                busqueda,
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
