"""
author Pavlenko Konstantin, DP158Py

"""


def name(y):
	answer = []
	first_row = ['', 'один', 'два', 'три', 'четыри', 'пять', 'шесть', 'семь', 'восемь', 'девять']
	second_row = ['', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
	              'семнадцать', 'восемнадцать', 'девятнадцать']
	tens_name = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
	             'девяносто']
	third_row = ['', 'сто', 'двести', 'триста', 'четыриста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
	fourth_row = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыри тысячи', 'пять тысяч', 'шесть тысяч',
	              'семь тысяч', 'восемь тысяч', 'девять тысяч']
	t = y // 1000  # выделяю число тысяч
	hundreds = (y % 1000) // 100  # выделяю сотни
	ten = (y % 100) // 10  # выделяю число десятков
	units = y % 10  # выделяю число единиц
	if ten == 1 and units > 0:
		answer.append(fourth_row[t])
		answer.append(third_row[hundreds])
		answer.append(second_row[units])
	else:
		answer.append(fourth_row[t])
		answer.append(third_row[hundreds])
		answer.append(tens_name[ten])
		answer.append(first_row[units])
	for i in answer:
		print(i, end=' ')


num = int(input('Введите число от 9999 до 1'))

if num > 0:
	name(num)
else:
	print('Некорректный ввод, число должно быть больше 0')
	num = int(input('Введите число от 9999 до 1'))
	name(num)
