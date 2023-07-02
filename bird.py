import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [] 

        self.x = x
        self.y = y
        for number in range (1,4):
            img =  pygame.image.load(f"./images/bird{number}.png")
            self.images.append(img)
            
        self.reset()
        
        
    def reset(self):
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.images[self.index].get_rect()        
        self.rect.center = [self.x, self.y] 
        self.velocity = 0
        self.clicked = False
        
    def update(self):
        #gravity       
        self.velocity += 0.5        
        if self.velocity > 8:
            self.velocity = 8
            
        if (self.rect.bottom < 768 or self.velocity < 0) and (self.rect.top > 0 or self.velocity > 0):
            self.rect.y += int(self.velocity)
        
        # jump
        # if mouse is pressed and clicked is false
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.velocity = -10
            # set clicked
            self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # animation
        self.counter += 0.5
        if self.counter > 5:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            
        #rotate
        self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)

        