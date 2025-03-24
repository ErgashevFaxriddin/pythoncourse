# def salomber():
#     print('Assalamu alaikum')
# salomber()

# ________________________________

# def salomber(ism):
#     print(f"Salom {ism.title()}")

# salomber('lazizbek')

# ___________________________________

# def toliq_ism(ism, familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('ali', 'husanov')

# _________________________________________________________

# def yosh_hisobla(ism, tyil):
#     print(f"Assalamu alaikum {ism.title()} siz {2025 - tyil} yoshdasiz")

# ism = input('ism: ')
# tyil = int(input('tugilgan yilingiz: '))
# yosh_hisobla(ism, tyil)

# ________________________________________________________________

# def karra(son):
#     for i in range(1, 11):
#         print(f"{son}x{i}={son*i}")

# son = int(input('son: '))
# karra(son)
# __________________________________________________________________

# def kopaytir(son, kopaytma):
#     print(f"{son} x {kopaytma} = {son*kopaytma}")

# son = int(input('son: '))
# kopaytma = int(input('kopaytma: '))
# kopaytir(son, kopaytma)
# ___________________________________________________________________

# def yosh_calculate(tyil, yil=2025):
#     print(f"{yil - tyil} yoshdasiz")
    
# yosh_calculate(1980, 2035)
# _____________________________________________________________________________________________

# # Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

# def kv_kub(son):
#     print(f"kvadrat: {son**2}\n"
#           f"kub: {son ** 3}")

# kv_kub(4)
# ________________________________________________________________________________________________

# # Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing
# def juftmi(son):
#     if son % 2 == 0:
#         print(f"{son} soni juft son")
#     else:
#         print(f"{son} soni toq son")
        
# juftmi(3)
# ____________________________________________________________________________________________________

# # Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
# # Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def taqqosla(son1, son2):
#     if son1 > son2:
#         javob = f"{son1} > {son2}"
#     elif son1 < son2:
#         javob = f"{son1} < {son2}"
#     else:
#         javob = f"{son1} = {son2}"
#     print(javob)

# taqqosla(55, 55)
#______________________________________________________________________________________

# # Foydalanuvchidan x va y sonlarini olib, (x**y) ni konsolga chiqaruvchi funksiya yozing.
# def kv_hisobla(son, kopaytma):
#     print(f"{son}**{kopaytma}={son**kopaytma}")
# kv_hisobla(2, 2)
# ____________________________________________________________________________

# def kv_hisobla2(son, kopaytma = 2):
#     print(f"{son}: {kopaytma} = {son**kopaytma}")

# kv_hisobla2(5)
# __________________________________________________________________________________________________________________________

# # # Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
# # # Natijalarni konsolga chiqaring.
# def bolinish_tekshir(son):
#     for i in range(2, 100):
#         if son % i == 0:
#             print(f"{son} / {i} = {son // i}")
            
# bolinish_tekshir(20)
# _______________________________________________________________________________________________

# # FUNKSIYAGA RO'YXAT UZATISH
# def yigindi(sonlar):
#     return sum(sonlar)

# raqamlar = [2, 3, 5]
# natija = yigindi(raqamlar)

# print(natija)
# ______________________________________________

# Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

# def katta_harf(royxat):
# 	for i in range(len(royxat)):
# 		royxat[i] = royxat[i].capitalize()

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(katta_harf)
# ____________________________________________________________________________________

# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

# def katta_harf2(royxat):
#     yangi_royxat = []
#     for i in royxat:
#         yangi_royxat.append(i.capitalize())
#     return yangi_royxat
        
# talablar = ['najmiddin', 'lazizbek', 'muhmammadyahyo']
# yangi_talablar = katta_harf2(talablar)
# print(", ".join(yangi_talablar))

# def sonlar(royxat):
#     yangi_sonlar = []
#     for son in royxat:
#         yangi_sonlar.append(son)
#     return yangi_sonlar

# raqamlar = [1, 4, 6, 5]
# print(sonlar(raqamlar))
# _____________________________________________________________________

# # Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va 
# # asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

# def bahola2(royxat):
#     baholar = {}
#     for ism in royxat:
#         baho = 'baho: '
#         baholar[ism] = baho
#     return baholar

# ishchilar = ['turdimuhammad', 'oybek', 'gulbahor']
# baholar = bahola2(ishchilar)
# print(", ".join(baholar).title()) 
# ______________________________________________________________________________

# Foydalanuvchidan bir nechta kitob nomlarini kiritishini so‘raydigan dastur yozing. 
# Dastur foydalanuvchi "stop" deb yozmaguncha davom etishi kerak. 
# Kiritilgan kitoblar ro‘yxatini qaytaruvchi funksiya yozing.


# kitoblar = []
# while True:
#     kitob_kirit = input('kitob: ')
#     if kitob_kirit.lower() == 'stop':
#         break
#     kitoblar.append(kitob_kirit)
# print("Kiritilgan kitoblar:", ", ".join(kitoblar))

# def kitob():
#     kitoblar = []
#     while True:
#         kitob_kirit = input('kitob: ')
#         if kitob_kirit.lower() == 'stop':
#             break
#         kitoblar.append(kitob_kirit)
#     return kitoblar

# kitoblarim = kitob()
# print(f"kitoblar: ", ", ".join(kitoblarim).title())
# _______________________________________________________________________

# # *ARGS VS *KWARGS
# # Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, 
# # va parametrlar yagona qiymatlar ko'rinishida uzatilsa, 
# # funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments). 

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(2, 4, 5))
# _____________________________________________________________________________________

# def summa(x, y, *sonlar):
#     return x + y + sum(sonlar)

# son = input("Kamida 2 ta butun son kiriting: ").split()

# try:
#     if len(son) < 2:
#         print("Iltimos, kamida 2 ta argument kiriting.")
#     else:
#         son = [int(i) for i in son]  # Butun songa o‘girish
#         print(summa(*son))  
# except ValueError:
#     print("Iltimos, faqat butun sonlar kiriting!")
# _________________________________________________________________________________

# Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, 
# va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).

def comp_info(model, protsessor, **infos):
    infos['model'] = model
    infos['protsessor'] = protsessor
    return infos

comp = comp_info('msi', '8', color='black', storage='256')
comp2 = comp_info('macbook', 'm3', color='white', storage='1 TB')

for key, value in comp.items():
    print(f"{key.title()}: {value.title()}")