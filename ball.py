import pygame
from constants import *
import random
import math

mixer.init()

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ( (value - min1) / (max1 - min1))

class Ball:
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.radius = 20
        self.color = WHITE
        self.theta = random.uniform(-math.pi/3, math.pi/3)
        self.velX = BALL_SPEED * math.cos(self.theta)
        self.velY = BALL_SPEED * math.sin(self.theta)
        self.hitSound = pygame.mixer.Sound("./assets/hit.mp3")
        self.hitSound.set_volume(0.2)
        self.scoreSound = pygame.mixer.Sound("./assets/score.mp3")
        self.scoreSound.set_volume(0.1)

    def update(self):
        self.x += self.velX
        self.y += self.velY
            

    def Hit(self, paddle, left=True):
        if left:
            if self.y < paddle.y + paddle.height//2 and \
                self.y > paddle.y - paddle.height//2 and \
                self.x - self.radius < paddle.x + paddle.width//2:
                if self.x > paddle.x:
                    d = self.y - (paddle.y - paddle.height//2)
                    self.theta = translate(d, 0, paddle.height, -math.radians(45), math.radians(45))
                    
                    self.velX = BALL_SPEED * math.cos(self.theta)
                    self.velY = BALL_SPEED * math.sin(self.theta)
                    self.x = paddle.x + self.radius + paddle.width//2
                    self.hitSound.play()
        else:   
            if self.y < paddle.y + paddle.height//2 and \
                self.y > paddle.y - paddle.height//2 and \
                self.x + self.radius > paddle.x - paddle.width//2:
                if self.x < paddle.x:
                    d = self.y - (paddle.y - paddle.height//2)
                    self.theta = translate(d, 0, paddle.height, math.radians(225), math.radians(135))
                    
                    self.velX = BALL_SPEED * math.cos(self.theta)
                    self.velY = BALL_SPEED * math.sin(self.theta)
                    self.x = paddle.x - self.radius - paddle.width//2
                    self.hitSound.play()
