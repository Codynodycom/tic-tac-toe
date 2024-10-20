from field_module import get_field
from constants import (
    EMPTY_CELL, # *
    ABC, # abc
    ABC_NUMS, # 123
    LETTER_TO_INDEX, # словарь с ключами-буквами и индексами-значениями
    WIN_LINE_O, # ['x', 'x', 'x']
    WIN_LINE_X, # ['o', 'o', 'o']
)

# Проверяет, правильно ли введен ход игрока
def check_turn(player_turn: str):
    # Если длина player_turn не 2, там могут быть варианты: 1, ккк..., пробел или пустота
    if len(player_turn) != 2:
        return False
    # Первый символ должен быть цифрой
    elif player_turn[0] not in ABC_NUMS:
        return False
    # Второй символ должен быть буквой
    elif player_turn[1:] not in ABC:
        return False
    
    return True

# Проверяет пустая ли ячейка на игровом поле
def is_cell_free(player_turn: str): # 1a | 2b | 3c
    row = int(player_turn[0]) - 1
    col = LETTER_TO_INDEX[player_turn[1]]
    field = get_field() # [ ['*','*','*'], ['*','o','*'], ['x','*','*'] ]

    if field[row][col] == EMPTY_CELL:
        return True

    return False

# Проверяет победителя
def chech_win(player_x: str, player_o: str, field: list):
    ...
