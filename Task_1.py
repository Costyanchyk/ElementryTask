a = input('input integer >= 0 ').lower()
b = input('Введите целое число больше 0 длина доски').lower()
a = int(a)
b = int(b)
if type(a) == int and type(b) == int:
	i = 0
	k = 0
	while i < b / 2:
		print('* ' * a)
		k += 1
		if k == b:
			break
		print(' *' * a)
		k += 1
		i += 1
elif a == 'help' or b == 'help':
	print('instruction')
else:
	a = input('Вы не ввели число. Введите целое число больше 0 - ширина доски  ').lower()
	b = input('Вы не ввели число. Введите целое число больше 0 - длина доски  ').lower()
	if a == 'help' or b == 'help':
		print('instruction')
