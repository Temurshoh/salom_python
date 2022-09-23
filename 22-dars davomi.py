def kopaytma(*sonlar):
    kopaytma=1
    for i in sonlar:
        kopaytma*=i
    return kopaytma
print(kopaytma(2,6,7))
print(kopaytma(56,99))





def talaba(ism,familya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familya']=familya
    return malumotlar
talaba1=talaba("ali","hakimov",kurs=4,fakultet="filolog")
talaba2=talaba("asad","olimov",yosh=24,yili=1998,uqishi="institut")
print(talaba1)
print(talaba2)


