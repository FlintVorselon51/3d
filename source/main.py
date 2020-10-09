import numpy as np
import pygame
import functions
from Camera import Camera
from Circle import Circle
import json


if __name__ == '__main__':
    with open('save.json', 'r') as save_file:
        save = json.load(save_file)

    SCREEN_WIDTH = save['resolution'][0]
    SCREEN_HEIGHT = save['resolution'][1]
    camera = Camera(
        np.array(save['camera']['coordinates']),
        save['camera']['h-v-a'],
        save['camera']['v-v-a'],
        save['camera']['h-r']
    )

    objects = []

    for obj in save['objects']:
        objects.append(Circle(
            np.array((obj['coordinates'])),
            obj['radius'], 
            np.array((obj['color']))
        ))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    functions.send_rays(camera, screen, objects)
    pygame.display.update()
    while True:
        pass
