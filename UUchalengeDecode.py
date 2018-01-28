#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:16:33 2018

Decode "UU"
CTF Link : https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-UU
Ressources : http://repository.root-me.org/Cryptographie/EN%20-%20Encodings%20format.pdf
module : https://docs.python.org/3/library/uu.html

@author: adminSeb
"""
import uu

uu.decode("UUchalenge.txt", "UUfinal.txt")
