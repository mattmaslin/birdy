import pygame
from pygame.locals import *

from bird import Bird
from pipe import PipeGroup

pygame.init()
clock = pygame.time.Clock()
fps = 60

game_started = False
game_over = False


screen_width = 768
screen_height = 936
screen = pygame.display.set_mode((screen_width,screen_height),0, 32)
pygame.display.set_caption("Flappy Bird")  

#load images
bg = pygame.image.load("./images/bg.png")
ground_img = pygame.image.load("./images/ground.png")
restart_img = pygame.image.load("./images/restart.png")
restart_img = pygame.transform.scale(restart_img, (240, 84))
restart_width = restart_img.get_width()
restart_heigt = restart_img.get_height()


# define game variables 
scroll_speed = 4
ground_scroll = 0

        
bird_group = pygame.sprite.Group()
pipe_group = PipeGroup(screen_width)
flappy = Bird(100, int(768 / 2))
font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 52)
text = None

bird_group.add(flappy)

run = True
last_count = -1
while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    
    bird_group.draw(screen)
    pipe_group.draw(screen)
    #draw and scroll ground
    screen.blit(ground_img, (ground_scroll, 768))
    if game_over:
        screen.blit(restart_img, (screen_width/2 - restart_width / 2,screen_height/2 - restart_heigt/2))
    if last_count != pipe_group.counter:
        text = font.render(f"Pipes: {pipe_group.counter}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen_width - 100, 22)     
    
    screen.blit(text, text_rect)
    if game_started:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        bird_group.update()
        pipe_group.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_started == False and game_over == False:            
            game_started = True
        if event.type == pygame.MOUSEBUTTONDOWN and game_over == True:
            flappy.reset()
            pipe_group.reset()
            game_over = False
            game_started = True
            
    if flappy.rect.bottom >= 768:
        game_over = True
        game_started = False
    if flappy.rect.top <= 0:
        game_over = True
        game_started = False
        
    if game_started == True and pipe_group.does_collide(flappy):
        game_over = True
        game_started = False            
    
    pygame.display.update()
pygame.quit() 