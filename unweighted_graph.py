class Node:
   def __init__(self, data):
      Graph.node_count += 1
      self.data = data

   def __del__(self):
      Graph.node_count -= 1

   def __repr__(self):
      return f"{self.data}"

class Edge:
   def __init__(self, node_a, node_b):
      self.connections = [node_a, node_b]
      Graph.edge_count += 2

   def __del__(self):
      Graph.edge_count -= 1

class Graph:
   node_count = 0
   edge_count = 0

   def __init__(self):
      self.node_list = []
      self.edge_list = []
      self.adjacency = {}

   def add_node(self, data):
      node = Node(data)
      self.node_list.append(node)
      self.adjacency[node] = []
      return node

   def add_edge(self, node_a, node_b):
      edge = Edge(node_a, node_b)
      self.edge_list.append(edge)
      self.adjacency[node_a].append(node_b)
      self.adjacency[node_b].append(node_a)
      return edge

   def bfs(self, node_a, node_b):
      visited = []
      queue = []
      predecessors = {}

      visited.append(node_a)
      queue.append(node_a)

      while queue:
         evaluated_node = queue.pop(0)
         #print(evaluated_node.data, end = " ")

         for adjacent_node in self.adjacency[evaluated_node]:
           if adjacent_node not in visited:
               visited.append(adjacent_node)
               queue.append(adjacent_node)
               predecessors[adjacent_node] = evaluated_node

               if adjacent_node is node_b:
                  reverse_path = [adjacent_node]
                  while reverse_path[-1] is not node_a:
                     reverse_path.append(predecessors[reverse_path[-1]])

                  reverse_path.reverse()
                  return reverse_path


      return None

graph = Graph()
node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
node4 = graph.add_node(4)

graph.add_edge(node1, node3)
graph.add_edge(node3, node2)
graph.add_edge(node2, node4)

print(graph.bfs(node1, node4))
