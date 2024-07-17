import pygame
import requests

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.SysFont('Arial', 35)

# Example Sudoku grid (0 represents empty cells)
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(window, (0, 0, 0), (50 * i, 0), (50 * i, 450), thickness)
        pygame.draw.line(window, (0, 0, 0), (0, 50 * i), (450, 50 * i), thickness)

def draw_numbers():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                value = font.render(str(grid[i][j]), True, (0, 0, 0))
                window.blit(value, (j * 50 + 15, i * 50 + 15))

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

def main():
    run = True
    solving = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True

        window.fill((255, 255, 255))
        draw_grid()
        draw_numbers()

        if solving:
            solve(grid)
            solving = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
