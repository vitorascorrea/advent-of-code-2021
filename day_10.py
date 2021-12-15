def solve_first(lines):
  sum_ = 0

  for line in lines:
    stack = []
    for c in line:
      if c in ['(', '[', '{', '<']:
        stack.append(c)
      elif c in [')', ']', '}', '>']:
        char = stack.pop()
        if c == ')' and char != '(':
          sum_ += 3
        if c == ']' and char != '[':
          sum_ += 57
        if c == '}' and char != '{':
          sum_ += 1197
        if c == '>' and char != '<':
          sum_ += 25137

  return sum_


def is_corrupted_line(line):
  stack = []

  for c in line:
    if c in ['(', '[', '{', '<']:
      stack.append(c)
    elif c in [')', ']', '}', '>']:
      char = stack.pop()
      if c == ')' and char != '(':
        return True
      if c == ']' and char != '[':
        return True
      if c == '}' and char != '{':
        return True
      if c == '>' and char != '<':
        return True

  return False


def find_oposite(char):
  if char == '(':
    return ')'
  if char == ')':
    return '('
  if char == '[':
    return ']'
  if char == ']':
    return '['
  if char == '{':
    return '}'
  if char == '}':
    return '{'
  if char == '>':
    return '<'
  if char == '<':
    return '>'


def find_closing_chars(line):
  stack = []

  for c in line:
    if c in ['(', '[', '{', '<']:
      stack.append(c)
    elif c in [')', ']', '}', '>']:
      stack.pop()

  return list(map(find_oposite, stack))


def solve_second(lines):
  scores = []

  for line in lines:
    if is_corrupted_line(line):
      continue
    else:
      closing_chars = find_closing_chars(line)
      closing_chars.reverse()

      score = 0

      for c in closing_chars:
        score *= 5
        if c == ')':
          score += 1
        if c == ']':
          score += 2
        if c == '}':
          score += 3
        if c == '>':
          score += 4

      scores.append(score)

  return sorted(scores)[(len(scores) - 1) // 2]


if __name__ == '__main__':
  f = open('inputs/day_10_input.txt')
  lines = f.read().splitlines()

  print(solve_first(lines))
  print(solve_second(lines))
