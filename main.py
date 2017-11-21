import pygame
import random
'''
task: collision
'''
pygame.init()

display_width = 1280
display_height = 720
block_size = 10
FPS = 20
score = 0
gun_range = 300

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
font = pygame.font.SysFont(None, 25)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Killer")

pygame.display.update()

gameExit = False
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])


def menu():
    gameDisplay.fill(red)
    message_to_screen("Welcome in killer game", black, display_width/2 - 80, display_height/2)
    message_to_screen("Press any key to play", black, display_width/2 - 80, display_height/3)
    pygame.display.update()
    clock.tick(0.5)


def score_counter(sc):
    sc += 1
    return sc


def new_enemy_position():
    x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    return x, y


enemy_x, enemy_y = new_enemy_position()


def check_hit(en_x, en_y, bullet_x, bullet_y):
    if en_x == bullet_x:
        if en_y == bullet_y:
            global enemy_x
            global enemy_y
            enemy_x, enemy_y = new_enemy_position()
            spawn_enemy(enemy_x, enemy_y)
            global score
            new_score = score_counter(score)
            score = new_score
            return True
    return False


def shoot(ev, x, y, enemy_x, enemy_y):
    i = 0

    bullet_x = x
    bullet_y = y

    if ev == pygame.K_d:
        while i < gun_range:
            gameDisplay.fill(white)
            spawn_character(lead_x, lead_y)
            spawn_enemy(enemy_x, enemy_y)
            bullet_x = x + i + 20
            pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y, 10, 10])
            i += 10
            if check_hit(enemy_x, enemy_y, bullet_x, bullet_y):
                break
            pygame.display.flip()
            clock.tick(100)

    elif ev == pygame.K_a:
        while i > - gun_range:
            gameDisplay.fill(white)
            spawn_character(lead_x, lead_y)
            spawn_enemy(enemy_x, enemy_y)
            bullet_x = x + i - 20
            pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y, 10, 10])
            i -= 10
            if check_hit(enemy_x, enemy_y, bullet_x, bullet_y):
                break
            pygame.display.flip()
            clock.tick(100)

    elif ev == pygame.K_w:
        while i > - gun_range:
            gameDisplay.fill(white)
            spawn_character(lead_x, lead_y)
            spawn_enemy(enemy_x, enemy_y)
            bullet_y = y + i - 20
            pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y, 10, 10])
            i -= 10
            if check_hit(enemy_x, enemy_y, bullet_x, bullet_y):
                break
            pygame.display.flip()
            clock.tick(100)

    elif ev == pygame.K_s:
        while i < gun_range:
            gameDisplay.fill(white)
            spawn_character(lead_x, lead_y)
            spawn_enemy(enemy_x, enemy_y)
            bullet_y = y + i + 20
            pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y, 10, 10])
            i += 10
            if check_hit(enemy_x, enemy_y, bullet_x, bullet_y):
                break
            pygame.display.flip()
            clock.tick(100)

    return bullet_x, bullet_y


def spawn_enemy(x, y):
    pygame.draw.rect(gameDisplay, green, [x, y, 10, 10])


def spawn_character(x, y):
    pygame.draw.rect(gameDisplay, black, [x, y, 10, 10])


class Level:
    def __init__(self, number, start_x, start_y):
        # we say what lvl is this and where main char has to spawn
        self.number = number
        self.start_x = start_x
        self.start_y = start_y

    def draw_background(self):
        if self.number == 1:
            pass
        elif self.number == 2:
            pass
        elif self.number == 3:
            pass

    def change(self):
        self.number += 1


menu()

while not gameExit:

    gameDisplay.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
            if event.key == pygame.K_UP:
                lead_y_change = -10
            if event.key == pygame.K_DOWN:
                lead_y_change = 10

            if event.key == pygame.K_w or pygame.K_a or pygame.K_s or pygame.K_d:
                shoot(event.key, lead_x, lead_y, enemy_x, enemy_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change

    spawn_enemy(enemy_x, enemy_y)
    spawn_character(lead_x, lead_y)
    message_to_screen("Score: {}".format(score), black, display_width/2, 40)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

quit()

