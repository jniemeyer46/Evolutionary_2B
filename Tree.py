# Tree Implementation

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    # Adds a root node if one doesn't exist, otherwise calls _add
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    # Add a node to the left or right if one doesnt exist, otherwise go to that node
    def _add(self, val, node):
        if(node.l is None):
            node.l = Node(val)
        elif(node.l is not None and node.r is None):
            node.r = Node(val)
        elif(node.l is not None and node.r is not None):
            self._add(val, node.l)
        else:
            self._add(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    # Start at the root
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)

    # Print the tree
    def _printTree(self, node):
        if(node is not None):
            print(str(node.v))
            self._printTree(node.l)
            self._printTree(node.r)
