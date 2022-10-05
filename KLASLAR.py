# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 06:06:40 2022

@author: User
"""

#SANA:05\10\2022
#MAVZU: KLASSLAR



class User:
    def __init__(self,ism,familya,email,tel,tyil):
        self.ism=ism
        self.familya=familya
        self.email=email
        self.tel=tel
        self.tyil=tyil
    def use_info(self):
        return f"Ismim {self.ism} Familyam {self.familya} Emailim {self.email} Telefon {self.tel} {self.tyil} "
    def get_name(self):
        return self.ism
    def get_age(self,yil):
        return yil-self.tyil
                
                
user1=User("Temur","Turdimurodov","tim98@gmail",915595546,1998) 
               
                
                
                