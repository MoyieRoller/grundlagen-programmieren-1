import math

while True:
    r = input('Please insert radius: ')
    if r.isdigit():
        r = int(r)
        area = math.pi * math.pow(r, 2)
        print('The area of the circle is:', str(area))
        break
    else:
        print('Please insert a correct radius.')
