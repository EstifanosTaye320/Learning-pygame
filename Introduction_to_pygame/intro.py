import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

radius = 50
y = screen.get_height() / 2- radius/4
x= screen.get_width() / 2 - radius/4

y_line = screen.get_height() -200

running = True
gravity = 0.1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")
    pygame.draw.line(screen, (0,0,255), (0 + 50, y_line - 250), (screen.get_width() - 50, y_line -250))
    pygame.draw.circle(screen ,(255, 0, 0), (x, y), 50)
    pygame.draw.line(screen, (0,0,255), (0 + 50, y_line), (screen.get_width() - 50, y_line))
    y += gravity

    if y + 50 >= y_line or y <= y_line - 200:
        gravity = -gravity

    pygame.display.flip()

pygame.quit()