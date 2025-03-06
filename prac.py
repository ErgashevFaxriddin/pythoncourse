# doslar = ['Najmiddin', 'Behruz', 'Lazizbek']
# print(doslar[0], 'qalesan?')
# print(doslar[1], 'nima gap?')
# print(doslar[2], 'qaydasan?')



# sonlar = [100, -12, 5.6, 3]
# bir = sonlar[1] + sonlar[0]

# ysonlar = sonlar[:]
# ikki = ysonlar[0] = 101
# 
# print(sonlar)

tshaxslar = ['Zahiriddin Mhammad Bobur', 'Alisher Navoiy', 'Muhammad al-Xorazmiy']
zshaxslar = ['Shavkat Mirziyoyev', 'Abror Muxtor Ali', 'Botir Qodirov']

friends = ['Shavkat Mirziyoyev', 'Abror Muxtor Ali', 'Botir Qodirov']

mehmonlar = []
mehmonlar.append(friends.pop())

# print('Men tarixiy shaxslardan ', tshaxslar.pop(0), 'va Zamonaviy shaxslardan ', zshaxslar.pop(0), 'ni juda hurmat qilaman' )
# print('bugun dasturxonimizga men sevgan kishilardan ', tshaxslar.pop(1), tshaxslar.pop(1), 'va', zshaxslar.pop(1), 'mehmonga kelishadi')

while friends:
    mehmonlar.append(friends.pop())

print('mehmonlar: ', mehmonlar)