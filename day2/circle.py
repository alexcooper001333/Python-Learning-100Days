from math import pi as PIE

radius = float(input('请输入圆的半径: '))
perimeter = 2 * PIE * radius
area = PIE * radius ** 2
print("周长: {:.2f}".format(perimeter))
print("面积: {:.2f}".format(area))
