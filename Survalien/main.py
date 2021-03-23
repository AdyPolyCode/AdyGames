# Main modules -> PYGAME, RANDOM
# Game consist of 2 main object -> ALIEN and METEOR
# Alien has an extra speed function


import pygame
from pygame.locals import *
import random

pygame.init()


class Alien(pygame.sprite.Sprite):

    def __init__(self, path, x, y):
        super().__init__()
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.hp = 5
        self.hp_image = pygame.image.load('heart.png').convert()
        self.hp_image.set_colorkey((0, 0, 0))
        self.speed = 5
        self.speed_count = 3
        self.faster = False
        self.trigger = False

    def update(self):
        self.control()
        self.display_health()

    # MOVEMENT CONTROL
    def control(self):
        movement = pygame.key.get_pressed()
        if movement[K_UP] and self.rect.centery >= self.rect.height // 2:
            self.rect.centery -= self.speed
        if movement[K_DOWN] and self.rect.centery <= screenH - self.rect.height // 2:
            self.rect.centery += self.speed
        if movement[K_LEFT] and self.rect.centerx >= self.rect.width // 2:
            self.rect.centerx -= self.speed
        if movement[K_RIGHT] and self.rect.centerx <= screenW - self.rect.width // 2:
            self.rect.centerx += self.speed
        if movement[K_SPACE] and self.speed_count == 3:
            self.trigger = True
        if self.trigger:
            if self.trigger and self.speed_count <= 3:
                self.speed_run()
                self.speed_count -= 0.02
            if self.trigger and self.speed_count <= 1:
                self.speed_count = 0
                self.faster = False
                self.speed_run()
        if not movement[K_SPACE]:
            if not self.trigger and self.speed_count <= 3:
                self.speed_count += 0.005
            if not self.trigger and self.speed_count >= 3:
                self.speed_count = 3
                self.faster = True

    def display_health(self):
        for i, h in enumerate(range(self.hp)):
            screen.blit(self.hp_image, (10 + 40 * i, 10))

    # EXTRA SPEED WHEN YOU PRESS SPACE
    def speed_run(self):
        if self.faster:
            if self.speed <= 20:
                self.speed *= 1.2
        else:
            if self.speed >= 5:
                self.speed -= 0.2
            elif self.speed <= 5:
                self.speed = 5
                self.trigger = False


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x, y, x_speed, y_speed):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        if self.x < 0:
            self.rect.centerx += self.x_speed
        if self.x > 1280:
            self.rect.centerx -= self.x_speed
        self.rect.centery += self.y_speed

        if self.rect.centerx >= 1500 or self.rect.centerx < -400:
            self.kill()


# set Window -> size, title, icon, game-fps, music, sound
screen = pygame.display.set_mode((1280, 720))
screenW, screenH = screen.get_width(), screen.get_height()
background = pygame.image.load('bg.png').convert()
pygame.display.set_caption('Survalien')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
fps = 120

music = pygame.mixer.music.load('alienblues.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

sound = pygame.mixer.Sound('got damage.wav')

# Initialize player -> img path, position, speed
player = Alien('ufo.png', 640, 360)
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

# Initialize enemy -> img path, position, speed
enemy_group = pygame.sprite.Group()
enemy_event = pygame.USEREVENT
pygame.time.set_timer(enemy_event, 100)


# Main function to draw both player and falling meteors + collision
def main():
    player_group.draw(screen)
    enemy_group.draw(screen)

    player_group.update()
    enemy_group.update()

    if pygame.sprite.spritecollide(player_group.sprite, enemy_group, True):
        player_group.sprite.hp -= 1
        sound.play()

    pygame.display.update()


# Game over Background + total score
def game_over():
    game_over_font = pygame.font.Font(None, 40)
    game_over_text = game_over_font.render('Game Over!', True, (255, 255, 255))
    screen.blit(game_over_text, (screenW // 2 - game_over_text.get_width() // 2, 360))

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f'Time survived: {time_survived} sec.', True, (255, 255, 255))
    screen.blit(score_text, (screenW // 2 - score_text.get_width() // 2, 400))

    play_again_font = pygame.font.Font(None, 32)
    play_again_text = play_again_font.render('Click to play again.', True, (255, 255, 255))
    screen.blit(play_again_text, (screenW // 2 - play_again_text.get_width() // 2, 440))

    pygame.display.update()


# Game score + timer to increase score by 1 (1000 millisecond == 1 second)
score_time = pygame.USEREVENT
pygame.time.set_timer(score_time, 1000)
time_survived = 0
# Main loop
run = True
while run:
    screen.blit(background, (0, 0))
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False

        if event.type == enemy_event:
            randomXEnd = random.randrange(1300, 1400)
            randomXStart = random.randrange(-300, -100)
            randomX = [randomXEnd, randomXStart]
            randomY = random.randrange(50, 650)
            randomXSpeed = random.randrange(5, 15)
            randomYSpeed = random.randrange(1, 2)
            enemy = Meteor('meteor.png', random.choice(randomX), randomY, randomXSpeed, randomYSpeed)
            enemy_group.add(enemy)
        if event.type == score_time and player_group.sprite.hp > 0:
            time_survived += 1
        if event.type == MOUSEBUTTONDOWN:
            time_survived = 0
            player_group.sprite.hp = 5

    if player_group.sprite.hp > 0:
        main()
    else:
        game_over()
