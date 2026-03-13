import pygame

print('Inicio da criação da window')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('Fim da criação da window')

print('Inicio do looping')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()