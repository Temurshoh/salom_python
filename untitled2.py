# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 06:01:12 2022

@author: User
"""

import random
for i in range(3):
    print(random.randint(10, 20))
    
    
a=[3,4,5]
b=[6,7,8]
ali=list(map(lambda x,y:x+y,a,b))
print(ali)



sonlar=[12,34,2,56,8]
ildiz=list(map(lambda x:x*x,sonlar))
print(ildiz)

son=[23,56,78,45,46,34,47,28,19]
s=list(map(lambda x:x%2==0,son))
print(s)


mevalar=["olma","anor","uzum","rayxon","anjir","banan","kivi","kakos"]
bob=list(filter(lambda meva: meva.startswith("b"),mevalar))
print(bob)
ali=list(filter(lambda meva:len(meva)<=5,mevalar))
print(ali)
sel=list(filter(lambda meva:(meva.startswith("a")and meva.endswith("r")),mevalar))  
print(sel)

#kvadrat=lambda x,y:x**y
#print(kvadrat(3,2))
def daraja(n):
    return lambda x: x**n
kvadrat=daraja(4)



















