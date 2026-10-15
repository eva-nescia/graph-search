        

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        
class StackFrontier:
    def __init__(self):
        self.frontier = []
        
    def add_node(self,node):
        self.frontier.append(node)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self, state_name):
        for node in self.frontier:
            if node.state == state_name:
                return True
            return False
        
    def remove(self):
        if not self.empty():
            return self.frontier.pop()
            
class QueueFrontier(StackFrontier):
    def remove(self):
        if not self.empty():
            return self.frontier.pop(0)
            
def graph_search(graph, start, goal, frontier):
    start_node = Node(state=start, parent=None)
    frontier.add_node(start_node)
    
    explored = set()
    explored_list = []
    
    while not frontier.empty():
        node = frontier.remove()
        
        if node.state == goal:
            path = []
            curr_node = node
            while curr_node is not None:
                path.append(curr_node.state)
                curr_node = curr_node.parent
            path.reverse( )
            return path, explored_list
        
        explored.add(node.state)
        explored_list.append(node.state)
        
        neigbours = sorted(graph.get(node.state, []))
        
        if isinstance(frontier, StackFrontier) and not isinstance(frontier, QueueFrontier):
            neigbours_to_add = reversed(neigbours)
        else:
            neigbours_to_add = neigbours
            
        for neighbour in neigbours_to_add:
            if not frontier.contains_state(neigbours) and neighbour not in explored:
                child = Node(state=neighbour, parent=node)
                frontier.add_node(child)

def main():
    road_dictionary = {
        "Jalan Yos Sudarso": ["Jalan Satando", "Jalan Andalas"],
        "Jalan Satando": ["Jalan Nusantara"],
        "Jalan Nusantara": ["Jalan Riburane"],
        "Jalan Riburane": ["Jalan Ahmad Yani"],
        "Jalan Ahmad Yani": ["Jalan Kajaolalido"],
        "Jalan Kajaolalido": ["Jalan Botolempangan"],
        "Jalan Botolempangan": ["Jalan Arief Rate"],
        "Jalan Arief Rate": ["Jalan Haji Bau"],
        "Jalan Haji Bau": ["Jalan Metro Tanjung Bunga"],
        "Jalan Metro Tanjung Bunga": ["Universitas Ciputra Makassar"],
        "Jalan Andalas": ["Jalan Bawakaraeng"],
        "Jalan Bawakaraeng": ["Jalan R.A Kartini"],
        "Jalan R.A Kartini": ["Jalan Kajaolalido"],
        "Universitas Ciputra Makassar": [],
    }
    
    bfs_path, bfs_explored = graph_search(road_dictionary, "Jalan Yos Sudarso", "Universitas Ciputra Makassar", QueueFrontier())
    dfs_path, dfs_explored = graph_search(road_dictionary, "Jalan Yos Sudarso", "Universitas Ciputra Makassar", StackFrontier())
    print("========== BFS RESULTS ==========")
    print("BFS Path      :", bfs_path)
    print("BFS Explored  :", bfs_explored)
    print("========== DFS RESULTS ==========")
    print("DFS Path      :", dfs_path)
    print("DFS Explored  :", dfs_explored)
    
main()