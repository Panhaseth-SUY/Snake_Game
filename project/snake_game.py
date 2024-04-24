# Add background image and music

import pygame
from pygame.locals import *
import time
from object import *


SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


class Game(Food, Snake):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.play_background_music()

        self.game_screen = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.game_screen)
        self.snake.draw()
        self.apple = Food(self.game_screen)
        self.apple.draw()

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()


    def reset(self):
        self.snake = Snake(self.game_screen)
        self.apple = Food(self.game_screen)


    def is_eating(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.game_screen.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating food scenario
        for i in range(self.snake.length):
            if self.is_eating(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.play_sound("ding")
                self.snake.increase_length()
                self.apple.move()

        # snake bite with itself
        # 4 blocks can bite itself that is why we set from 3 up
        for i in range(3, self.snake.length):
            if self.is_eating(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Snake bite itself"

        # snake bite with the boundries of the window
        
        if self.snake.x[0] > 960:
            self.snake.x[0] = 0
        elif self.snake.x[0] < 0:
            self.snake.x[0] = 960
        elif self.snake.y[0] > 800:
            self.snake.y[0] = 0
        elif self.snake.y[0] < 0:
            self.snake.y[0] = 800
        
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        level = font.render(f"Level: {self.snake.length // 15 + 1}",True, (200,200,200))
        self.game_screen.blit(level,(850,50))
        self.game_screen.blit(score,(850,10))
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.game_screen.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.game_screen.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        temp = pygame.event.get()
        while running:
            for event in pygame.event.get():
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        test = True
                        if event.key == K_LEFT:
                            if temp == K_RIGHT:
                                test = False
                            else:
                                self.snake.move_left()
                        if event.key == K_RIGHT:
                            if temp == K_LEFT:
                                test = False
                            else:
                                self.snake.move_right()

                        if event.key == K_UP:
                            if temp == K_DOWN:
                                test = False
                            else:
                                self.snake.move_up()

                        if event.key == K_DOWN:
                            if temp == K_UP:
                                test = False
                            else:
                                self.snake.move_down()
                        #avoiding back walking
                        if test:
                            temp = event.key
                        else:
                            pass
                        
                elif event.type == QUIT:
                    running = False
            try:
                #if hit lose condition it will stop
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()