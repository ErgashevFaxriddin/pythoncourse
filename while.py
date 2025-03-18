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

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    