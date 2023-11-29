class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, val):
        n = Node(val)
        if self.head == None:
            self.head = self.tail = n
            return

        self.tail.next = n
        self.tail = n
        n.next = self.head

    def display(self):
        if self.head == self.tail:
            print(self.head.val)
            return
        print(self.head.val, self.tail.val)
        temp = self.head
        while temp.next != self.head:
            print(temp.val, end=" ")
            temp = temp.next
        print(temp.val, temp.next.val, temp.next.next.val)


ll = CircularLL()
ll.addNode(10)
ll.addNode(20)
ll.addNode(1)
ll.addNode(2)
ll.addNode(0)
ll.addNode(200)
ll.display()
