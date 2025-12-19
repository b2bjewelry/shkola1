import pywebio

from pywebio.input import input as ps_input
from pywebio.output import put_text, put_html, put_warning, put_error, put_success


# Приведствме
put_html(f'<h1>Приведствую в нашем зоопарке</h1>')

age = int(ps_input(label='Введите ваш возраст'))

prise = 100

if age < 6:
    prise = 0
    put_success('✅ Вход бесплатный')
elif 6 <= age <= 12:
    discount = prise * 0.50
    total = prise - discount
    put_success(f'✅ Стоимость билета {prise} грн. '
                f'Скидка 50%. '
                f'Всего к оплате {total} грн')
elif 13 <= age <= 17:
    discount = prise * 0.25
    total = prise - discount
    put_success(f'✅ Стоимость билета {prise} грн. '
                f'Скидка 25%. '
                f'Всего к оплате {total} грн')
elif 18 <= age <= 60:
        discount = prise * 0
        total = prise - discount
        put_success(f'✅ Стоимость билета {prise} грн. '
                    f'Скидка 0%. '
                    f'Всего к оплате {total} грн')



