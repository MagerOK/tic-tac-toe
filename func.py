from random import choice

# Отображаем сетку 
def print_grid(grid: list[list[str]]) -> None:
        print()
        print('{}|{}|{}'.format(grid[0][0], grid[0][1], grid[0][2]),
               '-----',
              '{}|{}|{}'.format(grid[1][0], grid[1][1], grid[1][2]),
               '-----',
              '{}|{}|{}'.format(grid[2][0], grid[2][1], grid[2][2]), sep='\n', end='\n\n')

# Проверяем, если пользователь может походить в выбранную клетку
def is_valid_move(grid: list[list[str]], row: int, col: int) -> bool:
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if grid[row][col] != ' ':
        return False
    return True

# Проверяем, если есть выигрышная позиция у одного из игроков
def has_won(grid: list[list[str]], player: str) -> bool:
    for row in grid:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] == player:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True
    return False

# Проверяем на ничью        
def is_draw(grid: list[list[str]]) -> bool:
    for row in grid:
        if ' ' in row:
            return False
    return True

# Функция для хода человека
def human_move(grid: list[list[str]], human_player: str) -> None:
    while True:
        print_grid(grid)
        try:
            print()
            cells = list(map(int, input("Введите ряд и столбец от 1 до 3 через пробел. Например: 2 2\n").split()))
            if len(cells) != 2:
                print('Введите 2 числа через пробел')
                continue
            else:
                row, col = [x - 1 for x in cells]
                if is_valid_move(grid, row, col):
                    grid[row][col] = human_player
                    break
                else:
                    print("Эта клетка занята, попробуйте снова")
        except ValueError:
            print('Введите 2 числа через пробел')

# Функция для хода компьютера
def computer_move(grid: list[list[str]], computer_player: str) -> None:
    cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == ' ']
    row, col = choice(cells)
    grid[row][col] = computer_player

# Функция для проверки результатов игры
def check_game_status(grid: list[list[str]], current_player: str) -> bool:
    if has_won(grid, current_player):
        print_grid(grid)
        print("Победили Крестики" if current_player == 'X' else 'Победили Нолики!')
        return True
    elif is_draw(grid):
        print_grid(grid)
        print('Ничья!')
        return True
    return False
