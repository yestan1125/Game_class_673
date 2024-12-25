import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口大小
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇游戏")

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 蛇的相关设置
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

# 食物的相关设置
food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

# 游戏主循环
clock = pygame.time.Clock()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # 蛇的移动
    snake_x += snake_x_change
    snake_y += snake_y_change

    # 判断蛇是否撞墙
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        game_over = True

    # 绘制背景
    window.fill(black)

    # 绘制食物
    pygame.draw.rect(window, green, [food_x, food_y, snake_block_size, snake_block_size])

    # 更新蛇的身体列表
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # 绘制蛇的身体
    for segment in snake_list:
        pygame.draw.rect(window, white, [segment[0], segment[1], snake_block_size, snake_block_size])

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
        food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size
        snake_length += 1

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
quit()