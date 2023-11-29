class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def addChild(self,node):
        if node > self.value and not self.right:
            self.right = BST(node)
        elif node <= self.value and not self.left:
            self.left = BST(node)
        elif node > self.value:
            self.right.addChild(node)
        else:
            self.left.addChild(node)

    def display(self):
        #Inorder Traversal - Prints in sorted order (Left, print Node, Right) Application - Sorting  
        if self.left:
            self.left.display()
        print(self.value)
        if self.right:
            self.right.display()

        #Pre-order Traversal - (Prints Node, Left, Right) Application - Making a copy of something, Serialization, Evaluating Math expressions
        # print(self.value)
        # if self.left:
        #     self.left.display()
        # if self.right:
        #     self.right.display()

        #Post-order Traversal - (Left, Right,Prints Node) Application - Deletion of binary Tree, Bottom up calculation(height/diameter of tree etc.)
        # if self.left:
        #     self.left.display()
        # if self.right:
        #     self.right.display()
        # print(self.value)
        

root = int(input("Enter value of root node: "))
rootObj = BST(root)
while True:
    k = int(input("Do you want to enter a value (1/0): "))
    if not k:
        break
    nodeValue = int(input("Enter Value: "))
    rootObj.addChild(nodeValue)

rootObj.display()

