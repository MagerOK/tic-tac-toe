from random import choice, randint

# Отображаем сетку 
def print_grid(grid):
        print()
        print('{}|{}|{}'.format(grid[0][0], grid[0][1], grid[0][2]),
               '-----',
              '{}|{}|{}'.format(grid[1][0], grid[1][1], grid[1][2]),
               '-----',
              '{}|{}|{}'.format(grid[2][0], grid[2][1], grid[2][2]), sep='\n', end='\n\n')

# Проверяем, если пользователь может походить в выбранную клетку
def is_valid_move(grid, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if grid[row][col] != ' ':
        return False
    return True

# Проверяем, если есть выигрышная позиция у одного из игроков
def has_won(grid, player):
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
def is_draw(grid):
    for row in grid:
        if ' ' in row:
            return False
    return True

# Главная функция, создаем вложенный список из пробелов и распределяем роли
def play_game():
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X' if randint(0, 1) == 0 else 'O'
    print('Вам выпали Крестики!' if human_player == 'X' else 'Вам выпали Нолики!')
    current_player = 'X'
    while True: 
        # Если текущий игрок - человек, то он вводит координаты. Если компьютер - выбираются случайные свободные
        if current_player == human_player:
            print_grid(grid)
            try:
                print()
                cells = list(map(int, input("Введите ряд и столбец от 1 до 3 через пробел. Например: 2 2\n").split()))
                if len(cells) != 2:
                    print('Введите 2 числа через пробел')
                    continue
                else:
                    row, col = [x - 1 for x in cells]
            except ValueError:
                print('Введите 2 числа через пробел')
        else:
            cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == ' ']
            row, col = choice(cells)
        # Проверяем может ли игрок походить, если да, то меняем ящейку " " на Х или О.
        # Потом проверяем если игрок победил или ничья.
        # Если человек походил, то текущий игрок меняется на компютера, в противном случае добиваемся правильных данных от человека
        if is_valid_move(grid, row, col):
            grid[row][col] = current_player
            if has_won(grid, current_player):
                print_grid(grid)
                print("Победили Крестики" if current_player == 'X' else 'Победили Нолики!')
                break
            elif is_draw(grid):
                print_grid(grid)
                print('Ничья!')
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта клетка занята, попробуйте снова")

play_game()