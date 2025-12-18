from menu import MENU_1_PRICE
from menu import MENU_2_PRICE
import menu
import msg
from msg import GREETINGS, APPEAL

multiprocessing = '***' * 11
print(multiprocessing)
print(GREETINGS)
print(multiprocessing)
name = input("Как вас завут?: ")
print(APPEAL.format(name=name))
print(multiprocessing)
print(menu.MENU_1)
position = int(input("Сколько порций вы хотите? "))
prise = MENU_1_PRICE
total = prise * position

print(msg.APPEAL_3, menu.MENU_2)
position_1 = int(input("Сколько порций вы хотите? "))
prise_1 = MENU_2_PRICE
total_1 = prise_1 * position_1
print(multiprocessing)
sum = total + total_1
discount = sum * 0.15

print(f'Сумма без скидки = {sum}')
print(f'Сумма скидки = {discount}')
print(f'К оплате = {sum - discount}')
print(multiprocessing)

# age = input("Введите свой возраст: ").strip() # Сразу очешаем от пробелов


#######################################NAME############################################
name.title()  # Делает слово с большой буквы
name = name.strip()  # Убирает пробелы с переди и сзади
name = name.strip('0123456789 ')  # в таком варианте очешает символы которые не долны быть
# name = name.lstrip('0123456789 ') # очишат символы с лева
# name = name.rsplit('0123456789 ') # очишат символы с права
# name = name.lower() # Переводит все симвалы в мальникий размер
# name = name.upper() # Делает все симвалы с большой буквы
# name = name.replace('.', '@') # замена симвалав на другой симвал
# name = name.capitalize() # 1 буква большая остальные маленькие
#######################################################################################

#######################################################################################
# is_digit = age.isdigit()
# age = int(age) # Преводит к целому числу
#######################################################################################


# print(multiprocessing)

# name = name.title().strip().lower() # Можно прописать в одной строчке


# print(name)
# print(age)

# print(multiprocessing)


# print(menu.MENU_1)
