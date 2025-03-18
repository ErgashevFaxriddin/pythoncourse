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

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
son = 0
kitoblar = []
kitob = ''
ishora = True
while ishora:
    son +=1
    kitob = input(f"{son}-kitob: ")
    kitoblar.append(kitob)
    if kitob == 'x':
        break
for kitob in kitoblar:
    print(kitob)