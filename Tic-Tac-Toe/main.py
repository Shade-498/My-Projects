import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 4  # Thickness of grid lines, cross, and circle
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (255, 255, 255)  # White background
LINE_COLOR = (0, 0, 0)      # Black grid lines
CIRCLE_COLOR = (0, 0, 255)  # Blue for O
CROSS_COLOR = (255, 0, 0)   # Red for X
TEXT_COLOR = (255, 255, 255)  # White text
TEXT_BG_COLOR = (0, 0, 0, 128)  # Semi-transparent black background for text

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Player vs Bot")
screen.fill(BG_COLOR)

# Font for displaying messages
font = pygame.font.SysFont(None, 50)  # Larger font size

# Board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw the grid lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw the figures (O and X)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                    CIRCLE_RADIUS, LINE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), LINE_WIDTH)

# Mark a square with 'X' or 'O'
def mark_square(row, col, player):
    board[row][col] = player

# Check if a square is available
def available_square(row, col):
    return board[row][col] is None

# Check if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Check for a win
def check_win(player):
    # Check vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # Check diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Bot's move (random)
def bot_move():
    available_moves = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] is None]
    if available_moves:
        return random.choice(available_moves)
    return None

# Display a message on the screen with a semi-transparent background
def display_message(message):
    # Create a semi-transparent background
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Semi-transparent black
    screen.blit(overlay, (0, 0))

    # Render the text
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Restart the game
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

# Main game loop
def main():
    draw_lines()
    player = 'X'  # Player starts first
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 'X':
                mouseX = event.pos[0]  # X coordinate
                mouseY = event.pos[1]  # Y coordinate

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    elif is_board_full():
                        game_over = True
                    else:
                        player = 'O'  # Switch to bot's turn

                    draw_figures()

                    # Bot's turn
                    if not game_over and player == 'O':
                        bot_row, bot_col = bot_move()
                        if bot_row is not None and bot_col is not None:
                            mark_square(bot_row, bot_col, 'O')
                            if check_win('O'):
                                game_over = True
                            elif is_board_full():
                                game_over = True
                            else:
                                player = 'X'  # Switch back to player's turn

                            draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game if 'R' is pressed
                    restart()
                    game_over = False
                    player = 'X'  # Reset to player's turn

        # Draw everything
        screen.fill(BG_COLOR)  # Clear the screen
        draw_lines()  # Draw grid lines
        draw_figures()  # Draw X's and O's

        # Display message if the game is over
        if game_over:
            if check_win('X'):
                display_message("You Win!")
            elif check_win('O'):
                display_message("You Lose!")
            else:
                display_message("Draw!")

        pygame.display.update()

if __name__ == "__main__":
    main()