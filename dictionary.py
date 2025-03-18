# car0 = {'name':'toyota', 
# 'model':'carolla', 
# 'year':2025, 
# 'location':'usa'}
# car0['price'] = 1000000
# # del car0['location']
# print('nam/e:', car0['name'].title(),
# '\nmodel:', car0['model'].title(),
# '\nyear:', car0['year'],
# '\nprice: ', car0['price'], 
# '\nlocation:', car0["location"].upper())

# telefonlar = {
#     'ali':'iphone 12 pro max',
#     'vali':'samsung s24 ultra',
#     'Maftuna':'vivoy36'
# }
# phone = telefonlar.get("ali", 'Bunday ism mavjud emas')
# print(phone)

# taomlar = {
#     'ali':'osh',
#     'vali':'manti',
#     'kamol':'shashlik',
#     'temur':'norin',
#     'Islom':'somsa',
#     'maqsud':'dimlama',
#     'laziz':'sho\'rva',
#     'izzat':'mastava',
#     'farrux':'kulchaosh',
#     'sardor':'lavash'
# }
# taom = taomlar.get('maqsud', 'bunday ism mavjud emas')
# print(taom)

pydic = {
    'print':"print() bu funksiya jarayon amalga oshirish uchun ishlatiladi",
    'input':'input() - foydalanuvchidan ma\'lumot olish',
    'int':'int() - sonni butun qismida qaytaradi',
    'float':'float() - sonni o\'nlik qismida qaytaradi',
    'str':'str() - matn qaytaradi',
    'list':'list() - ro\'yxat qaytaradi',
    'tuple':'o\'zgarmas ro\'yxat qaytaradi',
    'dict':'dict() - lug\'at qaytaradi',
    'if':'if - agar shart to\'gri bo\'lsa shartni bajaradi',
    'else':'else - agar shart noto\'gri bo\'lsa shartni bajaradi',
    'elif':'elif - agar bir nehta shartlar to\'g\'ri bo\'lsa shartni bajaradi',
    'for':'for - sikl operatori',
    'while':'while - to\'g\'ri bo\'lsa shartni bajaradi',
    'break':'break - siklni to\'xtatish',
    'continue':'continue - sikl davom ettirish',
    'def':'def - funksiya yaratish',
    'return':'return - funksiya qaytarish',
    'import':'import - modulni chaqrirish',
    'from':'from - moduldan funksiya chaqirish',
    'as':'as - modulga alias berish',
    'class':'class - klass yaratish',
    'try':'try - kodni tekshirish',
    'except':'except - xatolarni tekshirish',
    'finally':'finally - kodni bajarish',
    'raise':'raise - xatoni chiqarish',
    'and':'adn - va',
    'or':'or - yoki',
    'not':'not - emas',
    'is':'is - teng',
    'in':'in - ichida',
    'global':'global - global o\'zgaruvchi',
    'nonlocal':'nonlocal - lokal o\zgaruvchi',
    'pass':"'",
    'lambda':'lambda - funksiya yaratish',
    'del':'del - o\chirish',
    'assert':'assert - tekshirish',
    'yield':'yield - qiymat qaytarish',
    'with':'with - faylni ochish',
    'open':'open - faylni ochish',
    'close':'close - faylni yopish',
    'read':'read - faylni o\'qish',
    'write':'write - faylni yozish',
    'append':'append - faylni qo\'shish',
    'mode':'mode - rejim',
    'r':'r - qo\'shish rejimi',
    'w':'w - yozish rejimi',
    'a':'qo\'shish rejimi',
    'r+':"r+ - o\'qish rejimi",
    'w+':'w+ - yozish rejimi'

}


# kalit = input('kalit soz kiriting: ').lower()
# # print(pydic.get(kalit, 'Bunday so\'z mavjud emas'))
# tarjima = pydic.get(kalit)
# if tarjima == None:
#     print('Bunday so\'z mavjud emas')
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


# for key, value in pydic.items():
#     print(f"kalit: {key.title()}\nQiymat: {value}")

# for key, value in pydic.items():
#     print(f"{key.title()}ning ma'nosi: {value.title()}")

# print(pydic.keys())

# for keys in pydic:
#     print(keys.title())

# print("python izohli lug'ati:\n")
# for i in pydic.keys():
#     print(i.title())

# print("python izohli lug'ati:\n")
# for i in sorted(pydic):
#     print(i.title())

# print("python izohli lug'ati:\n")
# # print(pydic.values())
# for i in pydic.values():
#     print(i)

# for key, value in sorted(pydic.items()):
#     print(key, value)

# davlatlar = {
#     'usa':'washington',
#     'uzbekistan':'tashkent',
#     'korea':'seul'
# }

# capital = input('davlat kiriing: ').lower()
# response = davlatlar.get(capital, f"{capital.title()} topilmadi")
# print(response.title())

# # for key, value in davlatlar.items():
# #     print(key,)
# #     print(value)

# user = input('davlat kiriting: ').lower()
# capital = davlatlar.get(user, 'Bunday davlat mavjud emas')
# print(capital)

# menu = {
#     'osh':25000,
#     'manti':3000,
#     'somsa':4000
# }
# taom = input('taom tanalng:').lower()
# narx = menu.get(taom, 'Bunday taom mevjud emas')
# print(narx)

# shaharlar = {
#     'Toshkent':3058.4,
#     'Samarqand ':4227.3,
#     'Farg\'ona ':4079.5,
#     'Andijon ':3409
# }
# for key, value in shaharlar:
#     shahar = f"{value} inson bor"
#     print(shahar)

# salon = {
#     'audi':21000,
#     'bmw':25000,
#     'tesla':18000
# }
# car = input('mashina tanlang:').lower()
# narx = salon.get(car, f"{car} yo'q")
# print(narx)

# mevalar = {
#     'olma':5000,
#     'mandarin':25000
# }
# meva = input('meva tanlang: ').lower()
# narx = mevalar.get(meva, 'yo\'q')
# print(narx)

# print('shaharlar lugatini yaratamiz')
# shaharlar = {}
# shahar = input('shahar: ')
# aholisoni = int(input('aholi sonini: '))
# shaharlar[shahar] = aholisoni
# print(f"yangi lugat: ", shaharlar )

# davlatlar = {
#     'uzbekistan' : 'tashkent',
#     'rossiya' : 'moskva'
# }
# davlat = input('davlat: ')
# poytaxt = davlatlar.get(davlat, 'yo\'q')
# print(poytaxt)

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
# agar taom menuda bo'lsa narhini ko'rsating, 
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.


# menu = {
#     'manti': 7000,  
#     'palov': 20000,
#     'shashlik': 10000
# }
# savat = {}

# print('3 ta taom kiriting')
# for i in range(3):
#     taom = input(f"{i+1}-taom: ").lower()  
#     if taom in menu:
#         savat[taom] = menu[taom]
#     else:
#         savat[taom] = None

# for taom, narx in savat.items():
#     if narx:
#         print(f"{taom} - {narx} som")
#     else:
#         print("bizda bunday taom yo'q")


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, 
# va har bir shaxs haqidagi ma'lumotni konsolga chiqaring

# shaxslar = {
#     melod1st : {
#         'ism' : 'faxriddin',
#         'kasb' : 'python web develooper',
#         'instagram' : 'melod1st'
#     },
#     najmiddin : {
#         'ism' : 'najmiddin',
#         'kasb' : 'javaScipt web develooper',
#         'instagram' : 'najmiddin_life'
#     },
#     melod1st : {
#         'ism' : 'behruz',
#         'kasb' : 'trader',
#         'instagram' : 'bekhruz'
#     }

# }

# melod1st = {
#     'ism': 'Faxriddin',
#     'kasb': 'Python Web Developer',
#     'yosh': 20,
#     'asar': ['Piano', 'Python']
# }
# najmiddin = {
#     'ism': 'Najmiddin',
#     'kasb': 'JavaScript Web Developer',
#     'yosh': 19,
#     'asar': ['Mumtoz', 'Piyola']
# }
# bexruz = {
#     'ism': 'Bekhruz',
#     'kasb': 'Trader',
#     'yosh': 18,
#     'asar': ['Inson Qasidasi', 'Vaqt']
# }

# shaxslar = [melod1st, najmiddin, bexruz]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()}ning kasbi {shaxs['kasb']} va u {shaxs['yosh']} yoshda.")

#     print(f"{shaxs['ism']}ning asarlari:")
#     for i in shaxs['asar']:
#         print(f" - {i}")
#     print()

# Davlatlar degan lug'at yarating, 
# lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring

# davlatlar = {
#     'uzb': {
#     'poytaxt': 'toshkent',
#     'aholi': 37.5,
#     'mintaqa': "o'rta osiyo",
#     'prezident': 'sh. m. mirziyoyev',
#     'valyuta': 'som'
#     },
#     'rus': {
#         'poytaxt': 'moskva',
#         'aholi': 146,
#         'mintaqa': "sharqiy yevropa",
#         'prezident': 'vladimir putin',
#         'valyuta': 'rubl'
#     },
#     'italia': {
#         'poytaxt': 'rome',
#         'aholi': 58.9,
#         'mintaqa': "shimoliy yevropa",
#         'prezident': 'sergio matarella',
#         'valyuta': 'the euro'
#     },
#     'germaniya': {
#         'poytaxt': 'berlin',
#         'aholi': 84.75,
#         'mintaqa': "central europe",
#         'prezident': 'Frank-Walter Steinmeier',
#         'valyuta': 'the euro'
#     }
# }

# for davlat, info in davlatlar.items():
#     print(f"{davlat}: {info['poytaxt']}")
#     print(f"aholi soni: {info['aholi']}")
#     print(f"hudud: {info['mintaqa']}")
#     print(f"prezident: {davlat['prezident']}")
#     print(f"pul birligi: {davlat['valyuta']}")

davlatlar = {
    'uzbekistan': {
        'poytaxt': 'Toshkent',
        'aholi': 37.5,
        'mintaqa': "O'rta Osiyo",
        'prezident': 'Sh. M. Mirziyoyev',
        'valyuta': 'So‘m'
    },
    'russia': {
        'poytaxt': 'Moskva',
        'aholi': 146,
        'mintaqa': "Sharqiy Yevropa",
        'prezident': 'Vladimir Putin',
        'valyuta': 'Rubl'
    },
    'italia': {
        'poytaxt': 'Rim',
        'aholi': 58.9,
        'mintaqa': "Janubiy Yevropa",
        'prezident': 'Sergio Mattarella',
        'valyuta': 'Yevro'
    },
    'germaniya': {
        'poytaxt': 'Berlin',
        'aholi': 84.75,
        'mintaqa': "Markaziy Yevropa",
        'prezident': 'Frank-Walter Steinmeier',
        'valyuta': 'Yevro'
    }
}

# for davlat, info in davlatlar.items():
#     print(f"{davlat.upper()}: {info['poytaxt']}")
#     print(f"Aholi soni: {info['aholi']} mln")
#     print(f"Hudud: {info['mintaqa']}")
#     print(f"Prezident: {info['prezident']}")
#     print(f"Pul birligi: {info['valyuta']}\n")


# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
# Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

# davlat = input(f"Davlat nomi: ").lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"Poytaxti: {info['poytaxt'].title()}")
#     print(f"Aholisi: {info['aholi']} mln")
#     print(f"Mintaqa: {info['mintaqa']}")
#     print(f"Pul birligi: {info['valyuta']}")
# else:
#     print(f"{davlat} haqida ma'lumot yo'q")



# Siz universitet talabalarining ma’lumotlarini saqlaydigan dastur yozishingiz kerak. 
# Har bir talabaning quyidagi ma’lumotlari bo‘ladi
talabalar = {
    'Najmiddin': {
        'ism': 'Najmiddin',
        'yosh': 20,
        'major': 'Digital Economy',
        'fanlar': ['Raqamli iqtisodiyot asoslari', 'Kompyuter Tarmoqlari'],
        'ball': [21, 23, 54, 67]
    },
    'Muhammadyahyo': {
        'ism': 'Muhammadyahyo',
        'yosh': 19,
        'major': 'Digital Economy',
        'fanlar': ['Raqamli iqtisodiyot asoslari', 'Kompyuter Tarmoqlari', 'Ma\'lumotlar Bazasi'],
        'ball': [21, 23, 54, 123]
    },
    'Lazizbek': {
        'ism': 'Lazizbek',
        'yosh': 21,
        'major': 'Digital Economy',
        'fanlar': ['Raqamli iqtisodiyot asoslari', 'Kompyuter Tarmoqlari', 'Ma\'lumotlar Bazasi', 'pul, kredit va banklar'],
        'ball': [21, 23, 90, 54]
    }
}

addtalaba = input(f"Talaba kiriting: ")

talaba = input('talaba ismini kiriting: ').title()
if talaba in talabalar:
    info = talabalar[talaba]
    print(f"Ismi: {info['ism'].title()}")
    print(f"yosh: {info['yosh']}")
    print(f"mutaxasisilgi: {info['major']}")
    for fan in info['fanlar']:
        print(f"yiqilgan fanlari: {fan}")
    # print(f"yiqilgan fanlari: ", ", ".join(info['fanlar']))
else:
    print(f"Bizda {talaba.title()} ismli talaba yo'q")

# # mevalar = ['olma', 'behi', 'uzum']
# # print(f"mevalar: ", ", ".join(mevalar))

# for talaba, info in talabalar.items():
#     total_ball = sum(info['ball'])
#     average = total_ball // len(info['ball'])
#     print(f"{info['ism']}ning umumiy balli: {total_ball}, o'rtacha balli: {average}")

