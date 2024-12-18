import pygame
import random

# 初始化 pygame
pygame.init()

# 游戏窗口设置
BLOCK_SIZE = 20  # 每个方块的大小
SCREEN_WIDTH = BLOCK_SIZE * 10 * 2  # 设置屏幕宽度
SCREEN_HEIGHT = BLOCK_SIZE * 20 * 2 # 设置屏幕高度
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 方块设置
COLUMN_COUNT = SCREEN_WIDTH // BLOCK_SIZE
ROW_COUNT = SCREEN_HEIGHT // BLOCK_SIZE

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I形
    [[1, 1], [1, 1]],  # O形
    [[0, 1, 0], [1, 1, 1]],  # T形
    [[1, 1, 0], [0, 1, 1]],  # S形
    [[0, 1, 1], [1, 1, 0]],  # Z形
    [[1, 0, 0], [1, 1, 1]],  # L形
    [[0, 0, 1], [1, 1, 1]],  # J形
]

SHAPES_COLORS = [CYAN, YELLOW, GREEN, RED, BLUE, MAGENTA, ORANGE]


# 方块类
class Tetrimino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = COLUMN_COUNT // 2 - len(shape[0]) // 2  # 方块初始位置X
        self.y = 0  # 方块初始位置Y

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]  # 顺时针旋转


# 游戏类
class Tetris:
    def __init__(self):
        self.board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = SHAPES_COLORS[SHAPES.index(shape)]
        return Tetrimino(shape, color)

    def valid_position(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, block in enumerate(row):
                if block:
                    if (self.current_piece.x + x < 0 or self.current_piece.x + x >= COLUMN_COUNT or
                        self.current_piece.y + y >= ROW_COUNT or
                        self.board[self.current_piece.y + y][self.current_piece.x + x]):
                        return False
        return True

    def place_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, block in enumerate(row):
                if block:
                    self.board[self.current_piece.y + y][self.current_piece.x + x] = SHAPES_COLORS.index(self.current_piece.color) + 1
        self.clear_lines()
        self.current_piece = self.new_piece()
        if not self.valid_position():
            self.game_over = True

    def clear_lines(self):
        full_lines = [i for i, row in enumerate(self.board) if all(cell != 0 for cell in row)]
        for line in full_lines:
            del self.board[line]
            self.board.insert(0, [0] * COLUMN_COUNT)
            self.score += 10  # 每行消除加分

    def move_piece(self, dx, dy):
        self.current_piece.x += dx
        self.current_piece.y += dy
        if not self.valid_position():
            self.current_piece.x -= dx
            self.current_piece.y -= dy
            if dy > 0:  # 如果方块是下落的
                self.place_piece()  # 固定当前方块，并生成一个新的方块
            return False
        return True

    def rotate_piece(self):
        self.current_piece.rotate()
        if not self.valid_position():
            self.current_piece.rotate()
            self.current_piece.rotate()
            self.current_piece.rotate()  # 恢复旋转

        return True

    def draw(self):
        SCREEN.fill(BLACK)

        # 画每一块
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                if self.board[y][x]:
                    pygame.draw.rect(SCREEN, SHAPES_COLORS[self.board[y][x] - 1], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # 画当前方块
        for y, row in enumerate(self.current_piece.shape):
            for x, block in enumerate(row):
                if block:
                    pygame.draw.rect(SCREEN, self.current_piece.color, ((self.current_piece.x + x) * BLOCK_SIZE, (self.current_piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # 显示分数
        font = pygame.font.SysFont('arial', 24)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.update()


# 游戏循环
def main():
    clock = pygame.time.Clock()
    tetris = Tetris()

    while not tetris.game_over:
        clock.tick(10)  # 控制游戏速度，10帧每秒

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tetris.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_piece(-1, 0)  # 向左移动
                if event.key == pygame.K_RIGHT:
                    tetris.move_piece(1, 0)  # 向右移动
                if event.key == pygame.K_DOWN:
                    tetris.move_piece(0, 1)  # 向下加速下落
                if event.key == pygame.K_UP:  # 上箭头旋转
                    tetris.rotate_piece()  # 旋转方块

        tetris.move_piece(0, 1)  # 自动下落
        tetris.draw()

    pygame.quit()


if __name__ == "__main__":
    main()
#上为变换键