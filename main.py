import pygame
import sys
import board_record
import random

# initializes pygame screen and sets up framerate
pygame.init()
screen = pygame.display.set_mode((300, 550))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# creates the pygame board and scales it
board = pygame.image.load("art/Board.png").convert()
board = pygame.transform.scale(board, (300, 550))

# creates the pieces for the game and scales them
active_pieces = [pygame.image.load("art/I.png").convert_alpha(),
                 pygame.image.load("art/J.png").convert_alpha(),
                 pygame.image.load("art/L.png").convert_alpha(),
                 pygame.image.load("art/O.png").convert_alpha(),
                 pygame.image.load("art/S.png").convert_alpha(),
                 pygame.image.load("art/T.png").convert_alpha(),
                 pygame.image.load("art/Z.png").convert_alpha()]

for i in range(len(active_pieces)):
    active_pieces[i] = pygame.transform.scale_by(active_pieces[i], 0.4)

# creates the corresponding dictionary to fill in block type
active_dict = {
    0: "i_block",
    1: "j_block",
    2: "l_block",
    3: "o_block",
    4: "s_block",
    5: "t_block",
    6: "z_block"
}

# sets the original (x, y) values for where the blocks spawn on the screen
x, y = 100, 50
# randomly selects a block from the array of active pieces
selection = random.randint(0, 6)
active_block = active_pieces[selection]
rotated = 0
new_rotation = rotated

points = 0
font = pygame.font.Font('art/fonts/KnightWarrior-w16n8.otf', 24)
points_text = font.render('Points: 0', True, "black", "white")
points_rect = points_text.get_rect(topright=(300, 5))

speed = 1

# game loop
playing = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and board_record.check_blocks(active_dict[selection], x, y, -1, 0, rotated):
                    x -= 25
                if event.key == pygame.K_RIGHT and board_record.check_blocks(active_dict[selection], x, y, 1, 0, rotated):
                    x += 25
                if event.key == pygame.K_SPACE:
                    if rotated < 3:
                        new_rotation = rotated + 1
                    else:
                        new_rotation = 0

                    if board_record.check_blocks(active_dict[selection], x, y, 1, 0, new_rotation):
                        active_block = pygame.transform.rotate(active_block, 90)
                        rotated = new_rotation
                    new_rotation = rotated

                if event.key == pygame.K_DOWN:
                    speed = points * 2 + 3
                else:
                    speed = points * .01 + 1

        screen.blit(board, (0, 0))

        for row in range(len(board_record.board_recorder)):
            for col in range(len(board_record.board_recorder[row])):
                if board_record.board_recorder[row][col] != 0 and board_record.board_recorder[row][col] != 1:
                    screen.blit(board_record.colors[board_record.board_recorder[row][col]], (col * 25, row * 25))

        screen.blit(active_block, (x, y))

        if board_record.check_blocks(active_dict[selection], x, y, 0, 1, rotated):
            y = y + 3 * speed
        else:
            if y < 75:
                playing = False
            board_record.set_blocks(active_dict[selection], x, y, rotated)
            selection = random.randint(0, 6)
            x, y = 100, 50
            active_block = active_pieces[selection]
            rotated = False
            speed = points * .01 + 1
        screen.blit(points_text, points_rect)
        points += board_record.delete()
        points_text = font.render('Points: ' + str(points), True, "black", "white")
        points_rect = points_text.get_rect(topright=(300, 5))

        pygame.display.flip()
        clock.tick(30)
    pygame.display.flip()
    clock.tick(30)
