import pygame
import random
from constants import *
from ball import Ball
from racket import Racket

def main():
    pygame.init()
    pygame.mixer.init()#модуль для звуков
    screen = pygame.display.set_mode((WIDTH, HEIGHT))#WIDTH, HEIGHT лежат в файле константс
    pygame.display.set_caption("Ping-Pong")
    clock = pygame.time.Clock()
    game = Game(screen, clock)
    game.Run()

    pygame.quit()

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fps = 60
        self.running = True
        self.background = pygame.image.load("./assets/BACKGROUND_PING_PONG.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("consolas", FONT_SIZE)#ШРИФТ И ЕГО РАЗМЕР
        self.ball = Ball()
        self.left_racket = Racket(RACKET_OFFSET)
        self.right_racket = Racket(WIDTH - RACKET_OFFSET)#RACKET_OFFSET лежит в константах
        
        self.left_score = 0
        self.right_score = 0
    
    def DrawScore(self): #отрисовка счета
        left_text = self.font.render(str(self.left_score), True, WHITE)
        self.screen.blit(left_text, (WIDTH//10, HEIGHT//12)) # рендер счёта
        right_text = self.font.render(str(self.right_score), True, WHITE)
        self.screen.blit(right_text, (WIDTH - 100, HEIGHT//12))
    def Run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0)) #рендер счёта
            self.HandleEvent()

            self.ball.update()
            self.left_score, self.right_score = self.ball.Boundary(self.left_score, self.right_score)

            self.ball.Hit(self.left_racket, True)
            self.ball.Hit(self.right_racket, False)

            self.ball.Draw(self.screen)
            self.left_racket.Draw(self.screen)
            self.right_racket.Draw(self.screen)

            self.DrawScore()

            pygame.display.update()
            self.clock.tick(self.fps)
    
    def HandleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#при нажатие крестика игра закроется
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# при нажатие esc игра закроется
                    self.running = False
        
        key = pygame.key.get_pressed()#прописали управление ракетками
        if key[pygame.K_w]:
            self.left_racket.update(-1 * RACKET_SPEED)
            self.left_racket.Boundary()
        elif key[pygame.K_s]:
            self.left_racket.update(1 * RACKET_SPEED)
            self.left_racket.Boundary()
        if key[pygame.K_UP]:
            self.right_racket.update(-1 * RACKET_SPEED)
            self.right_racket.Boundary()
        elif key[pygame.K_DOWN]:
            self.right_racket.update(1 * RACKET_SPEED)
            self.right_racket.Boundary()
                    

if __name__ == "__main__":
    main()
