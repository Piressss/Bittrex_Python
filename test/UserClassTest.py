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
currency = sys.argv[1]

c = UserClass(key,secret)

c.getAnalysis(currency)
