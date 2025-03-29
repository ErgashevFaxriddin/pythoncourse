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

# # Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, 
# # va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).

# def comp_info(model, protsessor, **infos):
#     while True:
#         comps = {}
#         infos['model'] = model
#         infos['protsessor'] = protsessor
#         return infos

# # comp = comp_info('msi', '8', color='black', storage='256')
# # comp2 = comp_info('macbook', 'm3', color='white', storage='1 TB')



# for key, value in comp.items():
#     print(f"{key.title()}: {value.title()}")
# ____________________________________________________________________

# sonlar = [1, 3, 44, 3, 7]
# print(*sonlar)

# muzikantlar = ['sirojiddin', 'mirolim', 'abduqahhor', 'nurali']
# print(*muzikantlar)
# ___________________________________________________________________
# *ARGS vs **KWARGS ___ *ARGS vs **KWARGS ___ *ARGS vs **KWARGS ___ *ARGS vs **KWARGS

# def zakaz_osh(osh, *qoshimchalar):
#     print(f"{osh}ga qoshimchalar: ")
#     for qoshimcha in qoshimchalar:
#         print(f" - {qoshimcha}")

# zakaz_osh('osh', 'manti', 'salat')

# def dokon(asosiy, *qoshimchalar, **malumotlar):
#     print(f"{asosiy.title()} mahsulotiga qoshimchalar: ")
#     for qoshimcha in qoshimchalar:
#         print(f" - {qoshimcha.title()}")
#     print('buyurtma ma\'lumotlari: ')
#     for key, value in malumotlar.items():
#         print(f"{key.title()}: {value}")

# dokon('sovun', 'gugurt', 'piyoz', yetkazib_berish = True, raqam = 123)
# _________________________________________________________________________________
# # Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def kopaytir(son, *sonlar):
#     javob = son
#     for s in sonlar:
#         if s == 'stop':
#             break
#         javob *= s
#     print(f"Natija: {javob}")

# kopaytir(12, 3, 4, 'stop')

# def qosh(son, *sonlar):
#     javob = son
#     for i in sonlar:
#         if i == 'stop':
#             break
#         javob += i
#     print(f"natija: {javob}")

# qosh(4, 1, 3, 10)

# def kwargs(**info):
#     for key, value in info.items():
#         print(f"{key.title()}: {value}")
        
# kwargs(name='faxriddin'.title(), age=21, hobby='playing piano'.title())
# ___________________________________________________________________
# Funksiya yozing, u talabaning ismi, yoshi va universitetini qabul qilib, 
# ekranga chiqarishi kerak.

# def talaba_info(ism, yosh, universitet, **talabalar):
#     talabalar['ism'] = ism.title()
#     talabalar['yosh'] = yosh
#     talabalar['universitet'] = universitet.upper()
#     return talabalar

# talaba1 = talaba_info('najmiddin', 20, 'tatuff', hobby='Football')
# for key, value in talaba1.items():
#     print(f"{key.title()}: {value}")
# ________________________________________________________________________________
# # Funksiya mashinaning turi, rangi va yili haqida ma’lumot chiqarishi kerak.

# def car_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key.title()}: {value.title()}")

# malumotlar = {}
# while True:
#     kalit = input('so\'z kiriting: ')
#     print('dasturni to\'xtatish uchun: (x)')
#     if kalit == 'x'.lower():
#         break
#     qiymat = input('qiymat kiriting: ')
#     malumotlar[kalit] = qiymat
    
# car_info(**malumotlar)
# ____________________________________________________________________
# # Funksiya mahsulot nomlari va narxlarini qabul qilib, ularni chiqarishi kerak
# def dokon(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key.title()}: {value}")
        
# mahsulotlar = {}
# while True:
#     print('dasturni to\'xtatish uchun: (x)')
#     kalit = input('mahsulot: ')
#     if kalit == 'x':
#         break
#     qiymat = input('qiymat: ')
#     mahsulotlar['kalit'] = qiymat
    
# dokon(**mahsulotlar)
#_______________________________________________________________
# # talaba malumotlari 
# def talaba_info(ism, yosh, universitet, **talabalar):
#     talabalar['ism'] = ism.title()
#     talabalar['yosh'] = yosh
#     talabalar['universitet'] = universitet.upper()
#     return talabalar

# print("Talaba ma'lumotlarini kiriting:")
# ism = input("Ism: ")
# yosh = int(input("Yosh: "))
# universitet = input("Universitet: ")

# talaba1 = talaba_info(ism, yosh, universitet)

# while True:
#     kalit = input("Qo'shimcha ma'lumot nomini kiriting (to'xtatish uchun 'x'): ")
#     if kalit.lower() == 'x':
#         break
#     qiymat = input(f"{kalit.title()} qiymatini kiriting: ")
#     talaba1[kalit] = qiymat

# for key, value in talaba1.items():
#     print(f"{key.title()}: {value}")
# __________________________________________________________________________________
# # mashina malumotlar
# def car_info2(model, **malumotlar):
#     malumotlar['model'] = model
#     return malumotlar

# print('mashina ma\'lumotlarini kiriting ')
# model = input('model: ')
# car1 = car_info2(model)

# while True:
#     kalit = input('qoshimcha (stop: "x")')
#     if kalit == 'x':
#         break
#     qiymat = input('qiymat: ')
#     car1['kalit'] = qiymat
    
# for key, value in car1.items():
#     print(f"{key.title()}: {value}")
# ________________________________________________________________________________
# # ishchilar
# def ishchilar(ism, id, kasb, **kwargs):
#     kwargs['ism'] = ism
#     kwargs['id'] = id
#     kwargs['kasb'] = kasb
#     return kwargs

# print(f"ishchilar ma\'lumotlarini kiriting")
# ism = input('ism: ')
# id = input('id: ')
# kasb = input('kasb: ')

# ishchi1 = ishchilar(ism, id, kasb)

# while True:
#     kalit = input('qoshimcha (stop: "x")')
#     if kalit == 'x':
#         break
#     qiymat = input('qiymat: ')
#     ishchi1[kalit] = qiymat

# print('Ishchi')
# for key, value in ishchi1.items():
#     print(f"{key.title()}: {value}")










# _____________________________________________________________________________________
# sportchilar

def sportchilar(ism, yosh, sport_turi, **kwargs):
    kwargs['ism'] = ism
    kwargs['yosh'] = yosh
    kwargs['sport turi'] = sport_turi
    return kwargs

ism = input('ism: ').title()
yosh = int(input('yosh: '))
sport_turi = input('sport turi: ').title()

sportchi1 = sportchilar(ism, yosh, sport_turi)

while True:
    kalit = input('qoshimcha (stop - x): ')
    if kalit == 'x':
        break
    
    qiymat = input(f"{kalit} uchun qiymat: ")
    
    if qiymat.isdigit():
        qiymat = int(qiymat)
    else:
        qiymat = qiymat.title()
    
    sportchi1[kalit] = qiymat
    
for key, value in sportchi1.items():
    print(f"{key.title()}: {value}")