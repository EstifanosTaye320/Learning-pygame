import pygame

pygame.init()
pygame.display.set_caption("Background Image Pygame")
pygame.display.set_icon(pygame.image.load("user.png"))
pygame.display.set_palette
width = 800
height = 150
screen = pygame.display.set_mode((width, height))
running = True

font = pygame.font.Font("Caramel.ttf", 40)
# text = font.render("Estifanos Taye The Engineer", True, (69, 245, 168))
text = font.render("= Estifanos Taye The Jolly Engineer :)", True, (84, 247, 176))
text_rect = text.get_frect(center=(width/2 + 20, height/2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((71, 46, 69))
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()
quit()