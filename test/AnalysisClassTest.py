#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from AnalysisClass import *
from PublicClass import *
from DTOClass import *

c = AnalysisClass()

a = c.getCurrencyPivot('BTC-XVG',12)
print a._Pivot
print '\n'

a = c.getCurrencyAverage('BTC-XVG',12)
print a
print '\n'

a = c.getCurrencyWR('BTC-XVG',12)
print a
print '\n'

a = c.getCurrencyRSI('BTC-XVG')
print a
print '\n'

a = c.getCurrencyOBV('BTC-XVG',12)
print a
print '\n'

a = c.getCurrencyAnalysis('BTC-XVG',12)
print a._Pivot
print a._Last
print '\n'

a = c.getTradeGain('BTC-XVG',2.15e-6)
print a
print '\n'
