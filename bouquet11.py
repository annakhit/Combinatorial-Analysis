# найти количество всевозможных букетов из 15 цветов, каждый состоящий из четного числа белых и красных цветов и нечетного количества розовых.

bouquet = [0]*3
count = 0
print("Белые / Красные / Розовые")
for white in range(0, 16):
    for red in range(0, 16):
        for pink in range(0, 16):
            bouquet = [white, red, pink]
            if sum(bouquet) == 15 and white % 2 == 0 and pink % 2 != 0 and red % 2 == 0:
                count += 1
                print(bouquet)

print(f"Количество всевозможных букетов с условием чет/нечет: {count}")