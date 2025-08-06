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

def display_text(text, x, y, size, color):
    font = pygame.font.Font("freesansbold.ttf", size)
    text_surf = font.render(text, True, color)
    disp.blit(text_surf, (x,y))






def ui():
    run = True
    start = False
    typing = True
    typed = ""
    with open("quests.txt", "r", encoding="utf-8") as q:
        quests = q.readlines()
    ques = []
    for quest in quests:
        ques.append(quest)
    quest_for_today = random.choice(ques)
            
    while run:
        disp.fill(white)
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if typing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        typing = False
                        start = True
                    elif event.key == pygame.K_BACKSPACE:
                        typed = typed[:-1]
                    else:
                        typed += event.unicode
        
              
        if typing:
            display_text("Get daily quest.", 200, 100, 50, black)
            display_text(typed, 300, 200, 50, black)

        elif start:
            disp.fill(black)

            display_text(quest_for_today, 100, 200, 15, white)
            
            
        pygame.display.update()


ui()


    

