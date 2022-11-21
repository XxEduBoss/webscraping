import mysql.connector as bbdd
from Scraping import *

def insertar_datos():

    lista_juegos = web_scraping()


    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="transfermarkt",
                            user="root",
                            password="1234",
                            autocommit=True)

    cursor = conexion.cursor()

    cursor.execute("delete from juegos where id is not null")

    cursor.execute("alter table juegos auto_increment=1")

    script_insert ="insert into juegos (imagen, nombre, precio, puntos, plataformas)" "values (%s, %s, %s, %s, %s)"

    for juego in lista_juegos:

        cursor.execute(script_insert, (juego["imagen"],
                                       juego["nombre"],
                                       juego["precio"],
                                       juego["puntos"],
                                       juego["plataformas"]))

    print("Datos insertados correctamente")

insertar_datos()


def consultar_datos():

    #Abrir conexión
    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="transfermarkt",
                            user="root",
                            password="1234",
                            autocommit=True)

    #Lista
    lista_juegos = []

    #Abrir cursor
    cursor = conexion.cursor()

    #Script de bd
    consulta = "select * from juegos"

    #Ejecuta la consulta
    cursor.execute(consulta)


    for dato in cursor.fetchall():
        juego = tuple([dato[0], dato[2], dato[3], dato[4], dato[5]])

        lista_juegos.append(juego)
    return lista_juegos

consultar_datos()