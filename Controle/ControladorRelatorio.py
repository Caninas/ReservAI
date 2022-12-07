from pathlib import Path

from Limite.TelaRelatorio import TelaRelatorio
from datetime import datetime as dt

import PySimpleGUI as sg
import pandas as pd

from collections import Counter

class ControladorRelatorio:
    def __init__(self, controlador_sistema, controlador_reserva, controlador_hospede, controlador_barco):
        self.__controlador_sistema = controlador_sistema

        self.__controlador_reserva = controlador_reserva
        self.__controlador_hospede = controlador_hospede
        self.__controlador_barco = controlador_barco

        self.__tela_relatorio = TelaRelatorio()

    def relatorioReservas(self):
        update = False
        data_i = None
        data_f = None
        dados = None
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu_rel_reservas(update)
            
            print(opçao, valores)

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_relatorio.close_menu_rel_reservas()
                break
            if opçao == 'exportar':
                data = {'total_reservas': len(dados[0]),'tempo_medio_estadia(dias)': dados[1],
                    'ocupacao_media_diaria_quartos(%)': dados[2], 'receita_total(R$)': dados[3], 'receita_media_diaria(R$)': dados[4]}
                df = pd.DataFrame(data, index=['valores'])
                data_inicial = data_i.strftime("%m-%d-%Y")
                data_final = data_f.strftime("%m-%d-%Y")
                try:
                    df.to_csv(f"{Path.home()}\Documents\\rel_reserva_{data_inicial}_{data_final}.csv")
                    self.__tela_relatorio.msg("Relatorio salvo com sucesso em pasta Documents!")
                except:
                    self.__tela_relatorio.msg("Falha em salvar relatorio :(")
                continue


            data_i = dt.strptime(valores['data_inicial'], '%d-%m-%y')
            data_f = dt.strptime(valores['data_final'], '%d-%m-%y')

            update = True       # para a instancia da windows nao ser recriada

            if data_i > data_f:
                self.__tela_relatorio.msg("Data final não pode ser antes da data inicial!")
                continue

            dados = self.GerarDadosReservas(data_i, data_f)
            
            self.__tela_relatorio.window_menu_rel_reservas['total_reservas'].update(f"Total de reservas: {len(dados[0])}")
            self.__tela_relatorio.window_menu_rel_reservas['tempo_medio'].update(f"Tempo médio de estadia das reservas: {dados[1]:.2f} dias")
            self.__tela_relatorio.window_menu_rel_reservas['ocupaçao_media'].update(f"Ocupação média diária dos quartos: {dados[2]:.2f}%")
            self.__tela_relatorio.window_menu_rel_reservas['receita_total'].update(f"Receita Total: R$ {dados[3]:.2f}")
            self.__tela_relatorio.window_menu_rel_reservas['receita_media_dia'].update(f"Receita média por dia: R$ {dados[4]:.2f}")
            self.__tela_relatorio.window_menu_rel_reservas['exportar'].update(disabled=False)

    def GerarDadosReservas(self, data_i, data_f):
        reservas = self.__controlador_reserva.reservas
        dias_totais = (data_f - data_i).days + 1    # inclusivo

        reservas_selecionadas = []
        receita = 0
        total_dias_reservas = 0
        tempo_medio_estadia = 0

        datas_entradas = dict()
        datas_saidas = dict()   # datas de saida / entrada de uma reserva podem ter outra reserva entrando / saindo,
                                # o que conta um dia para cada reserva no total_dias_reservas, esses dicionarios, o try except
                                # (#65) e o if (#79) resolvem o problema

        for reserva in reservas:
            # se a data da reserva se sobrepoe a data selecionada
            if dt.strptime(reserva.data_entrada, '%d-%m-%y') <= data_f and dt.strptime(reserva.data_saida, '%d-%m-%y') >= data_i:
                try:                                                                        
                    datas_entradas[reserva.quarto.numero].append(reserva.data_entrada)
                    datas_saidas[reserva.quarto.numero].append(reserva.data_saida)
                except:
                    datas_entradas[reserva.quarto.numero] = [reserva.data_entrada]
                    datas_saidas[reserva.quarto.numero] = [reserva.data_saida]

                dias_dentro = self.DiasDentro(reserva, data_i, data_f)  # quantidade de dias da reserva que estao dentro do periodo

                # somando a quantidade de dias totais da reserva
                tempo_medio_estadia += (dt.strptime(reserva.data_saida, '%d-%m-%y') - dt.strptime(reserva.data_entrada, '%d-%m-%y')).days

                receita += reserva.quarto.valor * dias_dentro

                if reserva.data_entrada in datas_saidas[reserva.quarto.numero] or reserva.data_saida in datas_entradas[reserva.quarto.numero]:
                    total_dias_reservas += (dias_dentro - 1)
                else:
                    total_dias_reservas += dias_dentro

                reservas_selecionadas.append(reserva)       # reservas no periodo

        print(dias_totais)
        if len(reservas_selecionadas) != 0:             # if para o caso de reservas_selecionadas = 0 (divisao por 0)
            tempo_medio_estadia = tempo_medio_estadia / len(reservas_selecionadas)
        else:
            tempo_medio_estadia = 0

        ocupaçao_media = (total_dias_reservas / (dias_totais * 8)) * 100    # porcentagem do tempo selecionado que os quartos ficaram com reservas / ocupado
        receita_diaria = receita / dias_totais

        return [reservas_selecionadas, tempo_medio_estadia, ocupaçao_media, receita, receita_diaria]

    def DiasDentro(self, reserva, data_i, data_f):
        entrada = dt.strptime(reserva.data_entrada, '%d-%m-%y')
        saida = dt.strptime(reserva.data_saida, '%d-%m-%y')

        if entrada <= data_i and data_i < saida <= data_f:              # diferentes formas de contas os dias dentro de um periodo
            return (saida - data_i).days + 1
        elif saida >= data_f and data_i <= entrada <= data_f:
            return (data_f - entrada).days + 1
        elif entrada <= data_i and saida >= data_f:
            return (data_f - data_i).days + 1
        elif data_i <= entrada <= data_f and data_i <= saida <= data_f:
            return (saida - entrada).days + 1
        else:
            return 1

    def relatorioHospedes(self):
        update = False
        data_i = None
        data_f = None
        dados = None
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu_rel_hospedes(update)
            
            print(opçao, valores)

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_relatorio.close_menu_rel_hospedes()
                break
            if opçao == 'exportar':
                data = {'total_reservas': len(dados[0]),'tempo_medio_estadia(dias)': dados[1],
                    'ocupacao_media_diaria_quartos(%)': dados[2], 'receita_total(R$)': dados[3], 'receita_media_diaria(R$)': dados[4]}
                df = pd.DataFrame(data, index=['valores'])
                data_inicial = data_i.strftime("%m-%d-%Y")
                data_final = data_f.strftime("%m-%d-%Y")
                try:
                    df.to_csv(f"{Path.home()}\Documents\\rel_reserva_{data_inicial}_{data_final}.csv")
                    self.__tela_relatorio.msg("Relatorio salvo com sucesso em pasta Documents!")
                except:
                    self.__tela_relatorio.msg("Falha em salvar relatorio :(")
                continue


            data_i = dt.strptime(valores['data_inicial'], '%d-%m-%y')
            data_f = dt.strptime(valores['data_final'], '%d-%m-%y')

            update = True       # para a instancia da windows nao ser recriada

            if data_i > data_f:
                self.__tela_relatorio.msg("Data final não pode ser antes da data inicial!")
                continue


            dados = self.gerarDadosHospedes()
                
            self.__tela_relatorio.window_menu_rel_hospedes['total_hospedes'].update(f"Total de hóspedes: {dados[0]}")
            self.__tela_relatorio.window_menu_rel_hospedes['idade_media'].update(f"Média de idade dos hóspedes: {dados[1]:.2f} anos")
            self.__tela_relatorio.window_menu_rel_hospedes['sexo_masc'].update(f"Hóspedes masculinos: {dados[2]}%")
            self.__tela_relatorio.window_menu_rel_hospedes['sexo_fem'].update(f"Hóspedes femininos: {dados[3]}%")
            self.__tela_relatorio.window_menu_rel_hospedes['sexo_outros'].update(f"Hóspedes outros gêneros: {dados[4]}%")
            self.__tela_relatorio.window_menu_rel_hospedes['cidade1'].update(f"1° cidade mais frequente: {dados[5]}")
            self.__tela_relatorio.window_menu_rel_hospedes['cidade2'].update(f"2° cidade mais frequente {dados[6]}")
            self.__tela_relatorio.window_menu_rel_hospedes['cidade3'].update(f"3° cidade mais frequente {dados[7]}")
            self.__tela_relatorio.window_menu_rel_hospedes['exportar'].update(disabled=False)


    def gerarDadosHospedes(self):
        qtd_hospedes = self.conta_hospedes()
        media_idade = self.calculaIdadeMedia()
        fem, masc, outros = self.calcula_genero()
        cidade1, cidade2, cidade3 = self.calcula_cidades()

        return [qtd_hospedes, media_idade, fem, masc, outros, cidade1, cidade2, cidade3]

    def conta_hospedes(self):
        qtd = 0
        for hospede in self.__controlador_hospede.hospedes:
            qtd = qtd + 1
        
        return qtd

    def calculaIdadeMedia(self):

        qtd_hospedes = self.conta_hospedes()

        idade_total = 0

        for hospede in self.__controlador_hospede.hospedes:
            try:
                dias = dt.now() - dt.strptime(hospede.data_nascimento , '%d-%m-%Y')
            except:
                dias = dt.now() - dt.strptime('09-03-2022' , '%m-%d-%Y')
            idade = dias.days/365
            idade_total = idade_total + idade
       
        media = idade_total/qtd_hospedes

        return media


    def calcula_genero(self):
        
        fem = 0
        masc = 0
        outros = 0

        qtd_hospedes = self.conta_hospedes()

        for hospede in self.__controlador_hospede.hospedes:
            if hospede.sexo == 'f' or hospede.sexo == 'F':
                fem += 1
            elif hospede.sexo == 'm' or hospede.sexo == 'M':
                masc += 1
            else:
                outros += 1

        media_fem = fem / qtd_hospedes *100
        media_masc = masc / qtd_hospedes *100
        media_outros = outros / qtd_hospedes *100
        
        print (media_fem, media_masc, media_outros)

        return [media_fem, media_masc, media_outros]


    def calcula_cidades(self):
        lista_cidades = []
        qtd_cidades = 0

        for hospede in self.__controlador_hospede.hospedes:
            lista_cidades.append(hospede.end_cidade)
            qtd_cidades += 1

        frequencia = Counter(lista_cidades).most_common()
        cidade_1, cidade_2, cidade_3 = frequencia[0], frequencia[1], frequencia[2]

        porc_1 = cidade_1[1] / qtd_cidades * 100
        porc_2 = cidade_2[1] / qtd_cidades * 100
        porc_3 = cidade_3[1] / qtd_cidades * 100

        resultado1 = (f"{cidade_1[0]}: {porc_1}%")
        resultado2 = (f"{cidade_2[0]}: {porc_2}%")
        resultado3 = (f"{cidade_3[0]}: {porc_3}%")

        print (resultado1, resultado2, resultado3)
        return [resultado1, resultado2, resultado3]


    def abre_tela(self):                 # clica quarto mapa (recebe numero dele aqui (botao) e dia selecionado)
<<<<<<< HEAD
        lista_opçoes = {"rel_reservas": self.relatorioReservas, "rel_hospedes": self.relatorioHospedes,
                        "rel_passeios": print}
=======
        lista_opçoes = {"rel_reservas": self.relatorioReservas, "rel_hospedes": print,
                        "rel_passeios": self.relatorioPasseios}
>>>>>>> 9d002e22100f0bd01fa5282212b880003b6c1e9c
        
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu()
            print(opçao, valores)
            self.__tela_relatorio.close_menu()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                break 

            lista_opçoes[opçao]()
    
    def relatorioPasseios(self):
        update = False
        data_i = None
        data_f = None
        dados = None
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu_rel_passeios(update)
            
            print(opçao, valores)

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_relatorio.close_menu_rel_passeios()
                break

            if opçao == 'exportar':
                data = {'total_passeios': len(dados[0]),
                    'ocupacao_media_diaria_barcos(%)': dados[1], 'receita_total(R$)': dados[2], 'receita_media_diaria(R$)': dados[3]}
                df = pd.DataFrame(data, index=['valores'])
                data_inicial = data_i.strftime("%m-%d-%Y")
                data_final = data_f.strftime("%m-%d-%Y")
                try:
                    df.to_csv(f"{Path.home()}\Documents\\rel_passeios_{data_inicial}_{data_final}.csv")
                    self.__tela_relatorio.msg("Relatorio salvo com sucesso em pasta Documents!")
                except:
                    self.__tela_relatorio.msg("Falha em salvar relatorio :(")
                continue

            data_i = dt.strptime(valores['data_inicial'], '%d-%m-%y')
            data_f = dt.strptime(valores['data_final'], '%d-%m-%y')

            update = True       # para a instancia da windows nao ser recriada

            if data_i > data_f:
                self.__tela_relatorio.msg("Data final não pode ser antes da data inicial!")
                continue

            dados = self.GerarDadosPasseios(data_i, data_f)
            
            self.__tela_relatorio.window_menu_rel_passeios['total_reservas'].update(f"Total de passeios: {len(dados[0])}")
            self.__tela_relatorio.window_menu_rel_passeios['ocupaçao_media'].update(f"Ocupação média diária dos barcos: {dados[1]:.2f}%")
            self.__tela_relatorio.window_menu_rel_passeios['receita_total'].update(f"Receita Total: R$ {dados[2]:.2f}")
            self.__tela_relatorio.window_menu_rel_passeios['receita_media_dia'].update(f"Receita média por dia: R$ {dados[3]:.2f}")
            self.__tela_relatorio.window_menu_rel_passeios['exportar'].update(disabled=False)

    def GerarDadosPasseios(self, data_i, data_f):
        reservas_barcos = self.__controlador_barco.reservas_barcos
        dias_totais = (data_f - data_i).days + 1    # inclusivo

        reservas_selecionadas = []
        receita = 0
        total_dias_reservas = 0

        for reserva in reservas_barcos:
            # se a data da reserva se sobrepoe a data selecionada
            if dt.strptime(reserva.data_reserva, '%d-%m-%y') <= data_f and dt.strptime(reserva.data_reserva, '%d-%m-%y') >= data_i:

                receita += reserva.valor

                total_dias_reservas += 1
                reservas_selecionadas.append(reserva)       # reservas no periodo

        print(dias_totais)

        ocupaçao_media = (total_dias_reservas / (dias_totais * 3)) * 100    # porcentagem do tempo selecionado que os quartos ficaram com reservas / ocupado
        receita_diaria = receita / dias_totais

        return [reservas_selecionadas, ocupaçao_media, receita, receita_diaria]


                




