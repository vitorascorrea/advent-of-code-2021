def get_signal_and_output(line):
  splitted = line.split(' | ')
  signal_patterns = splitted[0].split(' ')
  output = splitted[1].split(' ')

  return signal_patterns, output


def solve_first(lines):
  unique_digits = 0

  for line in lines:
    _, output = get_signal_and_output(line)

    for o in output:
      if len(o) in [2, 3, 4, 7]:
        unique_digits += 1

  return unique_digits


def solve_second(lines):
  sum_ = 0

  for line in lines:
    number_mapping = {x: '_' for x in range(10)}
    signal_patterns, output = get_signal_and_output(line)

    for _ in range(2):
      for original_p in sorted(signal_patterns + output, key=lambda x: len(x)):
        p = ''.join(sorted(original_p))

        if len(p) == 2:
          number_mapping[1] = p
        elif len(p) == 3:
          number_mapping[7] = p
        elif len(p) == 4:
          number_mapping[4] = p
        elif len(p) == 5:
          diff_from_1_set = set(p) - set(number_mapping[1])
          diff_from_9_set = set(number_mapping[9]) - set(p)
          diff_from_6_set = set(number_mapping[6]) - set(p)

          diff_from_1 = len(diff_from_1_set)
          diff_from_9 = len(diff_from_9_set)
          diff_from_6 = len(diff_from_6_set)

          # could be 2 or 3 or 5
          # if it is 3, will have 3 remaining lines when we overlap with 1
          if diff_from_1 == 3:
            number_mapping[3] = p
          # if it is 5, it will have 1 remaining lines when we overlap with 9
          elif diff_from_9 == 1:
            number_mapping[5] = p
          # if it is 2, it will have 2 remaining lines when we overlap with 6
          elif diff_from_6 == 2:
            number_mapping[2] = p
        elif len(p) == 6:
          diff_from_4 = len(set(p) - set(number_mapping[4]))
          diff_from_7 = len(set(p) - set(number_mapping[7]))

          # could be 0 or 6 or 9
          # if it is 9, it will have 2 remaining lines when we overlap with 4
          if diff_from_4 == 2:
            number_mapping[9] = p
          # if it is 0, it will have 3 remaining lines when we overlap with 7
          elif diff_from_7 == 3:
            number_mapping[0] = p
          # if it is 6, it will have 4 remaining lines when we overlap with 7
          elif diff_from_7 == 4:
            number_mapping[6] = p
        elif len(p) == 7:
          number_mapping[8] = p

    inv_map = {v: k for k, v in number_mapping.items()}

    number = ''

    for o in output:
      sorted_o = ''.join(sorted(o))
      number += str(inv_map[sorted_o])

    sum_ += int(number)

  return sum_


if __name__ == '__main__':
  f = open('inputs/day_8_input.txt')
  lines = f.read().splitlines()

  # print(solve_first(lines))
  print(solve_second(lines))
