import pygame
import sys

# 游戏窗口相关参数
WIDTH = 800
HEIGHT = 600
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 砖块相关参数
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_COLOR = RED

# 小球相关参数
BALL_RADIUS = 10
BALL_SPEED_X = 10
BALL_SPEED_Y = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# 挡板相关参数
PADDLE_WIDTH = 500
PADDLE_HEIGHT = 15
PADDLE_SPEED = 10
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 50

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打砖块游戏")
clock = pygame.time.Clock()

# 创建砖块矩阵
bricks = []
for row in range(BRICK_ROWS):
    brick_row = []
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + 5) + 50
        brick_y = row * (BRICK_HEIGHT + 5) + 50
        brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
        brick_row.append(brick_rect)
    bricks.append(brick_row)


# 绘制函数
def draw():
    screen.fill(BLACK)
    # 绘制砖块
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, BRICK_COLOR, brick)
    # 绘制小球
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), BALL_RADIUS)
    # 绘制挡板
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()


# 碰撞检测函数
def check_collision():
    global ball_dx, ball_dy
    # 小球与挡板碰撞检测
    if paddle_y <= ball_y <= paddle_y + PADDLE_HEIGHT and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        ball_dy = -ball_dy
    # 小球与砖块碰撞检测
    for row in range(len(bricks)):
        for col in range(len(bricks[row])):
            brick = bricks[row][col]
            if brick.colliderect(pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                ball_dy = -ball_dy
                bricks[row][col] = None
    # 过滤掉已被消除的砖块
    bricks[:] = [[brick for brick in row if brick is not None] for row in bricks]


# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += PADDLE_SPEED

    ball_x += ball_dx
    ball_y += ball_dy

    # 小球边界碰撞检测
    if ball_x < BALL_RADIUS or ball_x > WIDTH - BALL_RADIUS:
        ball_dx = -ball_dx
    if ball_y < BALL_RADIUS:
        ball_dy = -ball_dy
    elif ball_y > HEIGHT:
        print("游戏失败！")
        pygame.quit()
        sys.exit()

    check_collision()
    if not any(any(row) for row in bricks):
        print("游戏胜利！")
        pygame.quit()
        sys.exit()

    draw()
    clock.tick(FPS)