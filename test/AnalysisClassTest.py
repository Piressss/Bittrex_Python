#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from AnalysisClass import *
from PublicClass import *
from DTOClass import *

c = AnalysisClass()

a = c.getCurrencyPivot('BTC-XVG',12)
print a


