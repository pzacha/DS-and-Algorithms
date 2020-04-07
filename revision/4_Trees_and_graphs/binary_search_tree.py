class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
        if self:
            if data == self.data:
                print(str(data) + " found")
            elif data < self.data:
                if self.left: 
                    self.left.find(data)
                else:
                    print(str(data) + " not found")
                    return
            else:
                if self.right:
                    self.right.find(data)
                else:
                    print(str(data) + " not found")
                    return
        else:
            print(str(data) + " not found")
            return

    
    #Left --> Root --> Right
    def in_order_traversal(self):
        if self:
            if self.left: self.left.in_order_traversal()
            print(self.data)
            if self.right: self.right.in_order_traversal()

    #Root --> Left --> Right
    def pre_order_traversal(self):
        if self:
            print(self.data)
            if self.left: self.left.in_order_traversal()
            if self.right: self.right.in_order_traversal()

    #Left --> Right --> Root
    def post_order_traversal(self):
        if self:
            if self.left: self.left.in_order_traversal()
            if self.right: self.right.in_order_traversal()
            print(self.data)


root = Node(10)
[root.insert(i) for i in range(2,19,3)]

root.in_order_traversal()
print()
root.pre_order_traversal()
print()
root.post_order_traversal()

root.find(4)