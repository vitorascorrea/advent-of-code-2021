def find_low_points(int_lines):
  low_points = []

  for i in range(len(int_lines)):
    for j in range(len(int_lines[i])):
      number = int_lines[i][j]
      left = True
      right = True
      up = True
      down = True

      if i > 0:
        left = number < int_lines[i - 1][j]
      if i < len(int_lines) - 1:
        right = number < int_lines[i + 1][j]
      if j > 0:
        up = number < int_lines[i][j - 1]
      if j < len(int_lines[i]) - 1:
        down = number < int_lines[i][j + 1]

      if left and right and up and down:
        low_points.append({'number': number, 'coordinates': (i, j)})

  return low_points


def find_basin_from_point(current_coordinates, int_lines, basin_points, coordinates):
  i, j = current_coordinates
  current_number = int_lines[i][j]

  if current_number == 9:
    return

  if i > 0 and int_lines[i - 1][j] > current_number and int_lines[i - 1][j] < 9 and (i - 1, j) not in coordinates:
    basin_points.append(int_lines[i - 1][j])
    coordinates.append((i - 1, j))
    find_basin_from_point((i - 1, j), int_lines, basin_points, coordinates)

  if i < len(int_lines) - 1 and int_lines[i + 1][j] > current_number and int_lines[i + 1][j] < 9 and (i + 1, j) not in coordinates:
    basin_points.append(int_lines[i + 1][j])
    coordinates.append((i + 1, j))
    find_basin_from_point((i + 1, j), int_lines, basin_points, coordinates)

  if j > 0 and int_lines[i][j - 1] > current_number and int_lines[i][j - 1] < 9 and (i, j - 1) not in coordinates:
    basin_points.append(int_lines[i][j - 1])
    coordinates.append((i, j - 1))
    find_basin_from_point((i, j - 1), int_lines, basin_points, coordinates)

  if j < len(int_lines[i]) - 1 and int_lines[i][j + 1] > current_number and int_lines[i][j + 1] < 9 and (i, j + 1) not in coordinates:
    basin_points.append(int_lines[i][j + 1])
    coordinates.append((i, j + 1))
    find_basin_from_point((i, j + 1), int_lines, basin_points, coordinates)


def solve_first(lines):
  int_lines = [list(map(int, x)) for x in lines]
  return sum([x['number'] + 1 for x in find_low_points(int_lines)])


def solve_second(lines):
  int_lines = [list(map(int, x)) for x in lines]
  low_points = find_low_points(int_lines)

  basins_lens = []

  for point in low_points:
    basin_points = [point['number']]
    coordinates = [point['coordinates']]
    find_basin_from_point(point['coordinates'], int_lines, basin_points, coordinates)
    basins_lens.append(len(basin_points))

  top_three = sorted(basins_lens)[-3:]

  return top_three[0] * top_three[1] * top_three[2]


if __name__ == '__main__':
  f = open('inputs/day_9_input.txt')
  lines = f.read().splitlines()

  print(solve_first(lines))
  print(solve_second(lines))
