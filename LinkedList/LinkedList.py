class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, pos, val, element=-1):
        n1 = Node(val)
        if pos == "Beginning":
            if self.head == None:
                self.head = self.tail = n1
                return
            n1.next = self.head
            self.head = n1
            return
        elif pos == "End":
            if self.tail == None:
                self.head = self.tail = n1
                return

            self.tail.next = n1
            self.tail = n1

        elif pos == "After":
            if not self.head:
                print("Empty LL")
                return
            temp = self.head
            while temp:
                if temp.val == element:
                    break
                temp = temp.next
            if not temp:
                print("No Element Found")
                return
            if temp == self.tail:
                temp.next = n1
                self.tail = n1
                return
            n1.next = temp.next
            temp.next = n1
            return

        elif pos == "Before":
            if not self.head:
                print("Empty LL")
                return
            temp = self.head
            if temp.val == element:
                n1.next = temp
                self.head = n1
                return

            while temp.next:
                if temp.next.val == element:
                    break
                temp = temp.next
            if not temp:
                print("No Element Found")
                return
            n1.next = temp.next
            temp.next = n1
            return

    def deleteNode(self, pos, element=-1):
        if pos == "Beginning":
            self.head = self.head.next
        elif pos == "End":
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        elif pos == "Mid":
            temp = self.head
            while temp.next:
                if temp.next.val == element:
                    break
                temp = temp.next
            temp.next = temp.next.next

    def print(self):
        if self.head == None:
            print("No elements buddy ")
            return
        print("Head --> ", self.head.val)
        print("Tail ---> ", self.tail.val)
        temp = self.head
        while temp:
            print(temp.val, "--->", end="  ")
            temp = temp.next
        print("END")


ll1 = LinkedList()
ll2 = LinkedList()
# ll1.addNode("End", 10)
# ll1.addNode("End", 5)
# ll1.addNode("After", -1, 10)
# ll1.addNode("Beginning", 10)
# ll1.addNode("End", 0)
# ll1.addNode("After", 18, 5)
# ll1.addNode("Before", 3, 18)
# ll1.addNode("Before", 2, 3)
# ll1.addNode("End", 12)
# ll1.addNode("Beginning", 20)
# ll1.addNode("Before", 19, 20)
# ll1.addNode("After", 13, 12)

# ll1.deleteNode("Beginning")
# ll1.deleteNode("End")
# ll1.deleteNode("End")
# ll1.deleteNode("Mid", 2)

ll1.addNode("Beginning", 4)
ll1.addNode("Beginning", 2)
ll1.addNode("Beginning", 1)


ll2.addNode("Beginning", 4)
ll2.addNode("Beginning", 3)
ll2.addNode("Beginning", 1)


def merge(list1, list2):
    head = tail = None

    while list1 and list2:
        if list1.val <= list2.val:
            n = Node(list1.val)
            if not head:
                head = tail = n
            else:
                tail.next = n
                tail = n
            list1 = list1.next

        else:
            n = Node(list2.val)
            if not head:
                head = tail = n
            else:
                tail.next = n
                tail = n
            list2 = list2.next

    while list1:
        n = Node(list1.val)
        if not head:
            head = tail = n
        else:
            tail.next = n
            tail = n
        list1 = list1.next

    while list2:
        n = Node(list2.val)
        if not head:
            head = tail = n
        else:
            tail.next = n
            tail = n
        list2 = list2.next

    if head == None:
        print("No elements buddy ")
        return
    print("Head --> ", head.val)
    print("Tail ---> ", tail.val)
    temp = head
    while temp:
        print(temp.val, "--->", end="  ")
        temp = temp.next
    print("END")


merge(ll1.head, ll2.head)
