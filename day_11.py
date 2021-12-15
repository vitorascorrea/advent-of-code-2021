def step(lines):
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      lines[i][j] += 1

  return lines


def has_flashable_octopus(lines):
  for row in lines:
    for c in row:
      if c > 9:
        return True

  return False


def count_flashes_and_update(lines):
  flashes = 0
  already_flashed = []

  while has_flashable_octopus(lines):
    for i in range(len(lines)):
      for j in range(len(lines[i])):
        if lines[i][j] > 9:
          flashes += 1
          lines[i][j] = 0
          already_flashed.append((i, j))

          if i > 0 and (i - 1, j) not in already_flashed:
            lines[i - 1][j] += 1
          if i < len(lines) - 1 and (i + 1, j) not in already_flashed:
            lines[i + 1][j] += 1
          if j > 0 and (i, j - 1) not in already_flashed:
            lines[i][j - 1] += 1
          if j < len(lines[i]) - 1 and (i, j + 1) not in already_flashed:
            lines[i][j + 1] += 1

          # diagonals
          if i > 0 and j > 0 and (i - 1, j - 1) not in already_flashed:
            lines[i - 1][j - 1] += 1
          if i > 0 and j < len(lines[i]) - 1 and (i - 1, j + 1) not in already_flashed:
            lines[i - 1][j + 1] += 1
          if i < len(lines) - 1 and j > 0 and (i + 1, j - 1) not in already_flashed:
            lines[i + 1][j - 1] += 1
          if i < len(lines) - 1 and j < len(lines[i]) - 1 and (i + 1, j + 1) not in already_flashed:
            lines[i + 1][j + 1] += 1

  return flashes


def solve_first(lines):
  int_lines = [list(map(int, x)) for x in lines]
  flashes = 0

  for _ in range(100):
    step(int_lines)
    flashes += count_flashes_and_update(int_lines)

  return flashes


def solve_second(lines):
  int_lines = [list(map(int, x)) for x in lines]
  flashes = 0
  step_index = 0

  while flashes != len(lines) * len(lines[0]):
    step_index += 1
    step(int_lines)
    flashes = count_flashes_and_update(int_lines)

  return step_index


if __name__ == '__main__':
  f = open('inputs/day_11_input.txt')
  lines = f.read().splitlines()

  print(solve_first(lines))
  print(solve_second(lines))
