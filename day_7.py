def solve_first(numbers):
  min_sum = float('inf')
  min_num = None

  for i in numbers:
    number_sum = 0

    for j in numbers:
      if i != j:
        number_sum += abs(i - j)

    if number_sum < min_sum:
      min_sum = number_sum
      min_num = i

  return min_num, min_sum


def solve_second(numbers):
  min_sum = float('inf')
  min_num = None

  for i in range(1, max(numbers) + 1):
    number_sum = 0

    for j in numbers:
      if i != j:
        number_sum += gauss_sum(i, j)

    if number_sum < min_sum:
      min_sum = number_sum
      min_num = i

  return min_num, min_sum


def gauss_sum(i, j):
  diff = abs(i - j)
  return diff * (diff + 1) // 2

if __name__ == '__main__':
  f = open('inputs/day_7_input.txt')
  numbers = list(map(int, f.read().split(',')))

  print(solve_first(numbers))
  print(solve_second(numbers))
