"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    def detect_cycle(node, visited_nodes=None):
        # get or init visited nodes
        if not visited_nodes:
            visited_nodes = set()
            
        # if node has already been visited, cycle exists
        if node in visited_nodes:
            return True
            
        # otherwise, append node to set and continue traversing
        # if no more nodes, no cycles exist
        else:
            visited_nodes.add(node)
            if node.next:
                return detect_cycle(node.next, visited_nodes=visited_nodes)
            else:
                return False
    return detect_cycle(head, set())    
