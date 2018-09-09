#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from PublicClass import *
from DTOClass import *

c = PublicClass()

c.getSummaryCurrency('BTC-XRP')
