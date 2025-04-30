import flet as ft

def main(page: ft.Page):
    page.title = "Selecciona tu tipo de usuario"
    page.bgcolor = ft.colors.WHITE
    
    # Add scroll to the main page
    page.scroll = ft.ScrollMode.AUTO

    def navigate(e):
        # Navigate to the selected user type page
        user_type = e.control.data
        try:
            if user_type == "cuidador":
                # Importación tardía para evitar importación circular
                from cuidador import cuidador_page
                cuidador_page(page)
            elif user_type == "familiar":
                # Importación tardía para evitar importación circular
                from familiar import familiar_page
                familiar_page(page)
            elif user_type == "adulto_mayor":
                # Importación tardía para evitar importación circular
                from adulto_mayor import adulto_mayor_page
                adulto_mayor_page(page)
            elif user_type == "medico":
                # Importación tardía para evitar importación circular
                from medico import medico_page
                medico_page(page)
            elif user_type == "tienda":
                # Importación tardía para evitar importación circular
                from tienda_dulces import tienda_page
                tienda_page(page)
        except Exception as e:
            print(f"Error al navegar: {e}")
            page.snack_bar = ft.SnackBar(content=ft.Text(f"Error al cargar: {str(e)}"))
            page.snack_bar.open = True
            page.update()
    
    options = [
        ("Cuidadores", ft.colors.PURPLE, "cuidador", ft.icons.HEALTH_AND_SAFETY),
        ("Familiares", ft.colors.BLUE, "familiar", ft.icons.FAMILY_RESTROOM),
        ("Adultos Mayores", ft.colors.TEAL, "adulto_mayor", ft.icons.ELDERLY),
        ("Médicos", ft.colors.RED, "medico", ft.icons.MEDICAL_SERVICES),
        ("Tienda", ft.colors.PINK, "tienda", ft.icons.STORE),
    ]
    
    buttons = []
    for label, color, data, icon in options:
        btn = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(icon, color=ft.colors.WHITE),
                    ft.Text(label, color=ft.colors.WHITE, size=16, weight=ft.FontWeight.W_500)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=color,
            data=data,
            on_click=navigate,
            width=280,
            height=60,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                elevation=5,
            )
        )
        buttons.append(btn)
    
    title = ft.Text(
        "Bienvenido a Vitalis", 
        size=32, 
        color=ft.colors.BLACK, 
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    subtitle = ft.Text(
        "Selecciona tu tipo de usuario para continuar", 
        size=18, 
        color=ft.colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )
    
    # App logo/icon
    logo = ft.Icon(
        ft.icons.FAVORITE,
        size=80,
        color=ft.colors.BLUE
    )
    
    # Make the main column scrollable
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    logo,
                    title,
                    subtitle,
                    ft.Divider(height=2, color=ft.colors.GREY_300),
                    *buttons
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
            ),
            alignment=ft.alignment.center,
            expand=True,
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
