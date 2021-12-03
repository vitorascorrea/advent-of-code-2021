def solve_first(lines):
  horizontal = 0
  depth = 0

  for line in lines:
    direction, raw_intensity = line.split(' ')
    intensity = int(raw_intensity)

    if direction == 'forward':
      horizontal += intensity
    if direction == 'up':
      depth -= intensity
    if direction == 'down':
      depth += intensity

  return horizontal * depth


def solve_second(lines):
  horizontal = 0
  depth = 0
  aim = 0

  for line in lines:
    direction, raw_intensity = line.split(' ')
    intensity = int(raw_intensity)

    if direction == 'forward':
      horizontal += intensity
      depth += aim * intensity
    if direction == 'up':
      aim -= intensity
    if direction == 'down':
      aim += intensity

  return horizontal * depth

if __name__ == '__main__':
  f = open('inputs/day_2_input.txt')
  raw_input = f.read()

  lines = raw_input.splitlines()

  print(solve_first(lines))
  print(solve_second(lines))
