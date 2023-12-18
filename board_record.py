import pygame
pygame.init()

pixel_width, pixel_height = 25, 25

board_recorder = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

block_key = {
    "i_block": [[1], [1], [1], [1]],
    "j_block": [[1], [1, 1, 1]],
    "l_block": [[0, 0, 1], [1, 1, 1]],
    "o_block": [[1, 1], [1, 1]],
    "s_block": [[0, 1, 1], [1, 1]],
    "t_block": [[0, 1], [1, 1, 1]],
    "z_block": [[1, 1], [0, 1, 1]],
    "i_block_1": [[1, 1, 1, 1], [0]],
    "j_block_1": [[0, 1], [0, 1], [1, 1]],
    "l_block_1": [[1, 1], [0, 1], [0, 1]],
    "o_block_1": [[1, 1], [1, 1]],
    "s_block_1": [[1], [1, 1], [0, 1]],
    "t_block_1": [[0, 1], [1, 1], [0, 1]],
    "z_block_1": [[0, 1], [1, 1], [1]],
    "i_block_2": [[1], [1], [1], [1]],
    "j_block_2": [[1, 1, 1], [0, 0, 1]],
    "l_block_2": [[1, 1, 1], [1]],
    "o_block_2": [[1, 1], [1, 1]],
    "s_block_2": [[0, 1, 1], [1, 1]],
    "t_block_2": [[1, 1, 1], [0, 1]],
    "z_block_2": [[1, 1], [0, 1, 1]],
    "i_block_3": [[1, 1, 1, 1], [0]],
    "j_block_3": [[1, 1], [1], [1]],
    "l_block_3": [[1], [1], [1, 1]],
    "o_block_3": [[1, 1], [1, 1]],
    "s_block_3": [[1], [1, 1], [0, 1]],
    "t_block_3": [[1], [1, 1], [1]],
    "z_block_3": [[0, 1], [1, 1], [1]]
}

block_values = {
    "i_block": 2,
    "j_block": 3,
    "l_block": 4,
    "o_block": 5,
    "s_block": 6,
    "t_block": 7,
    "z_block": 8
}

colors = {
    2: pygame.image.load("art/Single Blocks/LightBlue.png"),
    3: pygame.image.load("art/Single Blocks/Blue.png"),
    4: pygame.image.load("art/Single Blocks/Orange.png"),
    5: pygame.image.load("art/Single Blocks/Yellow.png"),
    6: pygame.image.load("art/Single Blocks/Green.png"),
    7: pygame.image.load("art/Single Blocks/Purple.png"),
    8: pygame.image.load("art/Single Blocks/Red.png")
}

for i in range(2, 9):
    colors[i] = pygame.transform.scale_by(colors[i], 0.4)


def check_blocks(block_type, x, y, side_check, updown, rotated):
    right = int(x / 25) + side_check
    down = int(y / 25) + updown
    if rotated:
        block = block_key[block_type + "_" + str(rotated)]
    else:
        block = block_key[block_type]
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                if board_recorder[down + i][right + j] != 0:
                    return False
    return True


def set_blocks(block_type, x, y, rotated):
    right = int(x / 25)
    down = int(y / 25)
    if rotated:
        block = block_key[block_type + "_" + str(rotated)]
    else:
        block = block_key[block_type]
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                board_recorder[down + i][right + j] = block_values[block_type]


def delete():
    full = True
    point_gain = 0
    for row in range(1, 22):
        for col in range(1, 11):
            if board_recorder[row][col] == 0 or board_recorder[row][col] == 1:
                full = False
        if full:
            board_recorder.pop(row)
            board_recorder.insert(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            point_gain += 1
        full = True
    return point_gain
