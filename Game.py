# 파이게임 모듈을 불러 온다.
import pygame 

# 초기화 시킨다.
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 이미지를 갖고온다.
player = pygame.image.load("Shoot_Game/resources/images/dude.png")
grass = pygame.image.load("Shoot_Game/resources/images/grass.png")
castle = pygame.image.load("Shoot_Game/resources/images/castle.png")


# 계속 화면이 보이도록 한다.
while True:
    # 화면을 깨끗하게 한다.
    screen.fill((0,0,0))    # (R, G, B)
    
    # 모든 요소들을 다시 그린다.
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100,y*100))
    screen.blit(player, (100,100))

    # 화면을 다시 그린다.
    pygame.display.flip()

    # 게임을 종료한다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
