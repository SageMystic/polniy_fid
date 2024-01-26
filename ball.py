import pygame
from pygame import mixer
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
        self.angle = random.uniform(-math.pi/3, math.pi/3)
        self.velX = BALL_SPEED * math.cos(self.angle)
        self.velY = BALL_SPEED * math.sin(self.angle)
        self.hitSound = mixer.Sound("./assets/hit.mp3")
        self.hitSound.set_volume(0.2)
        self.scoreSound = mixer.Sound("./assets/score.mp3")
        self.scoreSound.set_volume(0.1)

    def update(self):
        self.x += self.velX
        self.y += self.velY
            

    def Hit(self, racket, left=True): #прописали поведение шарика после удара
        if left: #проверяется с левой ракеткой
            if self.y < racket.y + racket.height//2 and \
                self.y > racket.y - racket.height//2 and \
                self.x - self.radius < racket.x + racket.width//2:
                '''Проверка на соударение с левой ракеткой'''
                if self.x > racket.x: #мяч правее ракетки
                    d = self.y - (racket.y - racket.height//2)#расстояние от центра ракетки до корды y мяча
                    self.angle = translate(d, 0, racket.height, -math.radians(45), math.radians(45))
                    #угол под которым полетит мяч после удара
                    self.velX = BALL_SPEED * math.cos(self.angle)
                    self.velY = BALL_SPEED * math.sin(self.angle)
                    self.x = racket.x + self.radius + racket.width//2
                    self.hitSound.play()
        else:   #проверяется с правой ракеткой
            if self.y < racket.y + racket.height//2 and \
                self.y > racket.y - racket.height//2 and \
                self.x + self.radius > racket.x - racket.width//2:
                '''Проверка на соударение с правой ракеткой'''
                if self.x < racket.x:
                    d = self.y - (racket.y - racket.height//2)
                    self.angle = translate(d, 0, racket.height, math.radians(225), math.radians(135))
                    #угол под которым полетит мяч после удара
                    self.velX = BALL_SPEED * math.cos(self.angle)
                    self.velY = BALL_SPEED * math.sin(self.angle)
                    self.x = racket.x - self.radius - racket.width//2
                    self.hitSound.play()
                    

    def Boundary(self, left_score, right_score): #касание мяча стенки
        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= HEIGHT:
            self.velY *= -1

        if (self.x - self.radius) <= 0:
            self.Reset()
            right_score += 1
            self.scoreSound.play()

        elif (self.x + self.radius) >= WIDTH:
            self.Reset()
            left_score += 1
            self.scoreSound.play()


        return left_score, right_score

    def Reset(self): #возвращение в начало игры
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.angle = random.uniform(-math.pi/3, math.pi/3)#новый угол под которым полетит мяч

        self.velX = BALL_SPEED * math.cos(self.angle)
        self.velY = BALL_SPEED * math.sin(self.angle)

        if random.random() > 0.5: #в какую сторону полетит мяч
            self.velX *= -1

    def Draw(self, screen):#отрисовка мяча
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
