#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Market, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os,time
from tabulate import tabulate
sys.path.append('./')
from AnalysisClass import *
from PublicClass import *
from MarketClass import *
from AccountClass import *
from DTOClass import *

class UserClass():
    def __init__(self, apikey, apisecret):
        self.__marketClass = MarketClass(apikey, apisecret) 
        self.__analysisClass = AnalysisClass() 
        self.__publicClass = PublicClass() 

    def getAnalysis(self, currency):
        result = self.__analysisClass.getCurrencyAnalysis(currency,12) 

        def calc_perc(input1, input2):
            if input1 < input2:
                result = ((input1 / input2) * 100) - 100
                result = '\033[31m'+str("%.2f" %result)+"%"+'\033[0;0m'
            else:
                result = ((input1 / input2) * 100) - 100
                result = '\033[32m'+str("%.2f" %result)+"%"+'\033[0;0m'
            return result

        if result._Wr >= -20:
            Wr = '\033[31m'+'Sobrecompra'+'\033[0;0m'
        elif result._Wr <= -80:
            Wr = '\033[32m'+'Sobrevenda'+'\033[0;0m'
        else:
            Wr = ""

        if result._Rsi > 70:
            Rsi = '\033[31m'+'Overbouht'+'\033[0;0m'
        elif result._Rsi < 30:
            Rsi = '\033[32m'+'Oversold'+'\033[0;0m'
        else:
            Rsi = ""

        if result._Obv > result._Volume:
            Obv = '\033[31m'+'Maior'+'\033[0;0m'
        elif result._Obv <= result._Volume:
            Obv = '\033[32m'+'Menor'+'\033[0;0m'
            
        Avg = calc_perc(result._Average,result._Last)
        Pivot = calc_perc(result._Pivot,result._Last)
        Sup1 = calc_perc(result._Sup[0],result._Last)
        Sup2 = calc_perc(result._Sup[1],result._Last)
        Res1 = calc_perc(result._Res[0],result._Last)
        Res2 = calc_perc(result._Res[1],result._Last)
        Bid = calc_perc(result._Bid,result._Last)
        Ask = calc_perc(result._Ask,result._Last)

        if result._DayGain >= 0:
            DayGain = '\033[32m'+str("%.2f" %result._DayGain)+ "%"+ '\033[0;0m'
        else: 
            DayGain = '\033[31m'+str("%.2f" %result._DayGain)+ "%"+ '\033[0;0m'

        table = [["Currency", currency],
                ["Pivot", "%.8f" %result._Pivot, Pivot],
                ["Sup1", "%.8f" %result._Sup[0], Sup1],
                ["Sup2", "%.8f" %result._Sup[1], Sup2],
                ["Res1", "%.8f" %result._Res[0], Res1],
                ["Res2", "%.8f" %result._Res[1], Res2],
                ["Volume", "%.0f" %result._Volume],
                ["Average", "%.8f" %result._Average, Avg],
                ["WR", "%.8f" %result._Wr, Wr],
                ["RSI", "%.8f" %result._Rsi, Rsi],
                ["OBV", "%.0f" %result._Obv, Obv],
                ["Last", "%.8f" %result._Last],
                ["Bid", "%.8f" %result._Bid, Bid],
                ["Ask", "%.8f" %result._Ask, Ask],
                ["DayGain", DayGain]]

        print tabulate(table)

    def getOpenOrders(self, currency):
        data = self.__marketClass.getOpenOrders(currency)
        if data == 'Null':
            return data 
        else:
            if data._OrderUuid == '':
                return 'Empty'
            else:
                return data._OrderUuid

    def cancel(self, currency):
        result = getOpenOrders(currency)
        
        # faz 5 tentativas antes de finalizar
        if result == 'Null':
            i = 0
            while(i < 5 and result == 'Null'):
                result = getOpenOrders(currency)
                i += 1
            if result == 'Null':
                return False
            elif result == '':
                return False
            else:
                return result
                
    def sell(self, currency, quantity, rate):
        return self.__marketClass.sellOrder(currency, quantity, rate)
    
    def buy(self, currency, quantity, rate):
        return self.__marketClass.buyOrder(currency, quantity, rate)

    def tradeSell(self, currency, quantity, rate, gain):
        gain_measure = 'Null'
        print "Medindo o Ganho"
        while (gain_measure == 'Null'):
            gain_measure = self.__analysisClass.getTradeGain(currency, rate)
            time.sleep(1)
        print "Verificando Métricas para o Ganho"
        if (gain_measure >= gain) | (gain_measure <= -1 ):
            print "Enviando Ordem de Venda"
            sell = False
            while (sell != True):
                data = self.__publicClass.getValueCurrency(currency)
                sell_rate = data._Bid
                sell = self.sell(currency, quantity, sell_rate)
                time.sleep(0.1)
            selled = False
            print "Verificando se a venda foi concluída"
            while (selled != True):
                data = self.__getOpenOrders(currency)
                if (data._NumOrders == 0):
                    selled = True
                else:
                    data = self.__publicClass.getValueCurrency(currency)
                    if sell_rate >= (data._Bid * 1.015):
                        break
                time.sleep(0.1)
            if selled == True:
                print "Venda concretizada"
            else:
                cancel = False
                while (cancel != False):
                    cancel = self.__marketClass.cancel(data._OrderUuid)
                    time.sleep(0.1)
                print "Venda não concretizada"
        else:
            self.tradeSell(currency, quantity, rate, gain)

