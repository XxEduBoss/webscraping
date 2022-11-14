import requests
import bs4


def web_scraping():

    # Paso 1 --> Tomar el código HTML de la página.
    html = requests.get("https://www.game.es/VIDEOJUEGOS/PLAYSTATION-4")

    # Paso 2 --> Convertir nuestro hmtl en una sopa.
    soup = bs4.BeautifulSoup(html.content)

    # Paso 3 --> Crearnos un diccionario con la estructura.
    plantilla = {
        "Imagen": None,
        "Nombre": None,
        "Precio": None,
        "Puntos": None,
        "Plataformas": None
    }

    # Paso 4 --> Utilizar los métodos de bs4 (Encontrar los datos que quiero obtener).
    juegos = soup.find_all("article", {"class": "product-carousel-item"})

    lista_juegos = []

    for juego in juegos:

        # Creamos una copia del diccionario plantilla.
        dic_juegos = plantilla.copy()

        # Buscar los campos y asignarlos en el diccionario.

        # IMAGEN
        dic_juegos["Imagen"] = juego.find("img", {"class": "cover"})["src"]

        # NOMBRE
        dic_juegos["Nombre"] = juego.find("div", {"class": "product-carousel-item-title u-mb0"}).find("a").text.translate({ord('\r'): ' '}).translate({ord('\n'): ' '}).replace("      ", "").replace("  ", "")

        # PRECIO
        dic_juegos["Precio"] = juego.find("span", {"class": "int"}).text + juego.find("span", {"class": "decimal"}).text + juego.find("span", {"class": "currency"}).text

        # PUNTOS
        dic_juegos["Puntos"] = juego.find("small", {"class": "text-primary"}).text.replace("Puntos: ", "")

        # PLATAFORMAS
        dic_juegos["Plataformas"] = juego.find("div", {"class": "product-carousel-item-platform"}).text.translate({ord('\n'): ' '}).replace("4 P", "4, P").replace("5 Xbox One X", "5, Xbox One X").replace("4 X", "4 y X").replace("e X", "e y X").replace("5 X", "5 y X").replace("h P", "h, P")


        # Añadir el jugador a mi lista de jugadores.

        lista_juegos.append(juego)
        print(dic_juegos)


web_scraping()
