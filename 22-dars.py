

#SANA:22\09\2022
#MAVZU:FUNKSIYAGA RO'YXAT UZATISH



def katta(matn):
    for x in range(len(matn)):
        matn[x]=matn[x].title()
olim=["ali","vali","sardor","hakim"]
katta(olim)
print(olim)


def katta_harf(matnlar):
    for t in range(len(matnlar)):
        matnlar[t]=matnlar[t].title()
    return matnlar

olim=["asad","qashqar","ali","hakim"]
hall=katta_harf(olim[:])
print(hall)  


def bahola(matn):
    baholar={}
    for ism in matn:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho 
    return baholar

user=["vohid","sardor","alibek","turobiy"]
olim=bahola(user)
print(olim)        

























