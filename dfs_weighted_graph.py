import heapq

class Node:
   def __init__(self, data):
      Graph.node_count += 1
      self.data = data

   def __del__(self):
      Graph.node_count -= 1

   def __repr__(self):
      return f"{self.data}"

   def __lt__(self, other):
      return self.data < other.data

class Graph:
   node_count = 0

   def __init__(self):
      self.node_list = []
      self.adjacency = {}

   def add_node(self, data):
      node = Node(data)
      self.node_list.append(node)
      self.adjacency[node] = []
      return node

   def add_edge(self, node_a, node_b, weight):
      self.adjacency[node_a].append((node_b, weight))
      self.adjacency[node_b].append((node_a, weight))

   def internal_dfs(self, evaluated_node, visited):
      visited.append(evaluated_node)

      for neighbor_node, weight in self.adjacency[evaluated_node]:
         if neighbor_node not in visited:
            self.internal_dfs(neighbor_node, visited)

   def dijkstra_path_find(self, node_a, node_b):
      predecessors = {}
      distance_set = {}
      visited = []
      priority_queue = []
      path_found = False

      for node in self.node_list:
         distance_set[node] = float('inf')

      distance_set[node_a] = 0
      heapq.heappush(priority_queue, (0, node_a))

      while priority_queue:
         evaluated_distance, evaluated_node = heapq.heappop(priority_queue)

         if evaluated_node not in visited:
            visited.append(evaluated_node)

            for neighbor_node, weight in self.adjacency[evaluated_node]:
               neighbor_distance = evaluated_distance + weight
               if neighbor_distance < distance_set[neighbor_node]:
                  if neighbor_node is node_b:
                     path_found = True
                  distance_set[neighbor_node] = neighbor_distance
                  heapq.heappush(
                     priority_queue, (neighbor_distance, neighbor_node)
                  )
                  predecessors[neighbor_node] = evaluated_node

      if path_found is False:
         return Nene
      path = [node_b]
      while path[-1] is not node_a:
         path.append(predecessors[path[-1]])
      path.reverse()
      return path

   def dfs(self, initial_node):
      visited = []
      self.internal_dfs(initial_node, visited)
      return visited

graph = Graph()
node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
node4 = graph.add_node(4)
node5 = graph.add_node(5)

graph.add_edge(node1, node3, 29)
graph.add_edge(node3, node4, 50)
graph.add_edge(node3, node5, 2)
graph.add_edge(node4, node2, 20)

print(graph.dfs(node1))
