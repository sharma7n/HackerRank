""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# Currently passes: 0, 4, 8, 9, 12

def check_binary_search_tree_(root):
    is_search = True
    if root.left:
        if root.left.data < root.data:
            is_search = check_binary_search_tree_(root.left)
        else:
            is_search = False
    if root.right:
        if root.right.data > root.data:
            is_search = check_binary_search_tree_(root.right)
        else:
            is_search = False
    return is_search