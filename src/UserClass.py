#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Market, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os
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
                ["Ask", "%.8f" %result._Ask, Ask]]

        print tabulate(table)

