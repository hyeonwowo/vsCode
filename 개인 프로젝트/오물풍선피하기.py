# -*- coding: utf-8 -*-
import sys
import pygame
import random
#version
VERSION = '1.0'
#display
WIDTH = 800
HEIGHT = 600
#color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 12)
DARK_ORANGE = (196, 121, 67)
#scene
STARTSCENE = 'start_scene'
PLAYGAME = 'PLAY_game'
GAMEOVER = 'game_Over'
QUIT = 'quit'
#fps
FPS = 60
#pygame
pygame.init()
pygame.font.init()

screen = None
font_title = pygame.font.Font(None, 65)
font_big = pygame.font.Font(None, 36)
font_default = pygame.font.Font(None, 28)

#option
SPEED = 1
BULLET_SPEED = 2
MAX_BULLET = 40
current_score = 0

class Airplane(pygame.sprite.Sprite):
    '''
    비행기
    '''
    def __init__(self, x, y):
        super(Airplane).__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect() #비행기 좌표
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        pygame.draw.circle(self.image, RED, (self.center_x, self.center_y), 10, 0)
        self.rect.x = x - self.center_x
        self.rect.y = y - self.center_y

    def move_position(self, x, y):
        '''
        비행기 위치변경 함수
        '''
        if (self.rect.x + x <= WIDTH - 2*self.center_x) and (self.rect.x + x >= 0):
            self.rect.x += x
        if (self.rect.y + y <= HEIGHT - 2*self.center_y) and (self.rect.y + y >=0):
            self.rect.y += y

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
        return None

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, x_speed, y_speed):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

        pygame.draw.circle(self.image, YELLOW, (self.center_x, self.center_y), 5, 0)
        self.rect.x = x_position
        self.rect.y = y_position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_thresh = 0
        self.y_thresh = 0

    def update(self):
        self.x_thresh += self.x_speed
        self.y_thresh += self.y_speed
        if abs(self.x_thresh) > 1:
            self.rect.x += int(self.x_thresh)
            self.x_thresh -= int(self.x_thresh)
        if abs(self.y_thresh) > 1:
            self.rect.y += int(self.y_thresh)
            self.y_thresh -= int(self.y_thresh)

        if self.is_edge():
            global current_score
            current_score += 1
            self.kill()

    def is_edge(self):
        if self.rect.x > WIDTH:
            return True
        elif self.rect.x < 0:
            return True
        if self.rect.y > HEIGHT:
            return True
        elif self.rect.y < 0:
            return True
        return False

def random_bullet():
    '''
    무작위 총알
    '''
    global BULLET_SPEED
    side = random.randint(1, 100) % 4
    if side == 0:
        #Top
        x_position = random.randint(0, WIDTH)
        y_position = 0
        x_speed = random.uniform(-1, 1)
        y_speed = random.uniform(0, 1)
    elif side == 1:
        #Bottom
        x_position = random.randint(0, WIDTH)
        y_position = HEIGHT
        x_speed = random.uniform(-1, 1)
        y_speed = random.uniform(-1, 0)
    elif side == 2:
        #Right
        x_position = WIDTH
        y_position = random.randint(0, HEIGHT)
        x_speed = random.uniform(-1, 0)
        y_speed = random.uniform(-1, 1)
    elif side == 3:
        #Left
        x_position = 0
        y_position = random.randint(0, HEIGHT)
        x_speed = random.uniform(0, 1)
        y_speed = random.uniform(-1, 1)
    return Bullet(x_position, y_position, x_speed/BULLET_SPEED, y_speed/BULLET_SPEED)

def draw_text(text, font, surface, x, y, main_color, back_color):
    '''
    화면에 글자를 쓰는 함수
    '''
    textobject = font.render(text, True, main_color, back_color)
    textrect = textobject.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobject, textrect)

def start_screen():
    '''
    시작장면
    '''
    global font_title
    global font_big
    global font_default
    global screen
    screen.fill(BLACK)

    draw_text('Mong Mong', font_title, screen, WIDTH/2, HEIGHT/3, RED, YELLOW)
    draw_text('press space', font_big, screen, WIDTH/2, HEIGHT*2/3, GREEN, BLACK)
    pygame.display.update()

    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 return PLAYGAME
             elif event.key == pygame.K_ESCAPE:
                return QUIT
         elif event.type == pygame.QUIT:
             return QUIT
    return STARTSCENE

def play_game():
    '''
    게임실행
    '''
    global font_default
    global screen
    global current_score

    pygame.key.set_repeat(1, 1)
    airplane = Airplane(WIDTH/2, HEIGHT/2)
    bullets = pygame.sprite.Group()

    while True:
        screen.fill(BLACK)
        draw_text('{0} points'.format(current_score), font_default, screen, WIDTH/1.1, 20, DARK_ORANGE, None)
        draw_text('{0} bullets'.format(len(bullets)), font_default, screen, WIDTH/10, 20, DARK_ORANGE, None)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    airplane.move_position(0, -1 * SPEED)
                if keys[pygame.K_DOWN]:
                    airplane.move_position(0, 1 * SPEED)
                if keys[pygame.K_RIGHT]:
                    airplane.move_position(1 * SPEED, 0)
                if keys[pygame.K_LEFT]:
                    airplane.move_position(-1 * SPEED, 0)
                if keys[pygame.K_ESCAPE]:
                    return GAMEOVER
        if airplane.collide(bullets):
            return GAMEOVER

        if len(bullets) < MAX_BULLET:
            bullets.add(random_bullet())
        bullets.update()
        bullets.draw(screen)

        screen.blit(airplane.image, airplane.rect)
        pygame.display.update()

def game_over():
    '''
    게임종료
    '''
    global font_default
    global font_big
    global screen
    global current_score

    screen.fill(BLACK)
    draw_text('Game Over', font_big, screen, WIDTH/2, HEIGHT/4, RED, WHITE)
    draw_text('Score : {0}'.format(current_score), font_default, screen, WIDTH/2, HEIGHT/2, YELLOW, None)
    draw_text('Press enter for back to main menu', font_default, screen, WIDTH/2, HEIGHT/3, YELLOW, None)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(BLACK)
                current_score = 0
                return STARTSCENE
            elif event.key == pygame.K_ESCAPE:
                return QUIT
    return GAMEOVER

def main_loop():
    '''
    3가지 장면 결정함수
    '''
    user_action = STARTSCENE
    while user_action != QUIT:
        if user_action == STARTSCENE:
            user_action = start_screen()
        elif user_action == PLAYGAME:
            user_action = play_game()
        elif user_action == GAMEOVER:
            user_action = game_over()
    pygame.quit()
    sys.exit(0)

def main(argv):
    '''
    프로그램 시작함수
    '''
    #display
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #caption
    pygame.display.set_caption(' 오물풍선피하기 ' + VERSION)
    #FPS
    fps_clock = pygame.time.Clock()
    fps_clock.tick(FPS)

    main_loop()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
