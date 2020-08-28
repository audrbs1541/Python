import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello, Vincent!")

clock = pygame.time.Clock()
run = True
gb = [255,255]

# Game Loop
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 2) 게임 논리 실행
    if gb[0] == 0:
        direction = 1
    elif gb[0] == 255:
        direction = 2
        
    if direction == 1:
        gb[0] += 1
        gb[1] += 1
    elif direction == 2:
        gb[0] -= 1
        gb[1] -= 1


    # 3) 게임 장면 그리기
    screen.fill(pygame.color.Color(gb[0],255,gb[1]))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
