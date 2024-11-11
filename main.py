import pygame

pygame.init()

display_size = (950,580)
sc = pygame.display.set_mode(display_size)
pygame.display.set_caption("Tamagochi")

#загружаем фоны
background0 = pygame.image.load("images/hello.png")
background0 = pygame.transform.scale(background0, display_size)
background1 = pygame.image.load("images/background1.png")
background1 = pygame.transform.scale(background1, display_size)
background2 = pygame.image.load("images/menu.png")
background2 = pygame.transform.scale(background2, display_size)
background3 = pygame.image.load("images/bedroom.png")
background3 = pygame.transform.scale(background3, display_size)
background4 = pygame.image.load("images/kitchen.png")
background4 = pygame.transform.scale(background4, display_size)
table = pygame.image.load("images/table.png")
table = pygame.transform.scale(table, (table.get_width()*0.27, table.get_height()*0.27))

#инициализируем нужные шрифты
F = pygame.font.SysFont("comicsansms", 50)
f = pygame.font.SysFont("comicsansms", 25)
fF = pygame.font.SysFont("comicsansms",38)

#создаем классы
class Text():
    def __init__(self, words, color, ff, bg):
        self.color = color
        self.text = ff.render(words, True, color, bg)
class Button():
    def __init__(self, file, k):
        self.image = pygame.image.load(file)
        self.size = (self.image.get_width()*k, self.image.get_height()*k)
        self.position = (0,0)
        self.image = pygame.transform.scale(self.image,self.size)
class Tamagotchi():
    def __init__(self, file, k):
        self.image = pygame.image.load(file)
        self.size = (self.image.get_width()*k, self.image.get_height()*k)
        self.image = pygame.transform.scale(self.image, self.size)
        self.happy = 100

#здесь все питомцы
pet = [0 for i in range(4)]
pet[0] = Tamagotchi("images/picachu.png", 1)
pet[1] = Tamagotchi("images/cat1.png", 0.8)
pet[2] = Tamagotchi("images/панда.png", 0.35)
pet[3] = Tamagotchi("images/dog.png", 0.30)

current_pet = 0

#заготовки реплик
choose = Text("Выбери своего питомца", "purple", F, None)
score = Text("Уровень счастья:", "purple", F, None)
eating = Text("Кушать", "white", f, None)
sleep = Text("Спать", "white",f, None)
back = Text("назад", "white", f, None)
mess = Text("Я выспался!", "white", F, "purple")
over = Text("Питомец погиб :((", "purple", F, None)

#здесь все кнопки
button_play = Button("images/play.png", 0.3)
button_play.position = (display_size[0]//2 - button_play.size[0]//2, display_size[1]//3 - button_play.size[1]//2)
button_left = Button("images/left.png", 0.3)
button_right = Button("images/left.png",0.3)
button_yes = Button("images/yes.png", 0.3)
button_right.image = pygame.transform.flip(button_right.image, True, False)
button_func1 = Button("images/кнопка.png", 0.33)
button_func1.position = (758, 60)
button_func2 = Button("images/кнопка.png", 0.33)
button_func2.position = (758, 60 + 50)
button_left.position = (150 - button_left.size[0], 200 + pet[current_pet].size[1]//2)
button_right.position = (150 + pet[current_pet].size[0], 200 + pet[current_pet].size[1]//2)
button_yes.position = (20, 430)
button_back = Button("images/кнопка.png", 0.33)
button_back.position = (15, 510)
button_lamp = Button("images/lamp.png", 0.33)
button_lamp.position = (800, 60)

#список с едой класс кнопки
food = [["milk", Button("images/milk.png", 0.1)],
        ["cookie", Button("images/cokie.png", 0.45)],
        ["carrot", Button("images/carrot.png", 0.2)],
        ["candy", Button("images/candy.png", 0.1)],
        ["pizza", Button("images/pizza.png", 0.2)],
        ["meet", Button("images/meet.png", 0.2)]]
food[0][1].position = (700,50)
food[1][1].position = (800,50)
food[2][1].position = (700,190)
food[3][1].position = (820,190)
food[4][1].position = (680, 350)
food[5][1].position = (820,350)

#список с реакциями на еду
phrase = [Text("Молоко я люблю!", "white", fF, "purple"),
          Text("Омномном вкуснятина))", "white", fF, "purple"),
          Text("может что-то другое дашь?", "white", fF, "purple"),
          Text("Спасибо! ты знаешь, что я люблю", "white", fF, "purple"),
          Text("мм вкусненько", "white", fF, "purple"),
          Text("ну и блевотина...", "white", fF, "purple")]

current_background = 0 #текущий фон
lamp = "on" #лампа в спальне
morning = False #индикатор недавнего пробуждения
eating_yet = False #индикатор недавнего итинга
init = False #питомец выбран
running = True
st = pygame.time.get_ticks()

#запускаем игру
while running:
    if init:                #равномерное падение счётчика
        if pygame.time.get_ticks()-st >=1500:
            pet[current_pet].happy -= 1
            st = pygame.time.get_ticks()
    if pet[current_pet].happy == 0:
        sc.blit(background1, (0,0))
        sc.blit(over.text, (200,200))
        break
    #обработка ввода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif current_background == 0 and event.type == pygame.MOUSEBUTTONDOWN and\
        button_play.position[0] <= event.pos[0] <= button_play.position[0]+button_play.size[0] and\
        button_play.position[1] <= event.pos[1] <= button_play.position[1]+button_play.size[1]:
            current_background = 1
        elif current_background == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if button_left.position[0] <= event.pos[0] <= button_left.position[0] + button_left.size[0] and\
            button_left.position[1] <= event.pos[1] <= button_left.position[1] + button_left.size[1]:
                current_pet = (current_pet - 1) % 4
            elif button_right.position[0] <= event.pos[0] <= button_right.position[0] + button_right.size[0] and\
            button_right.position[1] <= event.pos[1] <= button_right.position[1] + button_right.size[1]:
                current_pet = (current_pet + 1) % 4
            elif button_yes.position[0] <= event.pos[0] <= button_yes.position[0] + button_yes.size[0] and\
            button_yes.position[1] <= event.pos[1] <= button_yes.position[1] + button_yes.size[1]:
                current_background = 2
                init = True
        elif current_background == 2 and event.type == pygame.MOUSEBUTTONDOWN:
            if button_func1.position[0] <= event.pos[0] <= button_func1.position[0] + button_func1.size[0] and\
            button_func1.position[1] <= event.pos[1] <= button_func1.position[1] + button_func1.size[1]:
                current_background = 4
            elif button_func2.position[0] <= event.pos[0] <= button_func2.position[0] + button_func2.size[0] and\
            button_func2.position[1] <= event.pos[1] <= button_func2.position[1] + button_func2.size[1]:
                current_background = 3
        elif current_background == 3 and event.type == pygame.MOUSEBUTTONDOWN:
            if button_back.position[0] <= event.pos[0] <= button_back.position[0] + button_back.size[0] and\
            button_back.position[1] <= event.pos[1] <= button_back.position[1] + button_back.size[1]:
                current_background = 2
                lamp = "on" #лампа включается при переходе в другую локацию
                morning = False
            if button_lamp.position[0] <= event.pos[0] <= button_lamp.position[0] + button_lamp.size[0] and\
            button_lamp.position[1] <= event.pos[1] <= button_lamp.position[1] + button_lamp.size[1]:
                if lamp == "on":
                    lamp = "off"
                    start_ticks=pygame.time.get_ticks() #отсчитываем время с начала сна
                else:
                    lamp = "on"
                    if (pygame.time.get_ticks()-start_ticks) >= 5000:
                        pet[current_pet].happy += 5
                        morning == True
                        start_morning = pygame.time.get_ticks() #Отсчитываем время с начала пробуждения
        elif current_background == 4 and event.type == pygame.MOUSEBUTTONDOWN:
            if button_back.position[0] <= event.pos[0] <= button_back.position[0] + button_back.size[0] and\
            button_back.position[1] <= event.pos[1] <= button_back.position[1] + button_back.size[1]:
                current_background = 2 
                eating_yet = False
            for n in range(6):
                if food[n][1].position[0] <= event.pos[0] <= food[n][1].position[0] + food[n][1].size[0] and\
                food[n][1].position[1] <= event.pos[1] <= food[n][1].position[1] + food[n][1].size[1]: 
                    pet[current_pet].happy += 3
                    food_number = n
                    eating_yet = True
                    start_eating = pygame.time.get_ticks() #отсчитываем время с момента когда поел чтобы выводить нужную реплику
    if current_background == 3 and lamp == "off": #если лампа выключена но прошло 5 сек то просыпается
        if (pygame.time.get_ticks()-start_ticks) >= 5000:
            pet[current_pet].happy += 5
            lamp = "on"
            morning = True
            start_morning = pygame.time.get_ticks()

    #обнова экрана
    if current_background == 1:
        background1.blit(choose.text, (30,50))
        background1.blit(button_left.image, button_left.position)
        background1.blit(button_right.image, button_right.position)
        background1.blit(button_yes.image, button_yes.position)
        sc.blit(background1, (0,0))
        sc.blit(pet[current_pet].image, (150,200))
    if current_background == 0:
        background0.blit(button_play.image, button_play.position)
        sc.blit(background0, (0,0))
    if current_background == 2:
        pygame.draw.ellipse(background2,(205,110,180),
                         (100, 140, 140, 140))
        pygame.draw.ellipse(background2,(204,0,204),
                         (100, 140, 140, 140), 8)
        pygame.draw.rect(background2, (204, 0, 204),
                 (display_size[0] - 210, 20, 180, 500), 8)
        pygame.draw.rect(background2, (205, 110, 180), 
                 (display_size[0] - 210+15, 20+15, 150, 470))
        background2.blit(pet[current_pet].image, (250, 200))
        background2.blit(score.text, (30,50))
        background2.blit(button_func1.image, button_func1.position)
        background2.blit(button_func2.image, button_func2.position)
        background2.blit(eating.text, (button_func1.position[0]+20, 65))
        background2.blit(sleep.text,(button_func1.position[0]+20, button_func1.position[1] + 55))
        if pet[current_pet].happy > 100:
            pet[current_pet].happy = 100
        if pet[current_pet].happy < 0:
            pet[current_pet].happy = 0
        score_n = Text(str(pet[current_pet].happy), "white", F, None)
        background2.blit(score_n.text, (130, 170))
        sc.blit(background2, (0,0))
    if current_background == 3:
        background3.blit(pet[current_pet].image, (250, 200))
        background3.blit(button_back.image, button_back.position)
        background3.blit(back.text, (button_back.position[0]+20, button_back.position[1] ))
        background3.blit(button_lamp.image, button_lamp.position)
        sc.blit(background3, (0,0)) 
        if lamp == "off": #накладываем прозрачный черный
            night = pygame.Surface(display_size)
            night.fill((0,0,0))
            night.set_alpha(180)
            sc.blit(night, (0,0))
        elif morning and (pygame.time.get_ticks() - start_morning)<= 4000:
            sc.blit(mess.text, (200,100))
        
    if current_background == 4:
        background4.blit(pet[current_pet].image, (250, 200))
        background4.blit(table, (660, 20))
        for i in range(len(food)):
            background4.blit(food[i][1].image, food[i][1].position)
        background4.blit(button_back.image, button_back.position)
        background4.blit(back.text, (button_back.position[0]+20, button_back.position[1]))
        sc.blit(background4, (0, 0))
        if eating_yet == True and (pygame.time.get_ticks() - start_eating) > 2000:
            eating_yet == False
        if eating_yet == True and (pygame.time.get_ticks() - start_eating) <= 2000:
            sc.blit(phrase[food_number].text,(100,100))
    pygame.display.update()
    
pygame.quit()