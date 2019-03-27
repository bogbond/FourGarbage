import pygame

pygame.init()  #инициализируем пайгейм
win = pygame.display.set_mode((1280, 800)) #создвем переменную в которую записываем разрешение(размер) окна

pygame.display.set_caption("Garbage truck") #присваиваем имя окна

#расположение обьекта
x = 50
y = 50
#размеры обьекта
width = 40
height = 60
#скорость перемешния
speed = 5
#прыжки
isJump = False
jumpCount = 10


run = True
while run: #цыкл
    pygame.time.delay(50)  #цыкл с интервалом каждые 50мс

    for event in pygame.event.get():  #перебераем массив event (все события в приложение)
        if event.type == pygame.QUIT:  #если собитие равно закрыванию окна, то
            run = False                 # переменной run присваиваем False

    keys = pygame.key.get_pressed() # создаем список в который записываються кнопки с клавиатуры
    if keys[pygame.K_LEFT] and x > 5:   #если нажата клавиша влево то, +второе условие не дает выйти обьекту за окно слево, отступ на 5 пикселей
        x-=speed              # от кординаты расположения обьекта отнимаем "скорость"
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:      # перемешаем в право +второе условие не дает выйти обьекту за границу справа (размер окна - ширина обьекта - отступ)
        x+=speed
    if not(isJump): # что бы не было возможности передвигать обьект верх\вниз в прижке
        if keys[pygame.K_UP] and y > 5:         #вверх и граница с отспупом в 5пх сверху
            y-=speed
        if keys[pygame.K_DOWN] and y < 500 - height - 5:       #вниз и отступ
            y+=speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:        #прыгвем вверх или вниз
            if jumpCount < 0:       #что бы падал вниз
                y += (jumpCount ** 2) / 2
            else:                        #вверх
                y -= (jumpCount ** 2) / 2
            jumpCount -=1
        else:                      #закончили прижек
            isJump = False
            jumpCount = 10



    win.fill((0, 0, 0)) #заполняем окно черным цветом, что бы не рисовать, а передвигать обьект
#рисуем квадрат (поле где он будет написован. цвет, расположение, размеры)
    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()  #обновляет окно, вывожит изоображение



pygame.quit()   #используем, что бы наверника закрыть окно
