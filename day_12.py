def build_graph(lines):
  graph = {}

  for line in lines:
    splitted = line.split('-')
    if not splitted[0] in graph:
      graph[splitted[0]] = []
    if not splitted[1] in graph:
      graph[splitted[1]] = []

    if splitted[0] != 'end':
      graph[splitted[0]].append(splitted[1])
    if splitted[1] != 'end':
      graph[splitted[1]].append(splitted[0])

  return graph

# watch out, ugly code ahead
def dfs(start_node, end_node, graph, visited, path, paths, visit_fn):
  if not start_node in visited:
    visited[start_node] = False

  visited[start_node] = True
  path.append(start_node)

  if start_node == end_node:
    paths.append(path[:])
  else:
    for node in graph[start_node]:
      if not node in visited:
        visited[node] = False

      if visited[node] == True and node.islower() and node != 'start' and node != 'end':
        lower_path = [x for x in path if x.islower()]
        set_path = set(lower_path)

        # no duplicate in this path yet
        if len(lower_path) == len(set_path):
          dfs(node, end_node, graph, visited, path, paths, visit_fn)
      elif visited[node] == False or visit_fn(node):
        dfs(node, end_node, graph, visited, path, paths, visit_fn)

  path.pop()
  if start_node.islower() and start_node != 'start' and start_node != 'end' and start_node in path:
    pass
  else:
    visited[start_node] = False


def solve_first(graph):
  path = []
  paths = []
  visited = {}

  visit_fn = lambda node: node.isupper()

  dfs('start', 'end', graph, visited, path, paths, visit_fn)

  return len(paths)


def solve_second(graph):
  path = []
  paths = []
  visited = {}

  visit_fn = lambda node: node.isupper()

  dfs('start', 'end', graph, visited, path, paths, visit_fn)

  return len(paths)


if __name__ == '__main__':
  f = open('inputs/day_12_input.txt')
  lines = f.read().splitlines()
  graph = build_graph(lines)

  # print(solve_first(graph))
  print(solve_second(graph))

