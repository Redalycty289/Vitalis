import flet as ft

# Lista de productos (simula los datos del marketplace)
products = [
    {
        "id": 1,
        "name": "Paracetamol 500mg",
        "brand": "MediCare",
        "price": 9.99,
        "image": "https://placehold.co/200x200?text=Paracetamol",
        "category": "Analgésico",
        "description": "Analgésico y antipirético para aliviar dolores leves y moderados, así como para reducir la fiebre.",
        "dosage": "1-2 comprimidos cada 6-8 horas, sin exceder 8 en 24 horas.",
        "sideEffects": ["Náuseas", "Dolor abdominal", "Erupción cutánea"],
        "stock": 45
    },
    {
        "id": 2,
        "name": "Ibuprofeno 400mg",
        "brand": "HealthPlus",
        "price": 12.50,
        "image": "https://placehold.co/200x200?text=Ibuprofeno",
        "category": "Antiinflamatorio",
        "description": "AINE que alivia el dolor, la inflamación y reduce la fiebre.",
        "dosage": "1 comprimido cada 6-8 horas después de las comidas, sin exceder 3 en 24 horas.",
        "sideEffects": ["Dolor de estómago", "Acidez", "Mareos", "Dolor de cabeza"],
        "stock": 32
    },
    {
        "id": 3,
        "name": "Amoxicilina 250mg",
        "brand": "PharmaCure",
        "price": 18.75,
        "image": "https://placehold.co/200x200?text=Amoxicilina",
        "category": "Antibiótico",
        "description": "Antibiótico de amplio espectro para tratar diversas infecciones.",
        "dosage": "1 cápsula cada 8 horas durante 7-10 días según prescripción médica.",
        "sideEffects": ["Diarrea", "Náuseas", "Erupción cutánea", "Candidiasis"],
        "stock": 20
    },
    {
        "id": 4,
        "name": "Loratadina 10mg",
        "brand": "AllerFree",
        "price": 7.25,
        "image": "https://placehold.co/200x200?text=Loratadina",
        "category": "Antihistamínico",
        "description": "Antihistamínico que alivia síntomas de alergias.",
        "dosage": "1 comprimido al día.",
        "sideEffects": ["Somnolencia", "Sequedad de boca", "Dolor de cabeza"],
        "stock": 50
    },
    {
        "id": 5,
        "name": "Omeprazol 20mg",
        "brand": "GastroHealth",
        "price": 15.30,
        "image": "https://placehold.co/200x200?text=Omeprazol",
        "category": "Antiácido",
        "description": "Inhibidor de la bomba de protones para tratar úlceras y reflujo.",
        "dosage": "1 cápsula al día antes del desayuno.",
        "sideEffects": ["Dolor de cabeza", "Náuseas", "Diarrea", "Dolor abdominal"],
        "stock": 38
    },
    {
        "id": 6,
        "name": "Vitamina C 1000mg",
        "brand": "VitaPlus",
        "price": 13.45,
        "image": "https://placehold.co/200x200?text=Vitamina+C",
        "category": "Suplemento",
        "description": "Suplemento dietético que apoya el sistema inmunológico.",
        "dosage": "1 comprimido al día con alimentos.",
        "sideEffects": ["Malestar estomacal", "Acidez", "Diarrea en altas dosis"],
        "stock": 60
    }
]


# Función para mostrar mensajes (snack bar)
def snack_bar_show(page: ft.Page, message: str):
    page.snack_bar = ft.SnackBar(ft.Text(message))
    page.snack_bar.open = True
    page.update()


# Función para crear la barra de navegación (MedicoNavbar)
def nav_bar(page: ft.Page) -> ft.Row:
    return ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.MENU, on_click=lambda e: page.go("/")),
            ft.IconButton(icon=ft.icons.SHOP, on_click=lambda e: page.go("/marketplace")),
            ft.IconButton(
                icon=ft.icons.LOGIN,
                on_click=lambda e: snack_bar_show(page, "Login button clicked")
            ),
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                on_click=lambda e: snack_bar_show(page, "Settings button clicked")
            ),
        ],
        alignment="spaceEvenly",
        spacing=20
    )


# Página de Inicio (Index)
def create_index_view(page: ft.Page) -> ft.View:
    return ft.View(
        route="/",
        controls=[
            ft.Column(
                controls=[
                    ft.AppBar(title=ft.Text("Index Page")),
                    ft.Container(
                        content=ft.Text("Bienvenido a la aplicación"),
                        alignment=ft.alignment.center,
                        padding=20,
                    ),
                    nav_bar(page)
                ],
                expand=True
            )
        ]
    )


# Página del Marketplace
def create_marketplace_view(page: ft.Page) -> ft.View:
    search_field = ft.TextField(label="Buscar medicamentos, suplementos...", width=300)
    product_cards = ft.Column()

    # Función para actualizar las tarjetas según la búsqueda
    def update_product_cards(e):
        product_cards.controls.clear()
        query = search_field.value.lower() if search_field.value else ""
        filtered = [
            p
            for p in products
            if query in p["name"].lower()
            or query in p["brand"].lower()
            or query in p["category"].lower()
        ]
        for p in filtered:
            card = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Image(src=p["image"], width=100, height=100, fit=ft.ImageFit.COVER),
                        ft.Text(p["name"], weight="bold"),
                        ft.Text(f"${p['price']:.2f}", color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                bgcolor=ft.colors.WHITE,
                padding=10,
                border_radius=10,
                border=ft.border.all(1, ft.colors.GREY),
                width=140,
                height=180,
                on_click=lambda e, pid=p["id"]: page.go(f"/marketplace/{pid}"),
            )
            product_cards.controls.append(card)
        page.update()

    search_field.on_change = update_product_cards
    update_product_cards(None)

    return ft.View(
        route="/marketplace",
        controls=[
            ft.Column(
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                        title=ft.Text("Marketplace")
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(controls=[search_field], alignment=ft.MainAxisAlignment.CENTER),
                                product_cards,
                            ],
                            spacing=20,
                        ),
                        padding=20,
                    ),
                    nav_bar(page),
                ],
                expand=True,
            )
        ],
    )


# Página de Detalles del Producto
def create_product_details_view(page: ft.Page, product_id: int) -> ft.View:
    # Buscar el producto por id
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return create_notfound_view(page)

    # Estado de cantidad (inicia en 1)
    qty = 1
    qty_text = ft.Text(str(qty), width=30, text_align=ft.TextAlign.CENTER)

    def decrease(e):
        nonlocal qty
        if qty > 1:
            qty -= 1
            qty_text.value = str(qty)
            page.update()

    def increase(e):
        nonlocal qty
        stock = product.get("stock", 10)
        if qty < stock:
            qty += 1
            qty_text.value = str(qty)
            page.update()

    def add_to_cart(e):
        snack_bar_show(page, f"{qty} {product['name']} añadido al carrito")

    return ft.View(
        route=page.route,  # La ruta ya viene configurada, por ejemplo: /marketplace/1
        controls=[
            ft.Column(
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/marketplace")),
                        title=ft.Text(product["name"], max_lines=1)
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(src=product["image"], width=200, height=200, fit=ft.ImageFit.COVER),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Categoría: {product['category']}"),
                                        ft.Text(f"Marca: {product['brand']}"),
                                        ft.Text(f"Precio: ${product['price']:.2f}", weight="bold", color=ft.colors.GREEN),
                                        ft.Text(f"Disponible: {product.get('stock', 'N/A')} unidades"),
                                        ft.Row(
                                            controls=[
                                                ft.IconButton(icon=ft.icons.REMOVE_CIRCLE, on_click=decrease),
                                                qty_text,
                                                ft.IconButton(icon=ft.icons.ADD_CIRCLE, on_click=increase),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=10,
                                        ),
                                        ft.ElevatedButton("Añadir al carrito", on_click=add_to_cart),
                                    ],
                                    spacing=10,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        padding=20,
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Detalles del producto", style="headlineSmall"),
                                ft.Text(product.get("description", "")),
                                ft.Text("Dosificación: " + product.get("dosage", "")),
                                ft.Text("Efectos secundarios: " + ", ".join(product.get("sideEffects", []))),
                            ],
                            spacing=5,
                        ),
                        padding=20,
                    ),
                    nav_bar(page),
                ],
                expand=True,
            )
        ],
    )


# Página NotFound
def create_notfound_view(page: ft.Page) -> ft.View:
    return ft.View(
        route=page.route,
        controls=[
            ft.Column(
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                        title=ft.Text("404 - Página no encontrada")
                    ),
                    ft.Container(
                        content=ft.Text("Lo sentimos, la página que buscas no existe.", color=ft.colors.RED),
                        alignment=ft.alignment.center,
                        padding=20,
                    ),
                    nav_bar(page),
                ],
                expand=True,
            )
        ],
    )


# Función principal de la aplicación
def main(page: ft.Page):
    page.title = "Marketplace con Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    # Función que se ejecuta cuando la ruta cambia
    def route_change(e):
        route = page.route
        if route == "/" or route == "":
            view = create_index_view(page)
        elif route == "/marketplace":
            view = create_marketplace_view(page)
        elif route.startswith("/marketplace/"):
            try:
                product_id = int(route.split("/")[-1])
                view = create_product_details_view(page, product_id)
            except Exception:
                view = create_notfound_view(page)
        else:
            view = create_notfound_view(page)
        page.views.clear()
        page.views.append(view)
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")


ft.app(target=main)