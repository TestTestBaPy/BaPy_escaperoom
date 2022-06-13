import pygame

def text_objects(text,font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()