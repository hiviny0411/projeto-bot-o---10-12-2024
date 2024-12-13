import flet as ft

def main(page: ft.Page):

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    def slider_changed(e):
        spotify_logo.width = e.control.value
        spotify_logo.height = e.control.value
        t.value = f"Slider changed to {e.control.value}"
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    c = ft.Switch(label="Light theme", on_change=theme_changed)

    spotify_logo = ft.Image(
        src="https://cdn.pixabay.com/photo/2016/10/22/00/15/spotify-1759471_1280.jpg",
        width=100,
        height=100
    )

    music_list = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Imagem", width=100, weight=ft.FontWeight.BOLD),
                    ft.Text("Música", width=200, weight=ft.FontWeight.BOLD),
                    ft.Text("Artista", width=200, weight=ft.FontWeight.BOLD),
                    ft.Text("Duração", width=100, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="https://i.discogs.com/2TWNEM1x2nMMG9vm56FDvD8zgOdVPeYrOJluJNowSTE/rs:fit/g:sm/q:90/h:525/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1MzM1/NjkyLTE1ODk5MTU1/OTAtODYyMS5qcGVn.jpeg", width=40, height=40),
                    ft.Text("Blinding Lights", width=200),
                    ft.Text("The Weeknd", width=200),
                    ft.Text("3:20", width=100),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyK07s21sfqsfdB4Wx9jZyqPvlBz6EEYzZ5A&s", width=40, height=40),
                    ft.Text("Shape of You", width=200),
                    ft.Text("Ed Sheeran", width=200),
                    ft.Text("3:53", width=100),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="https://i1.sndcdn.com/artworks-hSYY3M1z3IiDRrFK-7vTNMA-t500x500.jpg", width=40, height=40),
                    ft.Text("Levitating", width=200),
                    ft.Text("Dua Lipa", width=200),
                    ft.Text("3:23", width=100),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="https://i.scdn.co/image/ab67616d0000b27341e31d6ea1d493dd77933ee5", width=40, height=40),
                    ft.Text("Stay", width=200),
                    ft.Text("Justin Bieber & The Kid LAROI", width=200),
                    ft.Text("2:21", width=100),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="https://i.scdn.co/image/ab67616d00001e02b5097b81179824803664aaaf", width=40, height=40),
                    ft.Text("Save Your Tears", width=200),
                    ft.Text("The Weeknd", width=200),
                    ft.Text("3:35", width=100),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    t = ft.Text()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    page.add(
        c, 
        ft.Column(
            controls=[
                ft.Row(
                    controls=[spotify_logo],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                music_list,
                ft.Text("Slider to adjust the size of the Spotify logo:"),
                ft.Slider(min=50, max=200, divisions=30, label="{value}px", on_change=slider_changed),
                t
            ]
        )
    )

ft.app(main)
