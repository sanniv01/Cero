import pygame
import random

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]],  # Z shape
    [[1, 0, 0], [1, 1, 1]],  # L shape
    [[0, 0, 1], [1, 1, 1]],  # J shape
]

class Tetris:
    def __init__(self):
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_shape = self.new_shape()
        self.shape_x = 3
        self.shape_y = 0
        self.game_over = False

    def new_shape(self):
        return random.choice(SHAPES)

    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def collision(self, dx, dy):
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    board_x = self.shape_x + x + dx
                    board_y = self.shape_y + y + dy
                    if (board_x < 0 or board_x >= len(self.board[0]) or
                        board_y >= len(self.board) or self.board[board_y][board_x]):
                        return True
        return False

    def fix_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    self.board[self.shape_y + y][self.shape_x + x] = 1

    def clear_lines(self):
        new_board = [row for row in self.board if any(x == 0 for x in row)]
        while len(new_board) < len(self.board):
            new_board.insert(0, [0] * len(self.board[0]))
        self.board = new_board

    def move(self, dx, dy):
        if not self.game_over:
            if not self.collision(dx, dy):
                self.shape_x += dx
                self.shape_y += dy
            else:
                if dy:
                    self.fix_shape()
                    self.clear_lines()
                    self.current_shape = self.new_shape()
                    self.shape_x = 3
                    self.shape_y = 0
                    if self.collision(0, 0):
                        self.game_over = True  # Game over condition

    def draw(self, screen):
        for y, row in enumerate(self.board):
            for x, value in enumerate(row):
                if value:
                    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    pygame.draw.rect(screen, GREEN, ((self.shape_x + x) * BLOCK_SIZE, (self.shape_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Tetris()

    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                if event.key == pygame.K_DOWN:
                    game.move(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate_shape()
        game.move(0, 1)
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()