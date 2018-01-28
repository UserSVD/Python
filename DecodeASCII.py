#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:01:43 2018

ACSII Decoder
CTF link : https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-ASCII
Doc : https://docs.python.org/3/library/codecs.html

@author: adminSeb
"""
import os
import codecs

key=input('ENTREZ LE CODE ASCII :')
clear=codecs.decode(key, "hex").decode('utf-8')
print(clear)