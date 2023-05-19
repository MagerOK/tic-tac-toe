from random import randint
from func import human_move, computer_move, check_game_status


def play_game():
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X' if randint(0, 1) == 0 else 'O'
    print('Вам выпали Крестики!' if human_player == 'X' else 'Вам выпали Нолики!')
    current_player = 'X'
    while True:
        if current_player == human_player:
            human_move(grid, human_player)
        else:
            computer_move(grid, current_player)
        if check_game_status(grid, current_player):
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()