"""
author Pavlenko Konstantin, DP158Py

"""

n = 0
while n != 4:
	side_a = float(input('Enter side a'))
	if side_a == 0:
		print("enter only positive numbers greater than 0")
		break
	else:
		n += 1
	side_b = float(input('Enter side a'))
	if side_b == 0:
		print("enter only positive numbers greater than 0")
		break
	else:
		n += 1
	side_c = float(input('Enter side a'))
	if side_c == 0:
		print("enter only positive numbers greater than 0")
		break
	else:
		n += 1
	side_d = float(input('Enter side a'))
	if side_d == 0:
		print("enter only positive numbers greater than 0")
		break
	else:
		n += 1


if (side_a >= side_c and side_b >= side_d) or (side_a >= d and side_b >= c) or (
		side_c >= side_a and side_d >= side_b) or (side_c >= side_b and side_d >= side_a):
	print('One envelope fits in another.')
	answer = input('Do you want to continue?').lower()
else:
	print("One envelope won't fit in another.")
	answer = input('Do you want to continue?').lower()


while answer == 'y' or answer == 'yes':
