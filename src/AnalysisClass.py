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

    def getCurrencyPivot(self, currency, period):
        maximo = 0
        minimo = 2**32
        data = self.__publicClass.getCandles(currency)
        for i in range(len(data._High) - (12*period), len(data._High)):
            if maximo < data._High[i]:
                maximo = data._High[i]
                index_max = i
            if minimo > data._High[i]:
                minimo = data._High[i]
                index_min = i
        close = data._Close[len(data._Close)-1]
        pivot = (maximo+minimo+close)/3
        res1  = (2*pivot)-minimo
        sup1  = (2*pivot)-maximo
        res2  = pivot + (res1-sup1)
        sup2  = pivot - (res1-sup1)

        return [pivot,sup1,sup2,res1,res2]

