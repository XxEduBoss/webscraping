from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from datos_bbdd import insertar_datos
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from datos_bbdd import *


def aparecer_boton(panel):

    boton1 = Button(text="Hola")
    panel.add_widget(boton1)


def cargar_datos_tabla(tabla):


    #Cargar los datos
    lista_juegos = consultar_datos()

    for juego in lista_juegos:

        tabla.row_data.append(juego)



class Aplicacion(MDApp):

    def build(self):

        ventana = Screen(name="Juegos APP")

        tabla = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            size_hint=(0.7, 0.7),
            use_pagination=True,
            column_data=[
                ("id", dp(20)),
                ("nombre", dp(72)),
                ("precio", dp(20)),
                ("puntos", dp(25)),
                ("plataformas", dp(60)),

            ]
        )



        panel = BoxLayout(orientation='vertical', spacing=5)

        panel2 = BoxLayout(orientation='horizontal', spacing=5, size_hint=(1, 0.15))

        panel3 = BoxLayout(orientation='vertical', size_hint=(1, 1))



        boton1 = Button(text="Cargar")
        boton1.bind(on_press=lambda a: insertar_datos())
        boton2 = Button(text="Mostrar")
        boton2.bind(on_press=lambda a: cargar_datos_tabla(tabla))
        boton3 = Button(text="Buscar")
        boton4 = Button(text="Eliminar")

        panel2.add_widget(boton1)
        panel2.add_widget(boton2)
        panel2.add_widget(boton3)
        panel2.add_widget(boton4)

        panel.add_widget(panel2)
        panel3.add_widget(tabla)
        panel.add_widget(panel3)






        ventana.add_widget(panel)


        return ventana



Aplicacion().run()