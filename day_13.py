def build_grid(coordinates, biggest_x, biggest_y):
  grid = []

  for _ in range(biggest_y + 1):
    grid.append(['.' for _ in range(biggest_x + 1)])

  for y, x in coordinates:
    grid[x][y] = 'X'

  return grid


def flip_matrix(matrix, orientation):
  copy = matrix.copy()

  if orientation == 'v':
    copy.reverse()
  if orientation == 'h':
    for row in copy:
      row.reverse()

  return copy


def count_points(matrix):
  counter = 0

  for row in matrix:
    for c in row:
      if c == 'X':
        counter += 1

  return counter


def overlap_parts(part_a, part_b):
  bigger = part_a if len(part_a) >= len(part_b) else part_b
  smaller = part_a if len(part_a) < len(part_b) else part_b

  for i in range(len(smaller)):
    for j in range(len(smaller[i])):
      if smaller[i][j] == 'X':
        bigger[i][j] = 'X'

  return bigger


def solve_first_and_second(coordinates, instructions, biggest_x, biggest_y):
  grid = build_grid(coordinates, biggest_x, biggest_y)
  points_per_fold = {x: 0 for x in instructions}

  for instruction in instructions:
    axis, str_value = instruction.split('=')
    value = int(str_value)

    if axis == 'y':
      top = grid[:value].copy()
      bottom = grid[value + 1:].copy()
      flipped_bottom = flip_matrix(bottom, 'v')
      grid = overlap_parts(top, flipped_bottom)

    if axis == 'x':
      left = grid.copy()
      right = grid.copy()

      for i in range(len(left)):
        left[i] = left[i][:value]

      for i in range(len(right)):
        right[i] = right[i][value + 1:]

      flipped_right = flip_matrix(right, 'h')

      grid = overlap_parts(left, flipped_right)

    points_per_fold[instruction] = count_points(grid)

  return points_per_fold, grid


if __name__ == '__main__':
  f = open('inputs/day_13_input.txt')
  lines = f.read().splitlines()

  coordinates = []
  instructions = []
  biggest_x = float('-inf')
  biggest_y = float('-inf')

  reached_instructions = False

  for line in lines:
    if reached_instructions:
      instruction = line.split('fold along ')[1]
      instructions.append(instruction)
    elif line == '':
      reached_instructions = True
    else:
      x, y = tuple(map(int, line.split(',')))
      if x > biggest_x:
        biggest_x = x
      if y > biggest_y:
        biggest_y = y
      coordinates.append((x, y))

  points_per_fold, grid = solve_first_and_second(coordinates, instructions, biggest_x, biggest_y)
  print(points_per_fold)

  for row in grid:
    for c in row:
      print(c, end='')
    print()
