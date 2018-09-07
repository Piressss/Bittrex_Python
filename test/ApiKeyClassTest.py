#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src/')

from ApiKeyClass import *

c = ApiKeyClass()

print c.Decrypt('none')
