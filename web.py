from ast import compare

import pywebio
from pywebio.input import input as ps_input
from pywebio.output import put_html, put_text, put_success, put_error
from pywebio.input import PASSWORD as PW_PASSWORD #модуль который при введение пас ставить точкки (скрывает ввод)

import msg
import menu


LOGIN = '1'
PASSWORD = '1'

multiprocessing = '***' * 11
put_html(multiprocessing)
put_html(msg.GREETINGS)
login = ps_input(label = 'Введите ваш логин', required=True)
password = ps_input(label = 'Введите ваш пароль', required=True, type=PW_PASSWORD)

#Проверякм правильность введение логина и пароля в БД
compare_login = LOGIN == login # Сравниваем логин с БД
compare_password = PASSWORD == password # Сравниваем пароль с БД

if compare_login and compare_password:
    put_success('✅ Верно!')
else:
    put_error('❌ Неверно')



