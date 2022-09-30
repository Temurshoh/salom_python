# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 06:35:24 2022

@author: User
"""
mevalar=["olma","anor","uzum","anjir",'gilos',"behi"]
ali=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(ali)