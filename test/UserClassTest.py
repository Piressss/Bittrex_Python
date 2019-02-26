#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from AnalysisClass import *
from PublicClass import *
from UserClass import *
from DTOClass import *

key=''
secret=''

c = UserClass(key,secret)

if sys.argv[1] != 'sell' and sys.argv[1] != 'buy':
    currency = sys.argv[1]
    c.getAnalysis(currency)
elif sys.argv[1] == 'buy':
    currency = sys.argv[2]
    c.tradeBuy(currency, int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
elif sys.argv[1] == 'sell':
    currency = sys.argv[2]
    c.tradeSell(currency, int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
