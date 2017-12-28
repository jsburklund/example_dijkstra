import numpy as np

class Node:
  def __init__(self, x, y):
    self.neighbors = []
    self.x = x
    self.y = y
    self.curr_cost = float("inf")
    self.travel_cost = 1
    self.previous = None

  def __str__(self):
    return "Point: "+str(self.x)+", "+str(self.y)

if __name__ == "__main__":
  xx, yy = np.meshgrid(range(-2,3), range(-2,3))
  my_grid_list = list(zip(xx.flatten(), yy.flatten()))
  my_node_list = [Node(point[0], point[1]) for point in my_grid_list]
  for node in my_node_list:
    print("Node: "+str(node))
    print("Neighbors: ")
    # Add the 8-connected neighbors
    for test_node in my_node_list:
      if test_node.x==node.x and (test_node.y==node.y+1 or test_node.y==node.y-1):
        node.neighbors.append(test_node)
      if test_node.y==node.y and (test_node.x==node.x+1 or test_node.x==node.x-1):
        node.neighbors.append(test_node)
      if (test_node.x==node.x-1 or test_node.x==node.x+1) and (test_node.y==node.y+1 or test_node.y==node.y-1):
        node.neighbors.append(test_node)

  # Make a dictionary for quick access by point
  my_node_dict = dict(zip(my_grid_list, my_node_list))

  # Set the start and end nodes
  start_node = my_node_dict[(0,-2)]
  end_node = my_node_dict[(0,2)]

  # Setup some basic obstacles
  my_node_dict[(0,0)].travel_cost = float("inf")
  my_node_dict[(1,0)].travel_cost = float("inf")

  # Setup the unevaluated and evaluated lists
  unevaluated = my_node_list[:] # Make a copy
  evaluated = []
  my_node_dict[(start_node.x, start_node.y)].curr_cost = 0

  while len(unevaluated) > 0:
    min_node = min(unevaluated, key=lambda x: x.curr_cost)
    my_cost = min_node.curr_cost
    my_node = min_node
    for neighbor in my_node.neighbors:
      neighbor_node = neighbor
      neighbor_cost = neighbor.travel_cost
      if neighbor_node.curr_cost > my_cost + neighbor_cost:
        neighbor_node.curr_cost = my_cost+neighbor_cost
        neighbor.previous = my_node
    # MOve this node to the evaluated list
    unevaluated.remove(min_node)
    evaluated.append(min_node)

  # Now that all of the nodes have been evaluated, unwind the stack
  curr_node = my_node_dict[(end_node.x,end_node.y)]  # Start at the end
  path = []
  while curr_node != None:
    path.append(curr_node)
    curr_node = curr_node.previous

  # Get the order from start to end
  path.reverse()
  path_str = "Path: "
  for item in path:
    path_str+= str((item.x, item.y))  +", "
  print(path_str)
     
