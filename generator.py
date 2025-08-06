import random, pygame

pygame.init()

width = 800
height = 600
black = (0,0,0)
white = (255,255,255)

disp = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dialy Quests Generator")

def make_btn(pos_x, pos_y, width, height, color, text, font_size):
    font = pygame.font.Font("freesansbold.ttf", font_size)
    btn_rect = pygame.Rect(pos_x, pos_y, width, height)
    pygame.draw.rect(disp, color, btn_rect)
    message = font.render(text, True, black)
    message_rect = message.get_rect(center = btn_rect.center)
    disp.blit(message, message_rect)
    return btn_rect

def display_text(text, x, y, size):
    font = pygame.font.Foont("freesansbold.ttf", size)
    text_surf = font.render(text, True, black)
    disp.blit(text_surf, (x,y))

def get_input():
    typed = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return typed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return typed
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode




def ui():
    run = True
    start = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_text("Get daily quest", 300, 100, 50)
        #get inut
        #validate input
        #flag to start
        #open file
        #shuffle
        #display quest
        



ans = input("Let's generate our quests for the day? ").capitalize()
if ans == "Yes":
    with open("quests.txt", "r", encoding="utf-8") as q:
        quests = q.readlines()
    ques = []

    for quest in quests:
        ques.append(quest)

    print("Here is your quest for today: ", end="")
    print(random.choice(ques))

else:
    print()
    print("Goodbye and good luck to you.")
    SystemExit


    

