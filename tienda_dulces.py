import flet as ft
import random

def tienda_page(page: ft.Page):
    page.title = "Tienda"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    # Carrito de compras
    carrito = []
    
    # Función para volver a la selección de usuario
    def volver_seleccion(e):
        from seleccion_usuario import main as seleccion_usuario
        page.clean()
        seleccion_usuario(page)
    
    # Función para actualizar el contador del carrito
    def actualizar_contador_carrito():
        cantidad_total = sum(item["cantidad"] for item in carrito)
        contador_carrito.value = str(cantidad_total) if cantidad_total > 0 else ""
        contador_carrito.visible = cantidad_total > 0
        page.update()
    
    # Función para agregar producto al carrito
    def agregar_al_carrito(e, producto):
        # Verificar si el producto ya está en el carrito
        for item in carrito:
            if item["id"] == producto["id"]:
                item["cantidad"] += 1
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"Se agregó otro {producto['nombre']} al carrito"),
                    bgcolor=ft.colors.GREEN
                )
                page.snack_bar.open = True
                actualizar_contador_carrito()
                return
        
        # Si no está en el carrito, agregarlo
        carrito.append({
            "id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "imagen": producto["imagen"],
            "cantidad": 1
        })
        
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{producto['nombre']} agregado al carrito"),
            bgcolor=ft.colors.GREEN
        )
        page.snack_bar.open = True
        actualizar_contador_carrito()
    
    # Función para mostrar detalles del producto
    def mostrar_detalles(e, producto):
        # Crear contenido del diálogo
        detalles_content = ft.Column([
            ft.Image(
                src=producto["imagen"],
                width=300,
                height=200,
                fit=ft.ImageFit.CONTAIN
            ),
            ft.Text(producto["nombre"], size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Precio: ${producto['precio']:.2f}", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.PINK),
            ft.Text("Descripción:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text(producto["descripcion"], size=14),
            ft.Text("Ingredientes:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text(producto["ingredientes"], size=14),
            ft.Container(
                content=ft.Column([
                    ft.Text("Información Nutricional", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Calorías: {producto['calorias']} kcal", size=14),
                    ft.Text(f"Azúcares: {producto['azucares']}g", size=14),
                    ft.Text(f"Grasas: {producto['grasas']}g", size=14)
                ]),
                padding=10,
                border_radius=5,
                bgcolor=ft.colors.PINK_50
            )
        ], scroll=ft.ScrollMode.AUTO, spacing=10)
        
        # Crear diálogo de detalles
        dialogo_detalles = ft.AlertDialog(
            title=ft.Text("Detalles del Producto"),
            content=detalles_content,
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: setattr(dialogo_detalles, "open", False)),
                ft.ElevatedButton(
                    "Agregar al Carrito",
                    bgcolor=ft.colors.PINK,
                    color=ft.colors.WHITE,
                    on_click=lambda e, p=producto: agregar_y_cerrar(e, p, dialogo_detalles)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        # Función para agregar al carrito y cerrar diálogo
        def agregar_y_cerrar(e, producto, dialogo):
            agregar_al_carrito(e, producto)
            dialogo.open = False
            page.update()
        
        page.dialog = dialogo_detalles
        dialogo_detalles.open = True
        page.update()
    
    # Función para mostrar el carrito
    def mostrar_carrito(e):
        if not carrito:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("El carrito está vacío"),
                bgcolor=ft.colors.ORANGE
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # Crear lista de items en el carrito
        items_carrito = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
        total = 0
        
        for item in carrito:
            subtotal = item["precio"] * item["cantidad"]
            total += subtotal
            
            # Crear controles para ajustar cantidad
            def crear_control_cantidad(item_actual):
                def aumentar(e, item=item_actual):
                    item["cantidad"] += 1
                    actualizar_carrito_dialog()
                
                def disminuir(e, item=item_actual):
                    if item["cantidad"] > 1:
                        item["cantidad"] -= 1
                        actualizar_carrito_dialog()
                    else:
                        carrito.remove(item)
                        actualizar_carrito_dialog()
                
                return ft.Row([
                    ft.IconButton(
                        icon=ft.icons.REMOVE_CIRCLE,
                        on_click=disminuir,
                        icon_color=ft.colors.RED
                    ),
                    ft.Text(f"{item['cantidad']}", size=16),
                    ft.IconButton(
                        icon=ft.icons.ADD_CIRCLE,
                        on_click=aumentar,
                        icon_color=ft.colors.GREEN
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            
            # Crear tarjeta de item
            item_card = ft.Card(
                content=ft.Container(
                    content=ft.Row([
                        ft.Image(
                            src=item["imagen"],
                            width=60,
                            height=60,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Column([
                            ft.Text(item["nombre"], weight=ft.FontWeight.BOLD),
                            ft.Text(f"${item['precio']:.2f} x {item['cantidad']} = ${subtotal:.2f}")
                        ], expand=True),
                        crear_control_cantidad(item)
                    ]),
                    padding=10
                )
            )
            items_carrito.controls.append(item_card)
        
        # Crear resumen del carrito
        resumen = ft.Container(
            content=ft.Column([
                ft.Divider(),
                ft.Row([
                    ft.Text("Subtotal:", weight=ft.FontWeight.BOLD),
                    ft.Text(f"${total:.2f}")
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([
                    ft.Text("Impuestos (10%):", weight=ft.FontWeight.BOLD),
                    ft.Text(f"${total * 0.1:.2f}")
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([
                    ft.Text("Total:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"${total * 1.1:.2f}", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.PINK)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]),
            padding=10,
            bgcolor=ft.colors.PINK_50,
            border_radius=5
        )
        
        # Función para actualizar el diálogo del carrito
        def actualizar_carrito_dialog():
            carrito_dialog.open = False
            page.update()
            actualizar_contador_carrito()
            mostrar_carrito(None)
        
        # Función para vaciar el carrito
        def vaciar_carrito(e):
            carrito.clear()
            carrito_dialog.open = False
            page.update()
            actualizar_contador_carrito()
            
            page.snack_bar = ft.SnackBar(
                content=ft.Text("El carrito ha sido vaciado"),
                bgcolor=ft.colors.ORANGE
            )
            page.snack_bar.open = True
            page.update()
        
        # Función para proceder al pago
        def proceder_pago(e):
            carrito_dialog.open = False
            page.update()
            mostrar_checkout()
        
        # Crear diálogo del carrito
        carrito_dialog = ft.AlertDialog(
            title=ft.Text("Carrito de Compras"),
            content=ft.Column([
                items_carrito,
                resumen
            ], scroll=ft.ScrollMode.AUTO, spacing=10, height=400),
            actions=[
                ft.TextButton("Vaciar Carrito", on_click=vaciar_carrito),
                ft.TextButton("Cerrar", on_click=lambda e: setattr(carrito_dialog, "open", False)),
                ft.ElevatedButton(
                    "Proceder al Pago",
                    bgcolor=ft.colors.PINK,
                    color=ft.colors.WHITE,
                    on_click=proceder_pago
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        page.dialog = carrito_dialog
        carrito_dialog.open = True
        page.update()
    
    # Función para mostrar checkout
    def mostrar_checkout():
        # Calcular total
        subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
        impuestos = subtotal * 0.1
        total = subtotal + impuestos
        
        # Campos para información de pago
        nombre_tarjeta = ft.TextField(
            label="Nombre en la tarjeta",
            border_color=ft.colors.PINK,
            width=350
        )
        
        numero_tarjeta = ft.TextField(
            label="Número de tarjeta",
            border_color=ft.colors.PINK,
            width=350
        )
        
        fecha_expiracion = ft.TextField(
            label="Fecha de expiración (MM/AA)",
            border_color=ft.colors.PINK,
            width=170
        )
        
        cvv = ft.TextField(
            label="CVV",
            border_color=ft.colors.PINK,
            width=170,
            password=True
        )
        
        direccion_envio = ft.TextField(
            label="Dirección de envío",
            border_color=ft.colors.PINK,
            width=350,
            multiline=True,
            min_lines=2
        )
        
        # Función para procesar el pago
        def procesar_pago(e):
            if all([nombre_tarjeta.value, numero_tarjeta.value, fecha_expiracion.value, cvv.value, direccion_envio.value]):
                checkout_dialog.open = False
                page.update()
                
                # Mostrar confirmación
                mostrar_confirmacion()
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("Por favor complete todos los campos"),
                    bgcolor=ft.colors.RED
                )
                page.snack_bar.open = True
                page.update()
        
        # Crear diálogo de checkout
        checkout_dialog = ft.AlertDialog(
            title=ft.Text("Finalizar Compra"),
            content=ft.Column([
                ft.Text("Resumen de la Compra", size=18, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text("Subtotal:", weight=ft.FontWeight.BOLD),
                            ft.Text(f"${subtotal:.2f}")
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([
                            ft.Text("Impuestos (10%):", weight=ft.FontWeight.BOLD),
                            ft.Text(f"${impuestos:.2f}")
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([
                            ft.Text("Total:", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"${total:.2f}", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.PINK)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ]),
                    padding=10,
                    bgcolor=ft.colors.PINK_50,
                    border_radius=5
                ),
                ft.Divider(),
                ft.Text("Información de Pago", size=18, weight=ft.FontWeight.BOLD),
                nombre_tarjeta,
                numero_tarjeta,
                ft.Row([
                    fecha_expiracion,
                    cvv
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(),
                ft.Text("Información de Envío", size=18, weight=ft.FontWeight.BOLD),
                direccion_envio
            ], scroll=ft.ScrollMode.AUTO, spacing=10, height=500),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: setattr(checkout_dialog, "open", False)),
                ft.ElevatedButton(
                    "Confirmar Pago",
                    bgcolor=ft.colors.PINK,
                    color=ft.colors.WHITE,
                    on_click=procesar_pago
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        page.dialog = checkout_dialog
        checkout_dialog.open = True
        page.update()
    
    # Función para mostrar confirmación
    def mostrar_confirmacion():
        # Generar número de orden aleatorio
        numero_orden = f"ORD-{random.randint(10000, 99999)}"
        
        # Crear diálogo de confirmación
        confirmacion_dialog = ft.AlertDialog(
            title=ft.Text("¡Compra Exitosa!"),
            content=ft.Column([
                ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=64),
                ft.Text("Su pedido ha sido procesado correctamente", size=16, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Número de orden: {numero_orden}", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("Recibirá un correo electrónico con los detalles de su compra", size=14, text_align=ft.TextAlign.CENTER),
                ft.Text("¡Gracias por su compra!", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=ft.colors.PINK)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            actions=[
                ft.ElevatedButton(
                    "Continuar Comprando",
                    bgcolor=ft.colors.PINK,
                    color=ft.colors.WHITE,
                    on_click=lambda e: finalizar_compra(e)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )
        
        # Función para finalizar la compra
        def finalizar_compra(e):
            # Vaciar el carrito
            carrito.clear()
            actualizar_contador_carrito()
            
            # Cerrar diálogo
            confirmacion_dialog.open = False
            page.update()
        
        page.dialog = confirmacion_dialog
        confirmacion_dialog.open = True
        page.update()
    
    # Función para filtrar productos
    def filtrar_productos(e):
        texto_busqueda = busqueda.value.lower() if busqueda.value else ""
        categoria_seleccionada = filtro_categoria.value
        
        # Filtrar por texto de búsqueda y categoría
        productos_filtrados = productos
        if texto_busqueda:
            productos_filtrados = [p for p in productos_filtrados if 
                                texto_busqueda in p["nombre"].lower() or 
                                texto_busqueda in p["descripcion"].lower()]
        
        if categoria_seleccionada and categoria_seleccionada != "Todas":
            productos_filtrados = [p for p in productos_filtrados if 
                                p["categoria"] == categoria_seleccionada]
        
        # Actualizar la lista de productos
        actualizar_lista_productos(productos_filtrados)
    
    # Título principal
    titulo = ft.Text(
        "Tienda de Dulces",
        size=32,
        color=ft.colors.PINK_700,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    subtitulo = ft.Text(
        "Deléitate con nuestros dulces caseros en diferentes presentaciones",
        size=16,
        color=ft.colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )
    
    # Datos de ejemplo para productos (enfocados en dulces en diferentes presentaciones)
    productos = [
        {
            "id": 1,
            "nombre": "Bombones de Chocolate Surtidos",
            "precio": 12.99,
            "descripcion": "Deliciosos bombones de chocolate con diferentes rellenos. Presentación en caja elegante de 12 unidades.",
            "categoria": "Cajas Surtidas",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Chocolate negro 70%, crema, mantequilla, esencia de vainilla, frutos secos, licor.",
            "calorias": 120,
            "azucares": 8,
            "grasas": 7
        },
        {
            "id": 2,
            "nombre": "Dulces Tradicionales - Bolsa Familiar",
            "precio": 9.99,
            "descripcion": "Surtido de dulces tradicionales en bolsa familiar de 500g. Ideal para compartir.",
            "categoria": "Bolsas",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Azúcar, glucosa, saborizantes naturales, colorantes naturales.",
            "calorias": 90,
            "azucares": 18,
            "grasas": 0
        },
        {
            "id": 3,
            "nombre": "Trufas de Chocolate - Caja Premium",
            "precio": 18.99,
            "descripcion": "Exquisitas trufas de chocolate en caja premium de 9 unidades. Perfecto para regalo.",
            "categoria": "Cajas Premium",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Chocolate negro, crema, mantequilla, cacao en polvo, licor.",
            "calorias": 150,
            "azucares": 9,
            "grasas": 12
        },
        {
            "id": 4,
            "nombre": "Mini Dulces Surtidos - Bolsa Individual",
            "precio": 3.99,
            "descripcion": "Bolsa individual de mini dulces surtidos. 100g de pura felicidad.",
            "categoria": "Bolsas",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Azúcar, glucosa, saborizantes naturales, colorantes naturales.",
            "calorias": 85,
            "azucares": 16,
            "grasas": 0
        },
        {
            "id": 5,
            "nombre": "Dulces Artesanales - Caja Degustación",
            "precio": 15.99,
            "descripcion": "Caja degustación con 15 dulces artesanales variados. Una experiencia para los sentidos.",
            "categoria": "Cajas Surtidas",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Ingredientes variados según el tipo de dulce (chocolate, frutas, frutos secos, etc.).",
            "calorias": 110,
            "azucares": 12,
            "grasas": 5
        },
        {
            "id": 6,
            "nombre": "Paletas Artesanales - Pack de 5",
            "precio": 8.99,
            "descripcion": "Pack de 5 paletas artesanales de diferentes sabores. Elaboradas a mano.",
            "categoria": "Packs",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Azúcar, glucosa, saborizantes naturales, colorantes naturales.",
            "calorias": 95,
            "azucares": 20,
            "grasas": 0
        },
        {
            "id": 7,
            "nombre": "Dulces Sin Azúcar - Caja Especial",
            "precio": 14.99,
            "descripcion": "Caja especial de dulces sin azúcar añadido. 12 unidades para disfrutar sin culpa.",
            "categoria": "Cajas Especiales",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Edulcorantes naturales, frutas, chocolate sin azúcar, stevia.",
            "calorias": 60,
            "azucares": 2,
            "grasas": 3
        },
        {
            "id": 8,
            "nombre": "Dulces Regionales - Caja Gourmet",
            "precio": 19.99,
            "descripcion": "Selección gourmet de dulces regionales tradicionales. Caja de 10 unidades con recetas auténticas.",
            "categoria": "Cajas Premium",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Ingredientes naturales según recetas tradicionales (frutas, azúcar, miel, frutos secos).",
            "calorias": 130,
            "azucares": 14,
            "grasas": 6
        },
        {
            "id": 9,
            "nombre": "Dulces de Temporada - Edición Limitada",
            "precio": 16.99,
            "descripcion": "Edición limitada de dulces de temporada. Caja de 8 unidades con sabores únicos.",
            "categoria": "Cajas Especiales",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Ingredientes de temporada (frutas, especias, chocolate, etc.).",
            "calorias": 115,
            "azucares": 13,
            "grasas": 5
        },
        {
            "id": 10,
            "nombre": "Mini Dulces - Frasco Decorativo",
            "precio": 13.99,
            "descripcion": "Frasco decorativo reutilizable lleno de mini dulces surtidos. 250g de dulzura.",
            "categoria": "Presentaciones Especiales",
            "imagen": "/placeholder.svg?height=200&width=200",
            "ingredientes": "Azúcar, glucosa, saborizantes naturales, colorantes naturales.",
            "calorias": 90,
            "azucares": 17,
            "grasas": 0
        }
    ]
    
    # Campo de búsqueda
    busqueda = ft.TextField(
        label="Buscar productos",
        prefix_icon=ft.icons.SEARCH,
        on_change=filtrar_productos,
        width=400
    )
    
    # Filtro de categoría
    categorias = ["Todas"] + list(set([p["categoria"] for p in productos]))
    filtro_categoria = ft.Dropdown(
        label="Filtrar por presentación",
        options=[ft.dropdown.Option(categoria) for categoria in categorias],
        value="Todas",
        on_change=filtrar_productos,
        width=300
    )
    
    # Botón del carrito con contador
    contador_carrito = ft.Container(
        content=ft.Text("0", color=ft.colors.WHITE, size=12),
        bgcolor=ft.colors.RED,
        width=20,
        height=20,
        border_radius=10,
        alignment=ft.alignment.center,
        visible=False
    )
    
    boton_carrito = ft.Stack([
        ft.IconButton(
            icon=ft.icons.SHOPPING_CART,
            icon_color=ft.colors.PINK,
            icon_size=30,
            tooltip="Ver carrito",
            on_click=mostrar_carrito
        ),
        ft.Container(
            content=contador_carrito,
            alignment=ft.alignment.top_right,
            margin=ft.margin.only(top=5, right=5)
        )
    ])
    
    # Contenedor para la lista de productos
    lista_productos = ft.Column(spacing=15)
    
    # Función para actualizar la lista de productos
    def actualizar_lista_productos(productos_mostrados):
        lista_productos.controls = []
        
        if not productos_mostrados:
            lista_productos.controls.append(
                ft.Container(
                    content=ft.Text(
                        "No se encontraron productos con los criterios seleccionados",
                        text_align=ft.TextAlign.CENTER,
                        size=16
                    ),
                    padding=20
                )
            )
            page.update()
            return
        
        # Crear filas de productos (3 productos por fila)
        for i in range(0, len(productos_mostrados), 3):
            fila_productos = ft.Row(
                controls=[],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True
            )
            
            # Agregar productos a la fila
            for producto in productos_mostrados[i:i+3]:
                # Crear tarjeta de producto
                tarjeta = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Image(
                                src=producto["imagen"],
                                width=200,
                                height=150,
                                fit=ft.ImageFit.CONTAIN
                            ),
                            ft.Container(
                                content=ft.Text(
                                    producto["nombre"],
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                padding=ft.padding.only(top=10)
                            ),
                            ft.Container(
                                content=ft.Text(
                                    f"${producto['precio']:.2f}",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.PINK
                                ),
                                padding=ft.padding.only(top=5)
                            ),
                            ft.Container(
                                content=ft.Text(
                                    producto["categoria"],
                                    size=14,
                                    color=ft.colors.GREY_700
                                ),
                                padding=ft.padding.only(top=5)
                            ),
                            ft.Container(
                                content=ft.Row([
                                    ft.ElevatedButton(
                                        "Ver detalles",
                                        icon=ft.icons.INFO,
                                        on_click=lambda e, p=producto: mostrar_detalles(e, p),
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                    ),
                                    ft.ElevatedButton(
                                        "Agregar al carrito",
                                        icon=ft.icons.ADD_SHOPPING_CART,
                                        on_click=lambda e, p=producto: agregar_al_carrito(e, p),
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                        bgcolor=ft.colors.PINK,
                                        color=ft.colors.WHITE
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                                padding=ft.padding.only(top=10, bottom=10)
                            )
                        ]),
                        width=250,
                        padding=15,
                        border_radius=10
                    ),
                    elevation=3
                )
                fila_productos.controls.append(tarjeta)
            
            lista_productos.controls.append(fila_productos)
        
        page.update()
    
    # Botón para volver
    boton_volver = ft.ElevatedButton(
        "Volver a selección de usuario",
        icon=ft.icons.ARROW_BACK,
        on_click=volver_seleccion
    )
    
    # Inicializar la lista de productos
    actualizar_lista_productos(productos)
    
    # Agregar todos los elementos a la página
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row([
                    titulo,
                    boton_carrito
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                subtitulo,
                ft.Divider(height=2, color=ft.colors.PINK_200),
                ft.Row([
                    busqueda,
                    filtro_categoria
                ], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=20),
                lista_productos,
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
        tienda_page(page)
    
    ft.app(target=main)
