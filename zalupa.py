# class Zalupa: #класс залупа
#     def __init__(self, long, d):
#         self.long = long
#         self.d = d
#
# zalupa = Zalupa(12, 2)
# zalupa.color = "FUXY"
# print(f' Длина залупы пользователя составляет {zalupa.long} сантиметров.')
# print(f' Диаметр залупы пользователя составляет {zalupa.d} сантиметров.')
# print(f' Цвет залупы пользователя {zalupa.color}.')
#
# class Dog:
#     pass
#
# my_dog = Dog()  # Объект создан, но атрибутов нет
#
# my_dog.zalupa ="FUXY"
# print(f' Цвет залупы собаки {my_dog.zalupa}.')

# c = input("Введи число: ")
# d = input("Введи число: ")
# print(f'Сложение {int(c)+int(d)}')
# print(f'вычитание {int(c)-int(d)}')
# print(f'умножение {int(c)*int(d)}')
# print(f'деление {int(c)/int(d)}')
#
#
# a = 43
# b = "424"
# print(str(a)+b)

# def age():
#     b = int(input("Укажите Ваш возраст: "))
#     if b < 18:
#         print("Поздравляем! Вы ребенок")
#     elif b >= 18 and b <= 65:
#         print("Поздравляем! Вы Алан")
#     else:
#         print("Поздравляем! Вы пенсионер")


# # my_age = age()
# a = []
# for i in range(21):
#     print(i)
#     if i%2==0:
#         a.append(i)
# print(a)
#
# for i in input("Укажите число: "):
#     print(i)
#
# d = int(input("Введи число от 1 до 10: "))
# for i in range(1, 11):
#     print(f"{d} умножить на число {i} будет равно: {d*i}")
#
#

# movie = ["хуй", "залупа", "воротник"]
# print(movie)
# i = input("Новый фильм: ")
# movie.append(i)
# print(movie)

# def summ(a, b, c, d, e):
#     aa = [a, b, c, d, e]
#     for i in aa:
#         if b>i:
#             b=i
#     print(b)
#     print(max(aa))
#     print(min(aa))
#
# summ(3,4,6867,775,34)

# aaa = []
# bbb = []
# stroka = input("Напиши строку: ")
# print(len(stroka))
# print(stroka.upper())
# for i in stroka:
#     aaa.append(i)
# print(aaa)
#
# while aaa:
#     for i in aaa[-1]:
#         bbb.append(i)
#         aaa.pop(-1)
# print(aaa)
# print(bbb)
#
# ccc = ""
# for i in bbb:
#     ccc = ccc+i
# print(ccc)

# a = input("Введи строку: ")
# b = ''
# c = []
# for i in a:
#     if i != " ":
#         b = b+i
#     else:
#         c.append(b)
#         b=''
# c.append(b)
# print(c)
# print(c)

# S = π × r2

# pi = 3.14 #число пи
# s = int(input("Укажи диаметр первой пиццы: "))/2
# price = (int(input("Сколько стоит первая пицца: ")))
# s2 = int(input("Укажи диаметр второй пиццы: "))/2
# price2 = (int(input("Сколько стоит вторая пицца: ")))
#
# sp = s**2*pi #вычисляем площадь первой пиццы
# sp2 = s2**2*pi #вычисляем площадь второй пиццы
# price_sm = price/sp #вычисляем стоимость квадратного сантиметра пиццы
# price_sm2 = price2/sp2 #вычисляем стоимость квадратного сантиметра второй пиццы
# print(f"Площадь первой пиццы = {sp}")
# print(f"Стоимость квадратного сантиметра: {price_sm}")
# print(f"Площадь второй пиццы = {sp2}")
# print(f"Стоимость квадратного сантиметра: {price_sm2}")
#

nitik = ('Vladimir Iskusitel')
print('Кто сегодня о тебе вспоминает?')
print(f"Конечно же {nitik}")
Кто сегодня о тебе вспоминает?
Конечно же Vladimir Iskusitel