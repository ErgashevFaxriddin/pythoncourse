# ism = input('ism: ')
# savol = f"{ism} yoshingiz: "
# yosh = int(input('yosh: '))
# print(yosh)

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = int(input(savol))
# height = float(input("Bo'yingiz necha metr? "))

# ism = input('ism: ')
# savol = 'yosh kiriting: '
# yosh = int(input(savol))
# print(f"{yosh} yoshli {ism.title()} qalaysiz? ;)")

# son = 1
# while son <= 5:
#     print(son)
#     son += 1

# qiymat = ''
# while qiymat != 'x':
#     qiymat = input('son kiriting. toxtatish - x: ')
#     if qiymat != 'x':
#         print(float(qiymat) **2)

# ishora = True
# while ishora:
#     qiymat = input('son kiriting: ')
#     if qiymat == 'x':
#         ishora = False
#     else:
#         print(f"{qiymat} x 2 = {int(qiymat) **2}")

# # break
# ishora = True
# while ishora:
#     qiymat = input('type a digit: ')
#     if qiymat == 'x':
#         break
#     else:
#         print(f"{qiymat} x {qiymat} = {int(qiymat) ** 2}")

# # continue
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} * 2 = {son **2}")

# son = 0
# while son <= 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     print(son)

# # Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# # Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# son = 0
# kitoblar = []
# kitob = ''
# ishora = True
# while ishora:
#     son +=1
#     kitob = input(f"{son}-kitob: ")
#     kitoblar.append(kitob)
#     if kitob == 'x':
#         break
# for kitob in kitoblar:
#     print(kitob)

# # Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
# # 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
# # 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
# # Shunday while tsikl yozingki, 
# # dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# # Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# while True:
#     yosh = input("Yoshingizni kiriting (exit yoki quit - to'xtatish): ")
#     if yosh.lower() in ['exit', 'quit']:
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         narx = 0
#     elif yosh >= 7 and yosh < 18:
#         narx = 2000
#     elif yosh >= 18 and yosh < 65:
#         narx = 10000
#     else:
#         narx = 0
#     print(f"Sizga chipta narxi: {narx} so'm")

# ishora = True
# while ishora:
#     yosh = input('yosh: ')
#     if yosh.lower() == 'quit':
#         break
#     if not yosh.isdigit():
#         print('❌RAQAM KIRITING❌')
#         continue
#     yosh = int(yosh)
#     if yosh < 7:
#         narx = 0
#     elif yosh >= 7 and yosh < 18:
#         narx = 2000
#     elif yosh >= 18 and yosh < 65:
#         narx = 10000
#     else:
#         narx = 0
#     print(f"Sizga chipta narxi: {narx} so'm")

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. 
# Xatolarni to'g'rilay olasizmi?
# BERILGAN: 
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# # 1 dan 10 gacha bo‘lgan sonlarni ekranga chiqaruvchi dastur tuzing.
# son = 1
# while son <= 10:
#     print(son)
#     son += 1

# # 2 dan 10 gacha bo‘lgan juft sonlarni ekranga chiqaruvchi dastur tuzing.
# son = 0
# while son <= 10:
#     if son % 2 == 0:
#         print(son)
#     son += 1

# # 10 dan 1 gacha bo‘lgan sonlarni kamayish tartibida ekranga chiqaruvchi dastur tuzing
# son = 10
# while son > 0:
#     print(son)
#     son -= 1

# # Foydalanuvchi "stop" deb yozmaguncha so‘rov beruvchi dastur tuzing.
# mevalar = []
# ishora = True
# while ishora:
#     print('meva kiriting')
#     meva = input('toxtatish x: ').lower()
#     mevalar.append(meva)
#     if meva == 'x':
#         print(", ".join(mevalar))
#         break

# mevalar = []
# ishora = True
# while ishora:
#     print('meva kiriting')
#     meva = input('toxtatish x: ').lower()
#     mevalar.append(meva)
#     if meva == 'x':
#         break
# print(", ".join(mevalar))

# ismlar = []
# son = 1
# while True:
#     ism = input(f'{son}-kiriting: ')
#     ismlar.append(ism)
#     javob = input('yanami? ')
#     if javob == 'ha':
#         son+=1
#         continue
#     else:
#         break
# print(", ".join(ismlar))

# print('dostlaringiz yoshini aniqlaymiz')
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('ism: ').lower()
#     yosh = input('yosh: ')
#     dostlar[ism] = int(yosh)
#     javob = input('yanami? ha/yoq: ')
#     if javob == 'yoq':
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# print('bozorlik')
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input('mahsulot: ')
#     narx = input('narx: ')
#     if not narx.isdigit():
#         print('matn kiriting: ')
#         continue
#     mahsulotlar[mahsulot] = int(narx)
#     sikl = input('davom ettirasizmi? ha/yoq: ')
#     if sikl == 'yoq':
#         ishora = False
# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot.title()}: {narx} som")

# talabalar = ['ali', 'vali', 'samandar', 'ahad', 'ibrohim']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning ning bahosi: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(", ".join(baholangan_talabalar).title())

# # mahsulotlar narxini aniqlashda yordam bering
# mahsulotlar = ['pomidor', 'kartoshka', 'quruq-choy']
# narxlangan_mahsulotlar = {}
# while mahsulotlar:
#     mahsulot = mahsulotlar.pop()
#     narx = input(f"{mahsulot}ga narx bering: ")
#     if not narx.isdigit():
#         print('❌RAQAM KIRITING❌')
#         break
#     if int(narx) < 1000:
#         print(f"{mahsulot}ning qiymati juda oz\nQayta tekshiring: ")
#         continue
#     narxlangan_mahsulotlar[mahsulot] = narx
# for mahsulot, narx in narxlangan_mahsulotlar.items():
#     print(f"{mahsulot.title()}: {narx} som")

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# buyurtmalar = []
# while True:
#     buyurtma = input('mahsulot nomi: ')
#     if not buyurtma:
#         break
#     buyurtmalar.append(buyurtma)
#     print(f"{buyurtma} buyurtmalarga qoshildi✅")
#     soni = input('yana mahsulot qoshasizmi? "ha/yoq"')
#     if soni == 'ha':
#         continue
#     else:
#         break
# print("sizning savatchangiz: ", ", ".join(buyurtmalar).title())

# # tepadagi kod dictionary yordamida
# buyurtmalar = {}
# while True:
#     buyurtma = input('mahsulot nomi: ')
#     narx = input('narx: ')
#     buyurtmalar[buyurtma] = int(narx)
#     print(f"{buyurtma} buyurtmalarga qoshildi✅")
#     soni = input('yana mahsulot qoshasizmi? "ha/yoq"')
#     if soni == 'ha':
#         continue
#     else:
#         break
# print('sizning savatchangiz')
# for mahsulot, narx in buyurtmalar.items():
#     print(f"{mahsulot.title()}: {narx} som")
# yigindi_narx = sum((buyurtmalar.values()))
# print(f"umumiy xarajat summasi: {yigindi_narx}")


# Musbat sonlarni qabul qilish, manfiy son kiritsak siklni to‘xtatish
# while True:
#     son = input('son: ')
#     son = int(son)
#     if son < 0:
#         break

# # Juft sonlarni chiqarish, toq sonlarga kelganda siklni davom ettirish (continue).
# while True:
#     for son in range(1, 11):
#         if son % 2 != 0:
#             continue
#         print(son)
#     break

# Berilgan sonni teskari tartibda ekranga chiqarish (masalan, 123 → 321).
# while True:
#     son = 123
#     bir = son % 10
#     on = son // 10 % 10
#     yuz = son // 100
#     print(yuz, on, bir)
#     break

# teskari_son = []
# while son > 0:
#     son = input('son kiriting: ')
#     birlik = son % 10
#     teskari_son.append(teskari_son)
#     onlik = son // 10 % 10
#     teskari_son.append(onlik)
#     yuzlik = son // 100
#     teskari_son.append(yuzlik)
#     print(", ".join(teskari_son))
#     break

# son = int(input("Son kiriting: "))  
# teskari_son = 0  
# while son > 0:
#     qoldiq = son % 10  # Oxirgi raqamni olish
#     teskari_son = teskari_son * 10 + qoldiq  # Teskari tartibda yig‘ish
#     son = son // 10  # Oxirgi raqamni olib tashlash
# print("Teskari son:", teskari_son)



# # Mevalar ro‘yxatini foydalanuvchidan kiritib olish va oxirida ekranga chiqarish
# mevalar = []

# while True:
#     sanoq = int(input('nechta meva kiritmoqchisiz? '))

#     for i in range(sanoq):
#         meva = input(f"{i+1}-meva: ").lower()
#         mevalar.append(meva)

#     print(f"savatchaningiz: {", ".join(mevalar)}")
#     break

# __________________________________________________________________________________________________

# # Mahsulotlar lug‘atini to‘ldirish (mahsulot nomi va narxi), foydalanuvchi ‘stop’ kiritganda to‘xtatish.
# mahsulotlar = {}

# while True:
#     mahsulot = input('mahsulot kiriting: ')
#     narx = input('narx: ')

#     if not narx.isdigit():
#         print('narxni raqamlar bilan kiriting! : ')
#         continue

#     mahsulotlar[mahsulot] = int(narx)

#     davom = input('davom ettirasizmi? (ha/yoq): ')
#     if davom == 'yoq':
#         break

# print('bozorlik royxati')
# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot.title()}: {narx} som")

# ____________________________________________________________________________________

# oshoxona uchun menu
# buyurtmalar = {}

# menu = {
#     "osh": 30000,
#     "manti": 12000,
#     "somsa": 8000,
#     "shashlik": 15000,
#     "norin": 25000,
#     "mastava": 18000,
#     "lag'mon": 22000,
#     "shurva": 20000,
#     "tandir go'sht": 35000,
#     "chuchvara": 16000
# }
# while True:
#     son = 0
#     print("Menu")
#     for taom, narx in menu.items():
#         son += 1
#         print(f"{son}| {taom.title()}: {narx} som")

#     # savol = input('\nbuyurtma kiritasizmi? (ha/yoq): ').strip().lower()

#     # if savol.isdigit():
#     #     print("❌ matn kiriting ❌")
#     #     continue

#     # if savol != 'ha':
#     #     break

#     buyurtma = input('👇 taom kiriting: ').strip().lower()
#     if buyurtma.isdigit():
#         print('❌Matn kiriting❌ : ')
#         continue

#     if buyurtma in menu:
#         buyurtmalar[buyurtma] = menu[buyurtma]
#         print(" ✅buyurtma qabul qilindi")
#     else:
#         print(f" ❌{buyurtma.title()} mavjud emas❌ ")
#         continue

#     davom = input('davom ettirasizmi? (ha/yoq): ')
#     if davom == 'yoq':
#         print('dastur toxtatildi')
#         break

# if buyurtmalar:
#     print("👇 buyurtmalaringiz 👇")
#     for buyurtma, narx in buyurtmalar.items():
#         print(f"{buyurtma.title()}: {narx} som ")
#         print(f"umumiy summa: {sum(buyurtmalar.values())} som")
# else:
#     print("buyurtma berilmadi")

# # ______________________________________________________________________________

menu = {
    "osh": 30000,
    "manti": 12000,
    "somsa": 8000,
    "shashlik": 15000,
    "norin": 25000,
    "mastava": 18000,
    "lag'mon": 22000,
    "shurva": 20000,
    "tandir go'sht": 35000,
    "chuchvara": 16000
}

buyurtmalar = {}

gramm_taomlar = {"osh", "norin"}
dona_taomlar = {"manti", "shashlik", "somsa", "tandir go'sht"}
kosa_taomlar = {"mastava", "lag'mon", "shurva", "chuchvara"}

olchov_birliklari = {
    "g": 1,
    "gramm": 1,
    "kg": 1000,
    "kilogramm": 1000,
    "s": 100000,
    "sentner": 100000,
    "t": 1000000,
    "tonna": 1000000
}

while True:
    print("\n📜 MENU 📜")
    for i, (taom, narx) in enumerate(menu.items(), start=1):
        print(f"{i}. {taom.title()}: {narx} som")
    
    buyurtma = input('\n👇 Taom kiriting: ').strip().lower()
    
    if buyurtma not in menu:
        print(f" ❌ {buyurtma.title()} mavjud emas ❌ ")
        continue
    
    while True:
        if buyurtma in gramm_taomlar:
            miqdor_olchov = input(f"{buyurtma.title()} miqdorini kiriting (masalan: 500 g, 1.5 kg, 1 tonna): ").strip().lower()
            
            try:
                miqdor, birlik = miqdor_olchov.split()
                miqdor = float(miqdor)
                birlik = birlik.lower()
                if birlik not in olchov_birliklari:
                    raise ValueError
                miqdor *= olchov_birliklari[birlik]
            except (ValueError, IndexError):
                print("❌ Iltimos, to'g'ri miqdor va birlik kiriting (masalan: 500 g, 1.5 kg, 1 tonna) ❌")
                continue
        
        elif buyurtma in dona_taomlar:
            birlik = "dona"
            miqdor = input(f"{buyurtma.title()} necoha {birlik} buyurtma qilasiz? ").strip()
        else:
            birlik = "kosa"
            miqdor = input(f"{buyurtma.title()} necha {birlik} buyurtma qilasiz? ").strip()
        
        try:
            miqdor = float(miqdor)
        except ValueError:
            print("❌ Iltimos, to'g'ri son kiriting ❌")
            continue
        break
    
    buyurtmalar[buyurtma] = buyurtmalar.get(buyurtma, 0) + miqdor
    print("✅ Buyurtma qabul qilindi")
    
    davom = input('Davom ettirasizmi? (ha/yoq): ').strip().lower()
    if davom == 'yoq':
        print("Dastur to'xtatildi")
        break

if buyurtmalar:
    umumiy_summa = 0
    print("\n👇 Buyurtmalaringiz 👇")
    for taom, miqdor in buyurtmalar.items():
        birlik = "gramm" if taom in gramm_taomlar else ("dona" if taom in dona_taomlar else "kosa")
        narx = (menu[taom] / 1000) * miqdor if taom in gramm_taomlar else menu[taom] * miqdor
        umumiy_summa += narx
        print(f"{taom.title()} ({miqdor} {birlik}): {narx:.2f} som")
    print(f"\n💰 Umumiy summa: {umumiy_summa:.2f} som")
else:
    print("📌 Buyurtma berilmadi")

# __________________________________________________________________________________________________________________

# # while yordamida 5 marta salom sozini yozish
# soz = 'salom'
# son = 0
# while son < 20:
#     print(f"{son}: salom")
#     son += 3

# _____________________________________________________________________________________________________________________
# # parol
# # 1️⃣ while True – Cheksiz tsikl yoki Foydalanuvchi Kiritishini Kutish
# # 📌 Qachon ishlatish kerak?
# # ✅ Agar cheksiz tsikl kerak bo‘lsa
# # ✅ Foydalanuvchidan kiritish olish va shart bajarilmaguncha tsikl davom etishi kerak bo‘lsa

# while True:
#     parol = input('parol: ')
#     if parol == ".;'.":
#         print('xush galidiniz')
#         break
#     else:
#         print('Noto\'g\'ri parol, qayta urinib ko\'ring.')
# _________________________________________________________________________________________________________________
# # # Siz while yordamida bitta list ichidagi ma’lumotlarni olib, boshqa listga ko‘chirishingiz mumkin.
# # laptops = ['asus', 'msi', 'mac', 'hp']
# # new_laptops = []
# # while laptops:
# #     computer = laptops.pop(0)
# #     new_laptops.append(computer)
# # print(f"new list: {", ".join(new_laptops)}")
# # print(f"old list: {", ".join(laptops)}")

# bitiruvchi_talabalar = ['ali', 'vali', 'asad', 'abubakir']
# yangi_talabalar = []
# while bitiruvchi_talabalar:
#     talaba = bitiruvchi_talabalar.pop(0)
#     yangi_talabalar.append(talaba)
# print(f"yangi talabalar: {", ".join(yangi_talabalar).title().replace(", ", " ")}")
# print(f"eski talabalar: {bitiruvchi_talabalar}")