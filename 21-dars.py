# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 06:12:15 2022

@author: User
"""

#SANA:05\06\2022
#MAVZU:FUNKSUYADAN QIYMAT QAYTARISH



#def  Use_malumot(ism,familya,tyil,email="",tel=None):
#    use={"ism":ism,
#         "familya":familya,
#          "tyil":tyil,
#          "yosh":2022-tyil,
#          "email":email,
#          "tel":tel}
#    return use
#print("Foydalanuvchi haqidagi malumotlarni kiriting:")
#users=[]
#while True:
#     ism=input("ismi:")
#     familya=input("familyasi:")
#     tyil=int(input("tug'ilgan yili:"))
#     email=input("email:")
#     tel=input("telefon nomer:")
#     users.append(Use_malumot(ism, familya, tyil,email,tel))
#     javob=input("Yana foydalanuvchi kiritasizmi: (yes/no)")
#     if javob=="no":
#         break
#print("Foydalanuvchilar:")
#for user in users:
#    if user['email']:
#        email=user['email']
#    else:
#        email="Nmalum"
#    if user['tel']:
#        tel=user['tel']
#    else:
#        tel='Mavjud emas'
#    print(f"{user['ism'].title()} {user['familya'].title()}, "
#          f" {tel}  {email}  "
#          f"{user['yosh']} yoshda")
          
          
          
#def katta_son(x,y,z):
   #max=x 
   #if y>=max:
       # max=y 
   #if z>=max:
        #max=z 
   #return max

#print(katta_son(10,27,66))    





#def aylana_info(radius,pi=3.14159):
#    aylana={"radiusi":radius,
#            "yuzi":(radius**2)*pi,
#            "diametri":2*radius,
#            "peremetri":2*pi*radius}
#    return aylana
#yum=print(aylana_info(5))
#print(aylana_info(9))    

    



#def katta(min,max,qadam=None):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        if qadam:
#            min+=qadam
#        else:
#            min+=1
#    return sonlar
#print(katta(10,20))
#print(katta(20,40,2))  


#def tup_son_top(min,max):
#    sonlar=[]
#    for n in range(min,max):
#        tup=True
#        if n==1:
#            tup=False
#           
#        else:
#            for x in range(2,n):
#                if n%x==0:
#                    tup=False
#        if tup:
#            sonlar.append(n)
#    return sonlar
#print(tup_son_top(2, 77))


def fabinonchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or   x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fabinonchi(7))
