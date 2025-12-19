from pywebio.input import input as ps_input
from pywebio.output import put_text, put_button, clear, put_error, put_success, put_html, put_warning
from pywebio.input import actions
from pywebio.output import clear

import question


# Инициализируем счетчик очков

score = 0
#Заголовок
put_html('<h1>Привет  Давай пройдем опрос. </h1>')

#Вопрос 1
question_1 = ps_input(label=question.GUESTION_1, required=True)
compare_1 = question.ANSWER_1 == question_1

# Проверяем условие если верно или нет
if compare_1:
    put_success('✅ Верно!')
    score += 1
else:
    put_error('❌ Неверно')

actions(label='', buttons=['Далее'])

#Вопрос 2
question_2 = ps_input(label=question.GUESTION_2, required=True)
compare_2 = question.ANSWER_2 == question_2

if compare_2:
    put_success('✅ Верно!')
    score += 1
else:
    put_error('❌ Неверно')

actions(label='', buttons=['Далее'])

#Вопрос 3
question_3 = ps_input(label=question.GUESTION_3, required=True)
compare_3 = question.ANSWER_3 == question_3

if compare_3:
    put_success('✅ Верно!')
    score += 1
else:
    put_error('❌ Неверно')

actions(label='', buttons=['Далее'])

#Вопрос 4
question_4 = ps_input(label=question.GUESTION_4, required=True)
compare_4 = question.ANSWER_4 == question_4

if compare_4:
    put_success('✅ Верно!')
    score += 11
else:
    put_error('❌ Неверно')

actions(label='', buttons=['Далее'])

#Вопрос 5
question_5 = ps_input(label=question.GUESTION_5, required=True)
compare_5 = question.ANSWER_5 == question_5

if compare_5:
    put_success('✅ Верно!')
    score += 1
else:
    put_error('❌ Неверно')

put_warning(f'Вы ответили на {score} вопроса.')