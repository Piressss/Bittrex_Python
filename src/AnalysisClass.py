#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe que gera analises do mercado 

import sys,os
sys.path.append('./')
from PublicClass import *
from DTOClass import *

class AnalysisClass():
    def __init__(self):
        self.__publicClass = PublicClass() 

    # Metodo para calculo do Pivot, Resistencia e Suporte
    def getCurrencyPivot(self, currency, period):
        result = CurrencyAnalysisData()  
        # Preciso iniciliazar o maximo e minimo
        maximo = 0
        minimo = 2**32
        data = self.__publicClass.getCandles(currency)
        # encontro o maximo e o minimo do period estipulado
        for i in range(len(data._High) - (12*period), len(data._High)):
            if maximo < data._High[i]:
                maximo = data._High[i]
                index_max = i
            if minimo > data._High[i]:
                minimo = data._High[i]
                index_min = i
        # valor de fechamento do periodo
        close = data._Close[len(data._Close)-1]
        # calculo das informacoes
        pivot           = (maximo+minimo+close)/3
        result._Pivot   = pivot 
        res1            = (2*pivot)-minimo
        result._Res[0]  = res1 
        sup1            = (2*pivot)-maximo
        result._Sup[0]  = sup1 
        result._Res[1]  = pivot + (res1-sup1)
        result._Sup[1]  = pivot - (res1-sup1)

        return result 

    # Metodo para calculo da media simples
    def getCurrencyAverage(self, currency, period):
        data = self.__publicClass.getCandles(currency)
        # inicializo o accumulador
        acc = 0
        # acumulo os valores de fechamento do periodo
        for i in range(len(data._Close) - (12*period), len(data._Close)):
            acc += data._Close[i]
        # calculo a media
        media = acc / (len(data._Close) - (len(data._Close)-(12*period)))
        return media
    
    # Metodo para calculo do Williams %R
    def getCurrencyWR(self, currency, period):
        # Preciso iniciliazar o maximo e minimo
        maximo = 0
        minimo = 2**32
        data = self.__publicClass.getCandles(currency)
        # encontro o maximo e o minimo do periodo estipulado
        for i in range(len(data._High) - (12*period), len(data._High)):
            if maximo < data._High[i]:
                maximo = data._High[i]
            if minimo > data._High[i]:
                minimo = data._High[i]
            if i == len(data._High) - 1:
                fechamento = data._Close[i]
        # Calculo do WR 
        wr = (maximo - fechamento) / (maximo - minimo) * (-100)
        return wr

    # Metodo para calculo do RSI
    def getCurrencyRSI(self, currency):
        # Preciso iniciliazar as variaveis
        incr = 0
        decr = 0
        data = self.__publicClass.getCandles(currency)
        # encontro o maximo e o minimo do periodo estipulado
        for i in range(len(data._Open) - 14, len(data._Open)):
            if data._Open[i] > data._Close[i]:
                decr += data._Close[i]
            elif data._Open[i] < data._Close[i]:
                incr += data._Close[i]

        # Calculo do RSI
        incr = incr/14
        decr = decr/14
        rsi  = 100 - (100/(1+(incr/decr)))
        return rsi

    # Metodo para calculo do OBV
    def getCurrencyOBV(self, currency, period):
        data = self.__publicClass.getCandles(currency)
        volume = 0
        # encontro o maximo e o minimo do periodo estipulado
        for i in range(len(data._Open) - (12*period), len(data._Open)):
            if data._Open[i] < data._Close[i]:
                volume += data._Volume[i]
            elif data._Open[i] > data._Close[i]:
                volume -= data._Volume[i]
        return volume

    # Metodo que executa todas as Analises
    def getCurrencyAnalysis(self, currency, period):
        data = CurrencyAnalysisData()  
        # pivot
        data = self.getCurrencyPivot(currency, period)
        # media
        data._Average = self.getCurrencyAverage(currency, period)
        # WR
        data._Wr = self.getCurrencyWR(currency, period)
        # RSI
        data._Rsi = self.getCurrencyRSI(currency)
        # OBV
        data._Obv = self.getCurrencyOBV(currency, period)

        # Para os demais valores preciso fazer outra consulta
        value = self.__publicClass.getValueCurrency(currency)
        data._Volume = value._Volume
        data._Bid    = value._Bid
        data._Ask    = value._Ask
        data._Last   = value._Last

        return data 

    # Metodo que calcula o ganho de uma compra no momento
    def getTradeGain(self, currency, buy_rate):
        # Consulto o valor da moeda
        value = self.__publicClass.getValueCurrency(currency)

        return (((value._Last/buy_rate) -1) * 100) 
