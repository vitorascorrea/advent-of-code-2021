import pprint


def solve_first_and_second(lines, board_size=1000):
  board = [[0] * board_size for i in range(board_size)]
  overlaps = 0

  for line in lines:
    splitted = line.split(' -> ')
    x1, y1 = list(map(int, splitted[0].split(',')))
    x2, y2 = list(map(int, splitted[1].split(',')))

    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        board[x1][y] += 1
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        board[x][y1] += 1
    else:
      x_range = None
      y_range = None

      if x1 < x2:
        x_range = list(range(x1, x2 + 1))
      else:
        x_range = list(range(x1, x2 - 1, -1))

      if y1 < y2:
        y_range = list(range(y1, y2 + 1))
      else:
        y_range = list(range(y1, y2 - 1, -1))

      for i in range(len(x_range)):
        x = x_range[i]
        y = y_range[i]
        board[x][y] += 1

  for row in board:
    for cell in row:
      if cell >= 2:
        overlaps += 1

  return overlaps


if __name__ == '__main__':
  f = open('inputs/day_5_input.txt')
  lines = f.read().splitlines()

  pprint.pprint(solve_first_and_second(lines, 1000))
