class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, val):
        n = Node(val)
        if self.head == None:
            self.head = self.tail = n
            return
        self.tail.next = n
        n.prev = self.tail
        self.tail = n

    def delNode(self, pos, element=-1):
        if pos == "Beginning":
            self.head = self.head.next
            self.head.prev = None

        elif pos == "End":
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None

        else:
            temp = self.head
            while temp:
                if temp.val == element:
                    break
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def printt(self):
        if not self.head:
            print("Empty LL")
        temp = self.head
        while temp != None:
            if temp.prev:
                print(temp.prev.val, " <---", end=" ")
            else:
                print("None <---", end=" ")
            print(temp.val, end=" ")
            if temp.next:
                print("---> ", temp.next.val, end=" ")
            else:
                print("---> None", end=" ")
            temp = temp.next
            print()


ll = DoublyLL()

ll.addNode(10)
ll.addNode(20)
ll.addNode(30)
ll.addNode(40)
ll.addNode(50)
ll.addNode(60)
ll.addNode(70)


ll.delNode("End")
ll.delNode("Mid", 40)
ll.delNode("Mid", 20)

ll.printt()
