# `main.py`

### Этот файл отвечает за основной игровой процесс. Основные моменты:

- Запрашиваются ники игроков.
- Появляется возможность видеть таблицу лидеров до начала игры (`show_score()`).
- Игра обновляет таблицу результатов после завершения игры.

```python
# Меняет переменную с текущим игроком O --> X или наоборот
def change_player():
    ...
# START GAME
show_score()  # Выводим доску лидеров

print('\n' + 'НОВАЯ ИГРА!' + '\n')

nikname_1 = input(NICKNAME_INPUT.format(1)).capitalize()
nikname_2 = input(NICKNAME_INPUT.format(2)).capitalize()

player_name = nikname_1
player_value = 'x'

while True:
    ...
    # Проверка выйгрыша
    winner = chech_win(player_x=nikname_1.lower(), player_o=nikname_2.lower(), field=get_field())

    if winner is not None:
        show_field()
        print('\n' + winner)
        break

change_player()  # Смена игрока
```

# `constants.py`

### Этот файл содержит константы, используемые в игре. Например:

`WIN_LINE_X` и `WIN_LINE_O` для определения победных комбинаций.
`NICKNAME_INPUT` и `TURN_TEXT` для текстовых сообщений пользователю.

```python
WIN_LINE_X = ['x', 'x', 'x']
WIN_LINE_O = ['o', 'o', 'o']

NICKNAME_INPUT = 'Игрок {} введите никнейм: '
TURN_TEXT = '''Пример хода: 1b | 2c | 3a
Ходит игрок {} - {}:
>>>'''
```

# `file_manager.py`

### Этот модуль отвечает за работу с таблицей лидеров:

- Функции для отображения результатов (`show_score()`).
- Обновление результатов после победы (`update_score_file()`).

```python
def show_score():
    # Показать текущие результаты игроков
    ...
    
def update_score_file(player_name, result):
    # Обновить файл с результатами
    ...
```

# `gameplay.py`

### Этот модуль отвечает за игровую механику:

- Функция проверки правильности хода (`check_turn()`).
- Проверка, свободна ли клетка (`is_cell_free()`).
- Проверка победы (`chech_win()`).

```python
def check_turn(player_turn):
    ...

def is_cell_free(player_turn):
    ...

def chech_win(player_x, player_o, field):
    ...
```

# `field_module.py`

Работа с игровым полем. Функции для отображения поля и установки значений:

- `show_field()` для отображения текущего состояния поля.
- `set_cell_in_field()` для внесения хода игрока в поле.

```python
def show_field():
    ...

def set_cell_in_field(row, col, player):
    ...
```
