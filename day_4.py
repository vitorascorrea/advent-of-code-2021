def parse_boards(lines):
  numbers = list(map(int, lines.pop(0).split(',')))
  boards = []

  current_board = []

  while len(lines) > 0:
    line = lines.pop(0)
    if not line and len(current_board) > 0:
      boards.append(current_board)
      current_board = []
    elif line:
      splitted = list(filter(lambda x: x != '', line.split(' ')))
      int_line = list(map(int, splitted))
      current_board.append(
        [{ 'value': x, 'marked': False } for x in int_line]
      )

  if len(current_board) > 0:
    boards.append(current_board)

  return numbers, boards


def check_board(board):
  for row in board:
    winning_row = len(list(filter(lambda c: c['marked'] == False, row))) == 0
    if winning_row:
      return True

  for i in range(len(board)):
    column = [row[i] for row in board]
    winning_column = len(list(filter(lambda c: c['marked'] == False, column))) == 0
    if winning_column:
      return True

  return False


def mark_number(number, board):
  for row in board:
    for cell in row:
      if cell['value'] == number:
        cell['marked'] = True
        return


def calc_unmarked_sum(board):
  total_sum = 0

  for row in board:
    for cell in row:
      if cell['marked'] == False:
        total_sum += cell['value']

  return total_sum


def solve_first_and_second(numbers, boards):
  winning_number = None
  winning_board = None
  board_winning_order_sums = []
  winning_boards = []

  for number in numbers:
    for i, board in enumerate(boards):
      if i in winning_boards:
        continue

      mark_number(number, board)

      if check_board(board):
        winning_board = board
        winning_number = number
        unmarked_sum = calc_unmarked_sum(winning_board)

        board_winning_order_sums.append(unmarked_sum * winning_number)
        winning_boards.append(i)
        continue

  return board_winning_order_sums


if __name__ == '__main__':
  f = open('inputs/day_4_input.txt')
  lines = f.read().splitlines()
  numbers, boards = parse_boards(lines.copy())
  board_winning_order_sums = solve_first_and_second(numbers, boards)

  # first
  print(board_winning_order_sums[0])
  # second
  print(board_winning_order_sums[-1])
