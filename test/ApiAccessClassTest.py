#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src/')

from ApiAccessClass import *

c = ApiAccessClass()

print c.getAPI('buylimit')

print c.getAPI('getopenorders', 'BTC-XRP')
