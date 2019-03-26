"""
author Pavlenko Konstantin, DP158Py

"""

triangles = []
name, a, b, c = input('Enter the name of the triangle, side a, b and c, separated by commas').split(',')
triangles.append(name)
triangles.append(float(a))
triangles.append(float(b))
triangles.append(float(c))
answer = input('Do you want to continue?').lower()

while answer == 'y' or answer == 'yes':
    name, a, b, c = input('Enter the name of the triangle, side a, b and c, separated by commas').split(',')
    triangles.append(name)
    triangles.append(float(a))
    triangles.append(float(b))
    triangles.append(float(c))
    answer = input('Do you want to continue?').lower()
place = dict()
x = 4

for i in range(len(triangles)):
    a = triangles[i * x + 1]
    b = triangles[i * x + 2]
    c = triangles[i * x + 3]
    p = (a + b + c) / 2
    if a == p or b == p or c == p or a == 0 or b == 0 or c == 0:
        print('It is impossible to build a triangle with such parameters')
    place[triangles[i * x]] = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    if i == (len(triangles) - 4) / 4:                     # limit input values and stop iterations
        break

for i in range(len(place)):
    m = 0
    n = ''
    for key, value in place.items():                      # looking for MAX value in the 'place' dictionary
        if value >= m:
            m = value
            n = key
    print('[', n, ']:', m, 'cm')
    place[n] = 0
