from turtle import *
from math import *


def planet(sun_d, text, x, y, color, r, distance):
    # перемещаем черепашку
    penup()
    goto(x, y)
    pendown()

    # пишем текст
    write(text, align = 'center', font = ('Arial', int(sun_d / 15), 'normal'))

    # рисуем планету
    penup()
    goto(x, y + distance)
    pendown()

    fillcolor(color)
    begin_fill()
    circle(r)
    end_fill()
    
    if text == 'Сатурн':
        penup()
        goto(x, y + distance + r * (8 / 25))
        pendown()
        # a, b - длина и ширина элипса, они должны быть в 2 раза меньше планируемых
        a, b = r + r * (3 / 15), r * (9 / 13)
        dx = xcor()
        dy = ycor()
        for deg in range(361):
            rad = radians(deg)
            x1 = a * sin(rad) + dx
            y1 = -b * cos(rad) + b + dy
            goto(x1, y1)


def solar_system(sun_d):
    while True:
        answer = input('Сразу вывести результат? Введите да / нет ').strip().lower()
        if answer == 'да':
            Screen().tracer(0, 0)
            penup()
            hideturtle()
            goto(- sun_d * 2, -sun_d * 0.5)
            showturtle()
            pendown()
            
            distance_planets = sun_d * (0.9 / 4.7)

             # диаметры планет
            d_mercury = sun_d * (0.9 / 4.2)
            d_venus = sun_d * (1.3 / 4.2)
            d_earth = sun_d * (0.9 / 4.2)
            d_mars = sun_d * (0.7 / 4.2)
            d_jupiter = sun_d * (2.5 / 4.2)
            d_saturn = sun_d * (2.5 / 4.2)
            d_uranus = sun_d * (1.1 / 4.2)
            d_neptune = sun_d * (0.9 / 4.2)
            d_pluto = sun_d * (0.4 / 4.2)

            # y для Меркурия, Венеры, Земли, Марса
            line_mvem = ((sun_d + sun_d * (4 / 46)) - (d_venus + d_venus * (0.3 / 1.1))) / 1.5

            # y для Юпитера и Сатурна
            line_js = ((sun_d + sun_d * (4 / 46)) - (d_jupiter + d_jupiter * (1 / 6))) / 1.5

            # y для Урана, Нептуна, Плутона
            line_np = ((sun_d + sun_d * (4 / 46)) - (d_uranus + d_uranus * (0.5 / 1.6))) / 1.5

            # данные о планетах и Солнце в виде словаря
            planets = {'Солнце': [pos()[0] + sun_d / 2, -sun_d * 0.5, 'yellow', sun_d / 2, sun_d * (2 / 21)],
                    'Меркурий': [pos()[0] + sun_d + distance_planets + d_mercury / 2, line_mvem-sun_d * 0.5, 'orange', d_mercury / 2, d_mercury * (5 / 9)],
                    'Венера': [pos()[0] + sun_d + 2 * distance_planets + d_mercury + d_venus / 2, line_mvem-sun_d * 0.5, 'orange', d_venus / 2,
                                d_venus * (1 / 3)],
                    'Земля': [pos()[0] + sun_d + 3 * distance_planets + d_mercury + d_venus + d_earth / 2, line_mvem-sun_d * 0.5, 'cyan', d_earth / 2,
                                d_earth * (5 / 8)],
                    'Марс': [pos()[0] + sun_d + 4 * distance_planets + d_mercury + d_venus + d_earth + d_mars / 2, line_mvem-sun_d * 0.5, 'red',
                                d_mars / 2, d_mars * (6 / 7)],
                    'Юпитер': [pos()[0] + sun_d + 5 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter / 2,
                                line_js-sun_d * 0.5, 'orange', d_jupiter / 2, d_jupiter * (1 / 5)],
                    'Сатурн': [
                        pos()[0] + sun_d + 6 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn / 2,
                        line_js-sun_d * 0.5, 'orange', d_saturn / 2, d_saturn * (1 / 5)],
                    'Уран': [
                        pos()[0] + sun_d + 7 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus / 2,
                        line_np-sun_d * 0.5, 'lightblue', d_uranus / 2, d_uranus * (5 / 16)],
                    'Нептун': [
                        pos()[0] + sun_d + 8 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus + d_neptune / 2,
                        line_np-sun_d * 0.5, 'blue', d_neptune / 2, d_neptune * (6 / 15)],
                    'Плутон': [
                        pos()[0] + sun_d + 9 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus + d_neptune + d_pluto / 2,
                        line_np-sun_d * 0.5, 'orange', d_pluto / 2, d_pluto * (11 / 7)]
               }
            for i in planets:
                planet(sun_d, i, *planets[i])
            hideturtle()
            done()
            Screen().update()
            break
        elif answer == 'нет':
            penup()
            hideturtle()
            goto(- sun_d * 2, -sun_d * 0.5)
            showturtle()
            pendown()
            
            distance_planets = sun_d * (0.9 / 4.7)

             # диаметры планет
            d_mercury = sun_d * (0.9 / 4.2)
            d_venus = sun_d * (1.3 / 4.2)
            d_earth = sun_d * (0.9 / 4.2)
            d_mars = sun_d * (0.7 / 4.2)
            d_jupiter = sun_d * (2.5 / 4.2)
            d_saturn = sun_d * (2.5 / 4.2)
            d_uranus = sun_d * (1.1 / 4.2)
            d_neptune = sun_d * (0.9 / 4.2)
            d_pluto = sun_d * (0.4 / 4.2)

            # y для Меркурия, Венеры, Земли, Марса
            line_mvem = ((sun_d + sun_d * (4 / 46)) - (d_venus + d_venus * (0.3 / 1.1))) / 1.5

            # y для Юпитера и Сатурна
            line_js = ((sun_d + sun_d * (4 / 46)) - (d_jupiter + d_jupiter * (1 / 6))) / 1.5

            # y для Урана, Нептуна, Плутона
            line_np = ((sun_d + sun_d * (4 / 46)) - (d_uranus + d_uranus * (0.5 / 1.6))) / 1.5

            # данные о планетах и Солнце в виде словаря
            planets = {'Солнце': [pos()[0] + sun_d / 2, -sun_d * 0.5, 'yellow', sun_d / 2, sun_d * (2 / 21)],
                    'Меркурий': [pos()[0] + sun_d + distance_planets + d_mercury / 2, line_mvem-sun_d * 0.5, 'orange', d_mercury / 2, d_mercury * (5 / 9)],
                    'Венера': [pos()[0] + sun_d + 2 * distance_planets + d_mercury + d_venus / 2, line_mvem-sun_d * 0.5, 'orange', d_venus / 2,
                                d_venus * (1 / 3)],
                    'Земля': [pos()[0] + sun_d + 3 * distance_planets + d_mercury + d_venus + d_earth / 2, line_mvem-sun_d * 0.5, 'cyan', d_earth / 2,
                                d_earth * (5 / 8)],
                    'Марс': [pos()[0] + sun_d + 4 * distance_planets + d_mercury + d_venus + d_earth + d_mars / 2, line_mvem-sun_d * 0.5, 'red',
                                d_mars / 2, d_mars * (6 / 7)],
                    'Юпитер': [pos()[0] + sun_d + 5 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter / 2,
                                line_js-sun_d * 0.5, 'orange', d_jupiter / 2, d_jupiter * (1 / 5)],
                    'Сатурн': [
                        pos()[0] + sun_d + 6 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn / 2,
                        line_js-sun_d * 0.5, 'orange', d_saturn / 2, d_saturn * (1 / 5)],
                    'Уран': [
                        pos()[0] + sun_d + 7 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus / 2,
                        line_np-sun_d * 0.5, 'lightblue', d_uranus / 2, d_uranus * (5 / 16)],
                    'Нептун': [
                        pos()[0] + sun_d + 8 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus + d_neptune / 2,
                        line_np-sun_d * 0.5, 'blue', d_neptune / 2, d_neptune * (6 / 15)],
                    'Плутон': [
                        pos()[0] + sun_d + 9 * distance_planets + d_mercury + d_venus + d_earth + d_mars + d_jupiter + d_saturn + d_uranus + d_neptune + d_pluto / 2,
                        line_np-sun_d * 0.5, 'orange', d_pluto / 2, d_pluto * (11 / 7)]
               }
            for i in planets:
                planet(sun_d, i, *planets[i])
            hideturtle()
            done()
            Screen().update()
            break
        else:
            print('Я вас не понял')
            continue


solar_system(int(input()))
