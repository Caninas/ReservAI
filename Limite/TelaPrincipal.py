# tela inicial do sistema

import PySimpleGUI as sg

sg.theme('DarkAmber')


class TelaPrincipal:


    def mostra_mensagem(self, msg):
        sg.Popup("", msg + "\n")
