import requests
import bs4

lista_posiciones = ["player-position pos_1", "player-position pos_2", "player-position pos_3", "player-position pos_4"]


def web_scraping():

    # Paso 1 --> Tomar el código HTML de la página.
    html = requests.get("https://www.comuniazo.com/comunio-apuestas/jugadores")

    # Paso 2 --> Convertir nuestro hmtl en una sopa.
    soup = bs4.BeautifulSoup(html.content)

    # Paso 3 --> Crearnos un diccionario con la estructura.
    plantilla = {
        "posicion": None,
        "equipo": None,
        "nombre": None,
        "puntos_totales": None,
        "valor": None
    }

    # Paso 4 --> Utilizar los métodos de bs4 (Encontrar los datos que quiero obtener).
    jugadores = soup.find_all("tr", {"class": "btn"})

    lista_jugadores = []

    for jugador in jugadores:

        # Creamos una copia del diccionario plantilla.
        dic_jugador = plantilla.copy()

        # Buscar los campos y asignarlos en el diccionario.

        # NOMBRE
        dic_jugador["nombre"] = jugador.find("div", {"class": "player"}).strong.text

        # POSICION
        if jugador.find("span", {"class": "player-position pos_1"}) != None:
            dic_jugador["posicion"] = "PT"

        elif jugador.find("span", {"class": "player-position pos_2"}) != None:
            dic_jugador["posicion"] = "DFC"

        elif jugador.find("span", {"class": "player-position pos_3"}) != None:
            dic_jugador["posicion"] = "MC"

        else:
            dic_jugador["posicion"] = "DC"

        # EQUIPO
        dic_jugador["equipo"] = jugador.find("img", {"class": "team-logo"})["src"]

        # PUNTOS_TOTALES
        dic_jugador["puntos_totales"] = int(jugador.find_all("td", {"class": "tac"})[0].text)

        # VALOR
        dic_jugador["valor"] = int(jugador.find_all("td", {"class": "tac"})[6].text.replace(".", ""))

        # Añadir el jugador a mi lista de jugadores.

        lista_jugadores.append(jugador)
        print(dic_jugador)


web_scraping()
