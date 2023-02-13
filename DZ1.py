# Рябкин Игорь | Т11О-202Б-21 | 25 Вариант
#             Условия:
#               a) 2/21 = 0.095, sqrt(22) = 4.69
#               б) 24.5641, d = 0.09% 
#               в) 4.478
print("")
print("             Рябкин Игорь | Т11О-202Б-21 | 25 Вариант")
print ("       Условия \na) 2/21 = 0.095, sqrt(22) = 4.69 \nб) 24.5641, d = 0.09% \nв) 4.478" )
print("")
print ("       Ответы")
import math
#                                  Задание А

#               a) 2/21 = 0.095, sqrt(22) = 4.69
a1_init = (0.095)
a2_init = (4.69)
# Вычисляем значения с большим числом знаков после запятой
a1 = round(2/21, 6)
a2 = round(math.sqrt(22), 6)
# Вычисляем абсолютные погрешности
err_a1 = round((a1 - a1_init), 6)
err_a2 = round((a2 - a2_init), 6)

delta_a1 = 100 * round((err_a1 / a1), 3)
delta_a2 = 100 * round((err_a2 / a2), 3)


if delta_a1 < delta_a2:
    ans = ("2/21 точнее чем sqrt(22)")
else:
    ans = ("sqrt(22) точнее чем 2/21")
print("Ответ на задание А:", ans)


#                                  Задание Б

#               б) 24.5641, d = 0.09%
b = 24.5641
delta_b = round(((24.5641*0.09)/100), 2)  # == 0.022
b = round(b, 1)
print ("Ответ на задание Б:", b)

#                                  Задание В

#               в) 4.478
v = 4.478
abs_delta_v = 0.0005
otn_delta_v = (abs_delta_v / v)
print ("Ответ на задание В:", round((otn_delta_v * 100), 2), "%")  # 2 по правилу окрегления



#       Ответы
#Ответ на задание А: sqrt(22) точнее чем 2/21
#Ответ на задание Б: 24.6
#Ответ на задание В: 0.01 %