import decimal

MENU_1 = 'Сырники с изюмом и мёдом'
MENU_1_PRICE_1 = 180
MENU_1_PRICE = decimal.Decimal(str(MENU_1_PRICE_1)).quantize(decimal.Decimal('0.01'))


MENU_2 = 'Овсяная каша с шафраном и льном'
MENU_2_PRICE_2 = 150
MENU_2_PRICE = decimal.Decimal(str(MENU_2_PRICE_2)).quantize(decimal.Decimal('0.01'))



MENU_3 = 'Творог со сметаной'
MENU_3_PRICE = decimal.Decimal(100)



MENU_4 = 'Блины с красной икрой'
MENU_4_PRICE = decimal.Decimal(184)