def count_freq(lines):
  freq = {x: {'0': 0, '1': 0} for x in range(len(lines[0]))}

  for line in lines:
    splitted = list(line)
    for i, c in enumerate(splitted):
      freq[i][c] += 1

  return freq

def solve_first(lines):
  freq = count_freq(lines)

  most_bin_num = ''
  least_bin_num = ''

  for key in freq:
    most_bin_num += '0' if freq[key]['0'] > freq[key]['1'] else '1'
    least_bin_num += '0' if freq[key]['0'] < freq[key]['1'] else '1'

  return int(most_bin_num, 2) * int(least_bin_num, 2)

def solve_second(lines):
  oxygen_rating = get_oxygen_rating(lines)
  co2_rating = get_co2_rating(lines)

  return int(oxygen_rating, 2) * int(co2_rating, 2)

def get_oxygen_rating(lines):
  filtered_lines = lines[:]
  bit_position = 0

  while True:
    freq = count_freq(filtered_lines)
    most_common_bit = '1' if freq[bit_position]['1'] >= freq[bit_position]['0'] else '0'
    filtered_lines = list(filter(lambda num: num[bit_position] == most_common_bit, filtered_lines))
    bit_position += 1

    if len(filtered_lines) == 1:
      return filtered_lines[0]

def get_co2_rating(lines):
  filtered_lines = lines[:]
  bit_position = 0

  while True:
    freq = count_freq(filtered_lines)
    least_common_bit = '1' if freq[bit_position]['1'] < freq[bit_position]['0'] else '0'
    filtered_lines = list(filter(lambda num: num[bit_position] == least_common_bit, filtered_lines))
    bit_position += 1

    if len(filtered_lines) == 1:
      return filtered_lines[0]

if __name__ == '__main__':
  f = open('day_3_input.txt')
  raw_input = f.read()

  lines = raw_input.splitlines()

  print(solve_first(lines))
  print(solve_second(lines))
