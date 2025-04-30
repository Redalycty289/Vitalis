import flet as ft
import random
import asyncio
from menu_adulto_mayor import main as menu_principal

def main(page: ft.Page):
    page.title = "Juego de Memoria"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE  

    # Add scroll to the main page
    page.scroll = ft.ScrollMode.AUTO

    # Duplicate symbols for matching pairs
    symbols = [
        "🍎", "🍌", "🍇", "🍉", "🍓", "🍒", "🍍", "🥝"
    ] * 2
    random.shuffle(symbols)

    revealed_cards = []
    matched_cards = []
    buttons = []
    game_active = False  
    time_left = 300  # 5 minutes in seconds

    timer_text = ft.Text("Tiempo restante: 5:00", size=24, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
    result_text = ft.Text("", size=30, color=ft.colors.GREEN, weight=ft.FontWeight.BOLD)

    async def update_timer():
        """Cronómetro que cuenta hasta 0"""
        nonlocal time_left, game_active
        try:
            while time_left > 0 and game_active:
                await asyncio.sleep(1)
                time_left -= 1
                minutes = time_left // 60
                seconds = time_left % 60
                timer_text.value = f"Tiempo restante: {minutes}:{seconds:02d}"
                page.update()

            # Check if time's up and player hasn't won yet
            if time_left == 0 and len(matched_cards) < len(symbols):
                game_active = False
                result_text.value = "¡Tiempo agotado! Perdiste."
                result_text.color = ft.colors.RED
                result_text.update()
                disable_buttons()
        except Exception as e:
            print(f"Timer error: {e}")
    
    def volver_menu(e):
        # Stop any running timer by setting game_active to False
        nonlocal game_active
        game_active = False
        # Clean the page and navigate back
        page.clean()
        menu_principal(page)

    def disable_buttons():
        """Deshabilita todas las cartas al ganar o perder."""
        for btn in buttons:
            btn.disabled = True
            btn.update()

    async def on_click(e):
        nonlocal game_active  
        # Ignore clicks if game is not active
        if not game_active:
            return  

        index = int(e.control.data)

        # Skip cards that are already matched or revealed
        if index in matched_cards or index in revealed_cards:
            return

        # Reveal the card
        e.control.text = symbols[index]
        e.control.bgcolor = "#5dc7ac"  
        e.control.update()
        revealed_cards.append(index)

        # Check if two cards are revealed
        if len(revealed_cards) == 2:
            await asyncio.sleep(0.8)  # Slightly shorter delay for better gameplay

            # Check if cards match
            if symbols[revealed_cards[0]] == symbols[revealed_cards[1]]:
                matched_cards.extend(revealed_cards)
            else:
                # Hide non-matching cards
                for i in revealed_cards:
                    buttons[i].text = " "
                    buttons[i].bgcolor = "#7b37b9"  
                    buttons[i].update()

            revealed_cards.clear()

        # Check for win condition
        if len(matched_cards) == len(symbols):
            game_active = False
            disable_buttons()
            result_text.value = "¡Ganaste!"
            result_text.color = ft.colors.GREEN
            result_text.update()
            # Show replay button
            start_button.text = "Jugar de nuevo"
            start_button.visible = True
            start_button.update()

    def start_game(e):
        """Inicia el juego y el cronómetro"""
        nonlocal game_active, time_left, matched_cards, revealed_cards
        
        # Reset game state
        game_active = True
        time_left = 300
        matched_cards = []
        revealed_cards = []
        result_text.value = ""
        result_text.update()
        
        # Shuffle cards for new game
        random.shuffle(symbols)
        
        # Reset all buttons
        for i, btn in enumerate(buttons):
            btn.text = " "
            btn.bgcolor = "#7b37b9"
            btn.disabled = False
            btn.update()

        start_button.visible = False
        start_button.update()

        # Start timer
        page.run_task(update_timer)

    # Create card buttons
    for i in range(len(symbols)):
        button = ft.ElevatedButton(
            " ",  
            width=90,
            height=90,
            data=i,  
            bgcolor="#7b37b9",  
            color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),  
                padding=ft.Padding(20, 20, 20, 20),
            ),
            on_click=on_click,
            disabled=True,  # Start with disabled buttons
        )
        buttons.append(button)

    # Create responsive grid layout based on screen width
    def create_rows(e=None):
        rows.controls = []
        screen_width = page.width or 600
        
        # Adjust number of cards per row based on screen width
        cards_per_row = 4
        if screen_width < 400:
            cards_per_row = 2
        elif screen_width < 600:
            cards_per_row = 3
            
        for i in range(0, len(buttons), cards_per_row):
            rows.controls.append(
                ft.Row(
                    controls=buttons[i:i + cards_per_row], 
                    spacing=10, 
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        page.update()
    
    rows = ft.Column(spacing=10, alignment=ft.MainAxisAlignment.CENTER)
    
    # Header with icon and title
    header = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.MEMORY, color=ft.colors.BLACK, size=40),
            ft.Text("Juego de Memoria", size=28, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Start button
    start_button = ft.ElevatedButton(
        "Iniciar Juego",
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding(15, 30, 15, 30),
        ),
        on_click=start_game
    )
    
    # Botón para volver al menú
    volver_button = ft.ElevatedButton(
        "Volver al Menú",
        bgcolor=ft.colors.RED_400,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding(10, 20, 10, 20),
        ),
        on_click=volver_menu
    )

    # Instructions text
    instructions = ft.Text(
        "Encuentra todas las parejas de frutas antes de que se acabe el tiempo.",
        size=16, 
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )

    # Make sure the main column is scrollable too
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    header,
                    instructions,
                    rows,
                    ft.Row([start_button], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([timer_text], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([result_text], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([volver_button], alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
        )
    )
    
    # Make layout responsive
    page.on_resize = create_rows
    create_rows()  # Initial layout

if __name__ == "__main__":
  ft.app(target=main)

