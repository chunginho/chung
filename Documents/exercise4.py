import math

def distinct(x1, x2, y1, y2):
	l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return l


x1 = input('input x1 : ')
x2 = input('input x2 : ')
y1 = input('input y1 : ')
y2 = input('input y2 : ')
l = distinct(x1,x2,y1,y2)
print l