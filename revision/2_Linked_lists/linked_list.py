class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next

    def to_list(self):
        output = []
        n = self.head
        while n != None:
            output.append(n.data)
            n = n.next
        return output

    def insert_at_beginning(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def insert_at_end(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = n

    def insert_vals_at_end(self, vals):
        for val in vals:
            self.insert_at_end(val)

    def __len__(self):
        l = 0
        n = self.head
        while n:
            l += 1
            n = n.next

        return l
