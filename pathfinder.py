# Implementation of the A* pathfinding algorithm
# F=G+H

class Node():

    def __init__(self, parent=None, position: tuple=None):
        self.parent = parent
        self.position = position

        self.f = self.g = self.h = 0

    # override equality
    def __eq__(self, other):
        return (self.position==other.position)

    # override toString
    def __str__(self):
        return (str(self.position))

# Parameters:
# maze = map
# start = starting position
# end = target position
def astar(maze, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    end_list = []

    open_list.append(start_node)

    # loop until an answer is reached
    # TODO add case where endpoint is not reachable
    while(len(open_list)>0):

        # retrieve first node
        current_node = open_list[0]
        current_index = 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        # pop element in open_list and move to close_list
        open_list.pop(current_index)
        end_list.append(current_node)

        # if target is found
        if (current_node == end_node):
            path = []
            current = current_node
            while (current is not None):
                path.append(current)
                current = current.parent
            return path[::-1]

        # generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

             # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # create new node to mark exploration of position
            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            # check if child in closed list
            for closed_child in end_list:
                if child == closed_child:
                    continue

            # Define the heristics of the algorithm
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)
    for item in path:
        print(item)


if __name__ == '__main__':
    main()
