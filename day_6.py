def solve_second(original_numbers, target_days=256):
  numbers = original_numbers[:]
  dict_ = {x: 0 for x in range(9)}

  for number in numbers:
    dict_[number] += 1

  for _ in range(target_days):
    new_dict = {x: 0 for x in range(9)}

    for number in dict_:
      count = dict_[number]

      if number == 0:
        new_dict[6] += count
        new_dict[8] += count
      else:
        new_dict[number - 1] += count

    dict_ = new_dict

  return sum(dict_.values())


def solve_first(original_numbers, target_days=80):
  numbers = original_numbers[:]
  days = 1

  while days <= target_days:
    new_numbers = []

    for number in numbers:
      if number == 0:
        new_numbers.append(6)
        new_numbers.append(8)
      else:
        new_numbers.append(number - 1)

    numbers = new_numbers
    days += 1

  return len(numbers)


if __name__ == '__main__':
  f = open('inputs/day_6_input.txt')
  numbers = list(map(int, f.read().split(',')))

  print(solve_first(numbers))
  print(solve_second(numbers, 256))
