#решение уравнения 28x+30y+31z=365
total = 0
for x in range(1, 13):
    for y in range(1, 12):
        for z in range(1, 11):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)

#опровержение теоремы Эйлера
for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                    