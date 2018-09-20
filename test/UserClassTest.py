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

c.getAnalysis('BTC-XRP')
