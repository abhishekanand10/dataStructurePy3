class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def printlinkedlist(self):
        cur = self.head
        ll = []
        while cur.next is not None:
            cur = cur.next
            ll.append(cur.data)

        print(ll)


if __name__ == '__main__':
    a = LinkedList()

    a.append(1)
    a.append(2)
    a.append(3)
    a.printlinkedlist()
