import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pipe_image):
        super().__init__()

        # Pass in the image or surface you're working with and the location of the object
        self.image = pipe_image
        self.rect = self.image.get_rect()

        # Position the image
        self.rect.x = x
        self.rect.y = y
        
opening_size = 400
velocity = 4
pipe_spacing = 400
initial_offset = 20
bird_buffer = 3

class PipeGroup():
    def __init__(self, screen_width) -> None:
        self.screen_width = screen_width
        bottom_image = pygame.image.load("./images/pipe.png")
        top_image = pygame.transform.rotate(bottom_image, 180)
        self.pipe_count = int(screen_width / pipe_spacing) + 2
        self.pipes = []
        self.counter = 0
        self.group = pygame.sprite.Group()
        for i in range(0, self.pipe_count):
            x = screen_width + initial_offset + (pipe_spacing * i)
            opening = random.randint(200, 768-200)                  
            top_pipe = Pipe(x, opening - int(opening_size/2) - 560, top_image)
            bottom_pipe = Pipe(x, opening + 50, bottom_image)
            self.pipes.append((top_pipe, bottom_pipe))
            self.group.add(top_pipe)
            self.group.add(bottom_pipe)
            
    def reset(self):
        self.counter = 0
        for i in range(0, self.pipe_count):
            x = self.screen_width + initial_offset + (pipe_spacing * i)
            pipe = self.pipes[i]
            pipe[0].rect.x = x
            pipe[1].rect.x = x
            new_opening = random.randint(200, 768-200) + (opening_size/2)
            y_difference = new_opening - pipe[1].rect.y
            pipe[0].rect.y += y_difference
            pipe[1].rect.y += y_difference
            
    def draw(self, screen):
        self.group.draw(screen)
        
    def update(self):
        for pipe in self.pipes:
            pipe[0].rect.x -= velocity
            pipe[1].rect.x -= velocity
            if pipe[0].rect.right < 0:
                self.counter += 1
                pipe[0].rect.right = self.pipe_count * pipe_spacing
                pipe[1].rect.right = self.pipe_count * pipe_spacing
                new_opening = random.randint(200, 768-200) + (opening_size/2)
                y_difference = new_opening - pipe[1].rect.y
                pipe[0].rect.y += y_difference
                pipe[1].rect.y += y_difference
                
    def does_collide(self, bird) -> bool:
        bird_rect = pygame.Rect(bird.rect.left + bird_buffer, 
                                bird.rect.top + bird_buffer, 
                                bird.rect.width - (bird_buffer*2), 
                                bird.rect.height - (bird_buffer*2))
        for pipe in self.pipes:
            if pipe[0].rect.colliderect(bird_rect) or pipe[1].rect.colliderect(bird_rect):
                return True
            
        return False
             