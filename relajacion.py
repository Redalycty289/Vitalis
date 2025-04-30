import flet as ft
import webbrowser
from menu_adulto_mayor import main as menu_principal

class Video:
    def __init__(self, titulo, imagen_url, url, descripcion):
        self.titulo = titulo
        self.imagen_url = imagen_url
        self.url = url
        self.descripcion = descripcion

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Espacio de Relajación"
    page.padding = 20
    page.bgcolor = "#E0F7FA"  # Color celeste claro
    
    # Función para volver al menú principal
    def volver_menu(e):
        # Close any open dialogs
        detalles_dialog.open = False
        if 'nuevo_video_dialog' in locals() and nuevo_video_dialog.open:
            nuevo_video_dialog.open = False
        # Clean the page and navigate back
        page.clean()
        menu_principal(page)
    
    # Función para abrir videos
    def abrir_video(e, url):
        webbrowser.open(url)
    
    # Función para mostrar detalles del video
    def mostrar_detalles(e, video):
        detalles_dialog.title = ft.Text(video.titulo, size=20, weight=ft.FontWeight.BOLD)
        detalles_dialog.content = ft.Column([
            ft.Image(src=video.imagen_url, width=300, height=200, fit=ft.ImageFit.CONTAIN),
            ft.Text(video.descripcion, size=16),
            ft.ElevatedButton(
                "Ver video completo",
                on_click=lambda e, url=video.url: abrir_video(e, url),
                bgcolor="#9C27B0",
                color="white"
            )
        ])
        detalles_dialog.open = True
        page.update()
    
    # Título principal
    titulo = ft.Text(
        "Espacio de Relajación",
        size=28,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="#4527A0"
    )
    
    # Descripción
    descripcion = ft.Text(
        "Encuentra paz y tranquilidad con estos ejercicios de relajación",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color="#5E35B1"
    )
    
    # Videos de relajación predefinidos con descripciones
    videos = [
        Video(
            "Técnicas de respiración",
            "/placeholder.svg?height=200&width=300",
            "https://www.youtube.com/watch?v=nAR2PUPyH1I",
            "Aprende técnicas de respiración profunda para reducir el estrés y mejorar tu concentración. Esta práctica de 5 minutos puede realizarse diariamente."
        ),
        Video(
            "Técnicas de meditación",
            "/placeholder.svg?height=200&width=300",
            "https://www.youtube.com/watch?v=A-FKeahD_lQ",
            "Ejercicios de meditación guiada para principiantes. Ideal para personas que buscan un momento de calma en su rutina diaria."
        ),
        Video(
            "Técnicas de estiramiento",
            "/placeholder.svg?height=200&width=300",
            "https://www.youtube.com/watch?v=N39dSYRFdv8",
            "Estiramientos suaves para adultos mayores que ayudan a mejorar la flexibilidad y reducir la tensión muscular."
        ),
        Video(
            "Música relajante",
            "/placeholder.svg?height=200&width=300",
            "https://www.youtube.com/watch?v=lFcSrYw-ARY",
            "Música calmante para momentos de descanso y relajación. Perfecta para escuchar antes de dormir o durante momentos de ansiedad."
        ),
    ]
    
    # Diálogo para mostrar detalles del video
    detalles_dialog = ft.AlertDialog(
        title=ft.Text(""),
        content=ft.Column(
        [],
        scroll=ft.ScrollMode.AUTO,
        height=400 if page.height < 600 else None,  # Set max height on small screens
    ),
    actions=[
        ft.TextButton("Cerrar", on_click=lambda e: setattr(detalles_dialog, "open", False))
    ],
    )
    
    # Crear tarjetas de video
    video_cards = []
    for video in videos:
        card = ft.Container(
            width=320,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src=video.imagen_url, 
                        width=280, 
                        height=160, 
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(8)
                    ),
                    ft.Text(
                        video.titulo, 
                        size=18, 
                        weight=ft.FontWeight.BOLD,
                        color="#4527A0"
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.PLAY_ARROW),
                                        ft.Text("Ver video")
                                    ]
                                ),
                                style=ft.ButtonStyle(
                                    color="white",
                                    bgcolor="#9C27B0"
                                ),
                                on_click=lambda e, url=video.url: abrir_video(e, url)
                            ),
                            ft.OutlinedButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.INFO),
                                        ft.Text("Detalles")
                                    ]
                                ),
                                on_click=lambda e, v=video: mostrar_detalles(e, v)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    )
                ],
                spacing=10
            ),
            padding=20,
            margin=ft.margin.only(bottom=15),
            bgcolor="white",
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLUE_GREY_100,
            )
        )
        video_cards.append(card)
    
    # Crear grid adaptativo para las tarjetas
    def create_grid(e=None):
        grid.controls = []
        screen_width = page.width or 600
        
        # Determinar número de columnas según ancho de pantalla
        columns = 3
        if screen_width < 900:
            columns = 2
        if screen_width < 600:
            columns = 1
            
        # Dividir tarjetas en filas
        for i in range(0, len(video_cards), columns):
            row_cards = video_cards[i:i+columns]
            grid.controls.append(
                ft.Row(
                    controls=row_cards,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True
                )
            )
        page.update()
    
    # Make the grid scrollable
    grid = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        width=page.width if page.width else 600,
    )
    
    # Botón para agregar nuevos videos de relajación
    def mostrar_form_nuevo_video(e):
        nuevo_video_dialog.open = True
        page.update()
    
    agregar_btn = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor="#9C27B0",
        on_click=mostrar_form_nuevo_video
    )
    
    # Diálogo para agregar nuevo video
    titulo_input = ft.TextField(label="Título del video", width=400)
    url_input = ft.TextField(label="URL del video (YouTube)", width=400)
    descripcion_input = ft.TextField(label="Descripción", width=400, multiline=True, min_lines=3)
    
    def agregar_nuevo_video(e):
        if titulo_input.value and url_input.value and descripcion_input.value:
            nuevo_video = Video(
                titulo_input.value,
                "/placeholder.svg?height=200&width=300",
                url_input.value,
                descripcion_input.value
            )
            videos.append(nuevo_video)
            
            # Crear nueva tarjeta
            card = ft.Container(
                width=320,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src=nuevo_video.imagen_url, 
                            width=280, 
                            height=160, 
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(8)
                        ),
                        ft.Text(
                            nuevo_video.titulo, 
                            size=18, 
                            weight=ft.FontWeight.BOLD,
                            color="#4527A0"
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.PLAY_ARROW),
                                            ft.Text("Ver video")
                                        ]
                                    ),
                                    style=ft.ButtonStyle(
                                        color="white",
                                        bgcolor="#9C27B0"
                                    ),
                                    on_click=lambda e, url=nuevo_video.url: abrir_video(e, url)
                                ),
                                ft.OutlinedButton(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.INFO),
                                            ft.Text("Detalles")
                                        ]
                                    ),
                                    on_click=lambda e, v=nuevo_video: mostrar_detalles(e, v)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                        )
                    ],
                    spacing=10
                ),
                padding=20,
                margin=ft.margin.only(bottom=15),
                bgcolor="white",
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.colors.BLUE_GREY_100,
                )
            )
            video_cards.append(card)
            
            # Limpiar campos y cerrar diálogo
            titulo_input.value = ""
            url_input.value = ""
            descripcion_input.value = ""
            nuevo_video_dialog.open = False
            create_grid()
        else:
            # Mostrar error si faltan campos
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor complete todos los campos"),
                bgcolor=ft.colors.RED_400
            )
            page.snack_bar.open = True
        page.update()
    
    nuevo_video_dialog = ft.AlertDialog(
        title=ft.Text("Agregar nuevo video de relajación"),
        content=ft.Column([
            titulo_input,
            url_input,
            descripcion_input,
        ], 
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        height=300 if page.height < 600 else None,  # Set max height on small screens
    ),
    actions=[
        ft.TextButton("Cancelar", on_click=lambda e: setattr(nuevo_video_dialog, "open", False)),
        ft.ElevatedButton("Agregar", on_click=agregar_nuevo_video)
    ],
)
    
    # Make sure the page has scrolling enabled
    page.scroll = ft.ScrollMode.AUTO

    # Botón para volver al menú
    volver_button = ft.ElevatedButton(
        "Volver al Menú",
        icon=ft.icons.ARROW_BACK,
        bgcolor="#4527A0",
        color="white",
        on_click=volver_menu
    )

    # Make the main column scrollable
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                descripcion,
                ft.Divider(height=2, color="#B39DDB"),
                grid,
                volver_button
            ], 
            scroll=ft.ScrollMode.AUTO,
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            padding=ft.padding.only(bottom=80),  # Add padding at bottom for FAB
        )
    )
    
    page.floating_action_button = agregar_btn
    page.dialog = detalles_dialog
    
    # Hacer que el diseño sea responsivo
    page.on_resize = create_grid
    create_grid()  # Inicializar grid
    
if __name__ == "__main__":
  ft.app(target=main)

