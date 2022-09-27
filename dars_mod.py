def Use_malumot(ism,familya,tyil,email="",tel=None):
    use={"ism":ism,
         "familya":familya,
          "tyil":tyil,
          "yosh":2022-tyil,
          "email":email,
          "tel":tel}
    return use
def use_kirit():
    print("Foydalanuvchi haqidagi malumotlarni kiriting:")
    users=[]
    while True:
        ism=input("ismi:")
        familya=input("familyasi:")
        tyil=int(input("tug'ilgan yili:"))
        email=input("email:")
        tel=input("telefon nomer:")
        users.append(Use_malumot(ism, familya, tyil,email,tel))
        javob=input("Yana foydalanuvchi kiritasizmi: (yes/no)")
        if javob=="no":
            break
    return users
def use_print(Use_malumot):
  
    
    print(f"{Use_malumot['ism'].title()} {Use_malumot['familya'].title()}, "
          f"\n{Use_malumot['tyil']}-yilda  tug'ilgan "
          f"\nEmaili:{Use_malumot['email']} \nTelefoni:{Use_malumot['tel']}")
    
       