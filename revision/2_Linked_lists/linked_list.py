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

    def insert_at_begining(self, d):
        n = Node(d)
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
