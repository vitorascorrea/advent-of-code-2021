def solve_first(lines):
  increased = 0
  previous = None

  for line in lines:
    if previous and line > previous:
      increased += 1

    previous = line

  return increased

def solve_second(lines):
  increased = 0
  previous = None
  len_lines = len(lines)

  for i in range(3, len_lines + 1):
    if not previous:
      previous = lines[i - 1] + lines[i - 2] + lines[i - 3]
      continue

    current = lines[i - 1] + lines[i - 2] + lines[i - 3]

    if current > previous:
      increased += 1

    previous = current

  return increased


if __name__ == '__main__':
  f = open('inputs/day_1_input.txt')
  raw_input = f.read()

  lines = list(map(int, raw_input.splitlines()))

  print(solve_first(lines))
  print(solve_second(lines))


