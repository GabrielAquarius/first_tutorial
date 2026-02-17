import os
import pygame


BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images

class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop) # Don't take extra memory because both are looking for the same thing
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images)) # It's not necessary to subtract 1 here because using % imply that we pass 0 (3%3 == 0)
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]
    