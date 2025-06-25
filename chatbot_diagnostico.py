import flet as ft
import time
import random

def chatbot_diagnostico_page(page: ft.Page, datos_familiar=None):
    page.title = "Telemedicina - Diagnóstico Preliminar"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Obtener información del familiar y adulto mayor
    nombre_familiar = datos_familiar.get("nombres", "Usuario") if datos_familiar else "Usuario"
    nombre_adulto = datos_familiar.get("adulto_mayor", {}).get("nombre", "Adulto Mayor") if datos_familiar else "Adulto Mayor"
    
    # Definir las especialidades médicas
    especialidades = {
        "GERIATRIA": {
            "descripcion": "Especialidad médica dedicada a la atención de adultos mayores.",
            "sintomas": ["dificultad para moverse", "problemas de memoria", "caídas frecuentes", "fragilidad", "múltiples enfermedades crónicas"]
        },
        "PSICOLOGIA": {
            "descripcion": "Especialidad enfocada en la salud mental y el comportamiento humano.",
            "sintomas": ["tristeza", "ansiedad", "estrés", "problemas de autoestima", "dificultades en relaciones personales"]
        },
        "PSIQUIATRIA": {
            "descripcion": "Especialidad médica centrada en el diagnóstico y tratamiento de trastornos mentales.",
            "sintomas": ["depresión severa", "alucinaciones", "cambios de humor extremos", "pensamientos suicidas", "comportamiento errático"]
        },
        "REUMATOLOGIA": {
            "descripcion": "Especialidad médica que trata enfermedades del sistema musculoesquelético.",
            "sintomas": ["dolor en articulaciones", "inflamación", "rigidez", "limitación de movimiento", "dolor muscular crónico"]
        },
        "CARDIOLOGIA": {
            "descripcion": "Especialidad médica enfocada en el corazón y sistema circulatorio.",
            "sintomas": ["dolor en el pecho", "palpitaciones", "dificultad para respirar", "fatiga", "presión arterial alta"]
        },
        "NEUROLOGIA": {
            "descripcion": "Especialidad médica que trata trastornos del sistema nervioso.",
            "sintomas": ["dolores de cabeza severos", "mareos", "entumecimiento", "problemas de equilibrio", "convulsiones"]
        },
        "FISIOTERAPIA": {
            "descripcion": "Especialidad que trata lesiones o discapacidades mediante terapia física.",
            "sintomas": ["dolor muscular", "recuperación post-operatoria", "lesiones deportivas", "problemas de postura", "rehabilitación"]
        }
    }
    
    # Variables para el seguimiento de la conversación
    conversacion_activa = True
    preguntas_realizadas = 0
    sintomas_reportados = {}
    for esp in especialidades:
        sintomas_reportados[esp] = 0
    
    # Lista de preguntas del chatbot
    preguntas = [
        f"Hola {nombre_familiar}, soy tu asistente de telemedicina. Vamos a evaluar los síntomas de {nombre_adulto}. ¿Cuál es el principal motivo de consulta?",
        f"¿Desde hace cuánto tiempo {nombre_adulto} experimenta estos síntomas?",
        f"¿{nombre_adulto} siente dolor en alguna parte específica del cuerpo?",
        f"¿Has notado cambios en el estado de ánimo de {nombre_adulto} últimamente?",
        f"¿{nombre_adulto} tiene dificultad para realizar actividades físicas?",
        f"¿{nombre_adulto} ha experimentado problemas para dormir?",
        f"¿{nombre_adulto} siente fatiga o cansancio inusual?",
        f"¿{nombre_adulto} ha tenido dolores de cabeza frecuentes?",
        f"¿Has notado problemas de memoria o concentración en {nombre_adulto}?",
        f"¿{nombre_adulto} ha experimentado mareos o problemas de equilibrio?",
        f"¿{nombre_adulto} siente presión o dolor en el pecho?",
        f"¿Has notado inflamación en las articulaciones de {nombre_adulto}?",
        f"¿{nombre_adulto} tiene dificultad para respirar en ciertas situaciones?",
        f"¿{nombre_adulto} ha experimentado cambios en su peso recientemente?"
    ]
    
    # Función para volver al menú de familiares
    def volver_menu(e):
        from menu_familiares import menu_familiares_page
        page.clean()
        menu_familiares_page(page, datos_familiar)
    
    # Función para analizar la respuesta del usuario y actualizar los contadores de síntomas
    def analizar_respuesta(texto):
        texto = texto.lower()
        for especialidad, info in especialidades.items():
            for sintoma in info["sintomas"]:
                if sintoma in texto:
                    sintomas_reportados[especialidad] += 1
    
    # Función para determinar la especialidad recomendada
    def determinar_especialidad():
        max_coincidencias = 0
        especialidad_recomendada = "GERIATRIA"  # Valor por defecto
        
        for esp, coincidencias in sintomas_reportados.items():
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                especialidad_recomendada = esp
        
        # Si hay empate, elegir aleatoriamente entre las especialidades con más coincidencias
        empates = [esp for esp, coincidencias in sintomas_reportados.items() if coincidencias == max_coincidencias]
        if len(empates) > 1:
            especialidad_recomendada = random.choice(empates)
            
        return especialidad_recomendada
    
    # Función para mostrar el resultado del diagnóstico
    def mostrar_diagnostico():
        nonlocal conversacion_activa
        conversacion_activa = False
        
        especialidad = determinar_especialidad()
        
        # Mensaje del chatbot con la recomendación
        mensaje_bot = f"Basado en los síntomas de {nombre_adulto}, recomendaría consultar con un especialista en {especialidad}. {especialidades[especialidad]['descripcion']}\n\nRecuerda que este es un diagnóstico preliminar y no reemplaza la consulta médica profesional."
        
        # Agregar mensaje del chatbot
        chat_container.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Asistente de Telemedicina", weight=ft.FontWeight.BOLD, color=ft.colors.PINK),
                    ft.Container(
                        content=ft.Text(mensaje_bot, color=ft.colors.BLACK),
                        bgcolor=ft.colors.PINK_50,
                        border_radius=10,
                        padding=10,
                        width=300
                    )
                ]),
                margin=ft.margin.only(bottom=15)
            )
        )
        
        # Mostrar botones de acción
        chat_container.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("¿Qué deseas hacer ahora?", weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.ElevatedButton(
                            "Agendar cita",
                            icon=ft.icons.CALENDAR_TODAY,
                            bgcolor=ft.colors.GREEN,
                            color=ft.colors.WHITE,
                            on_click=lambda e: mostrar_mensaje_cita(especialidad)
                        ),
                        ft.ElevatedButton(
                            "Buscar cuidador",
                            icon=ft.icons.PEOPLE,
                            bgcolor=ft.colors.BLUE,
                            color=ft.colors.WHITE,
                            on_click=lambda e: ir_marketplace(e)
                        ),
                        ft.ElevatedButton(
                            "Volver al menú",
                            icon=ft.icons.HOME,
                            on_click=volver_menu
                        )
                    ], spacing=10, wrap=True)
                ]),
                margin=ft.margin.only(bottom=15, top=15)
            )
        )
        
        # Deshabilitar el campo de entrada y el botón de enviar
        mensaje_input.disabled = True
        enviar_btn.disabled = True
        
        # Actualizar la página
        page.update()
        
        # Hacer scroll hasta el final
        chat_container.controls[-1].focus()
        page.update()
    
    # Función para ir al marketplace
    def ir_marketplace(e):
        from marketplace_cuidadores import marketplace_page
        page.clean()
        marketplace_page(page, datos_familiar)
    
    # Función para mostrar mensaje de confirmación de cita
    def mostrar_mensaje_cita(especialidad):
        # Generar fecha aleatoria para la cita (entre 1 y 7 días después)
        dias = random.randint(1, 7)
        fecha_cita = time.strftime("%d/%m/%Y", time.localtime(time.time() + dias * 86400))
        
        # Mensaje de confirmación
        mensaje_confirmacion = f"Se ha agendado una cita de telemedicina para {nombre_adulto} con el especialista en {especialidad} para el {fecha_cita}. Recibirás un correo electrónico con los detalles y el enlace de la videollamada."
        
        # Agregar mensaje de confirmación
        chat_container.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Sistema de Telemedicina", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ft.Container(
                        content=ft.Text(mensaje_confirmacion, color=ft.colors.BLACK),
                        bgcolor=ft.colors.GREEN_50,
                        border_radius=10,
                        padding=10,
                        width=300
                    )
                ]),
                margin=ft.margin.only(bottom=15)
            )
        )
        
        page.update()
        
        # Hacer scroll hasta el final
        chat_container.controls[-1].focus()
        page.update()
    
    # Función para enviar mensaje
    def enviar_mensaje(e):
        if not mensaje_input.value:
            return
        
        nonlocal preguntas_realizadas
        
        # Obtener el mensaje del usuario
        mensaje_usuario = mensaje_input.value
        
        # Agregar mensaje del usuario al chat
        chat_container.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{nombre_familiar}", weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    ft.Container(
                        content=ft.Text(mensaje_usuario),
                        bgcolor=ft.colors.GREY_100,
                        border_radius=10,
                        padding=10,
                        width=300
                    )
                ]),
                alignment=ft.alignment.center_right,
                margin=ft.margin.only(bottom=15)
            )
        )
        
        # Limpiar el campo de entrada
        mensaje_input.value = ""
        page.update()
        
        # Analizar la respuesta del usuario
        analizar_respuesta(mensaje_usuario)
        
        # Simular que el chatbot está escribiendo
        chat_container.controls.append(
            ft.Container(
                content=ft.Row([
                    ft.ProgressRing(width=16, height=16, stroke_width=2),
                    ft.Text("Escribiendo...", size=12, color=ft.colors.GREY_400)
                ]),
                margin=ft.margin.only(bottom=10)
            )
        )
        page.update()
        
        # Esperar un momento para simular que el chatbot está pensando
        time.sleep(1)
        
        # Eliminar el indicador de "escribiendo..."
        chat_container.controls.pop()
        
        # Incrementar el contador de preguntas
        preguntas_realizadas += 1
        
        # Si ya se han realizado suficientes preguntas, mostrar el diagnóstico
        if preguntas_realizadas >= 5:
            mostrar_diagnostico()
            return
        
        # Obtener la siguiente pregunta
        siguiente_pregunta = preguntas[min(preguntas_realizadas, len(preguntas) - 1)]
        
        # Agregar respuesta del chatbot
        chat_container.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Asistente de Telemedicina", weight=ft.FontWeight.BOLD, color=ft.colors.PINK),
                    ft.Container(
                        content=ft.Text(siguiente_pregunta, color=ft.colors.BLACK),
                        bgcolor=ft.colors.PINK_50,
                        border_radius=10,
                        padding=10,
                        width=300
                    )
                ]),
                margin=ft.margin.only(bottom=15)
            )
        )
        
        page.update()
        
        # Hacer scroll hasta el final
        chat_container.controls[-1].focus()
        page.update()
    
    # Título y descripción
    titulo = ft.Text(
        "Telemedicina - Diagnóstico Preliminar",
        size=24,
        color=ft.colors.PINK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    descripcion = ft.Text(
        f"Evaluación médica virtual para {nombre_adulto}",
        size=16,
        color=ft.colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )
    
    # Contenedor para los mensajes del chat
    chat_container = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        height=400,
        width=600
    )
    
    # Campo de entrada para el mensaje
    mensaje_input = ft.TextField(
        hint_text="Describe los síntomas aquí...",
        border_color=ft.colors.PINK,
        multiline=True,
        min_lines=1,
        max_lines=3,
        expand=True
    )
    
    # Botón para enviar mensaje
    enviar_btn = ft.IconButton(
        icon=ft.icons.SEND,
        icon_color=ft.colors.PINK,
        tooltip="Enviar mensaje",
        on_click=enviar_mensaje
    )
    
    # Botón para volver
    boton_volver = ft.ElevatedButton(
        "Volver al Panel de Familiares",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_menu
    )
    
    # Agregar mensaje inicial del chatbot
    chat_container.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("Asistente de Telemedicina", weight=ft.FontWeight.BOLD, color=ft.colors.PINK),
                ft.Container(
                    content=ft.Text(preguntas[0], color=ft.colors.BLACK),
                    bgcolor=ft.colors.PINK_50,
                    border_radius=10,
                    padding=10,
                    width=300
                )
            ]),
            margin=ft.margin.only(bottom=15)
        )
    )
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                descripcion,
                ft.Divider(height=2, color=ft.colors.PINK_200),
                ft.Container(
                    content=chat_container,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=10,
                    padding=15,
                    bgcolor=ft.colors.WHITE
                ),
                ft.Row([
                    mensaje_input,
                    enviar_btn
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(
                    content=ft.Text(
                        "Nota: Este es un servicio de telemedicina preliminar y no reemplaza la consulta presencial con un profesional médico.",
                        size=12,
                        color=ft.colors.GREY_700,
                        italic=True
                    ),
                    margin=ft.margin.only(top=10, bottom=10)
                ),
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
        chatbot_diagnostico_page(page)
    
    ft.app(target=main)
