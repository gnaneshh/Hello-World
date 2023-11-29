class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

    def addChild(self):
        k = int(input("Do you want to enter right child of "+ str(self.val)+ " : (1/0) "))
        if k:
            rchild = int(input("Enter right child of "+ str(self.val)+ " : "))
            self.right = BinaryTree(rchild)
            self.right.addChild()
        m = int(input("Do you want to enter left child of "+ str(self.val)+ " : (1/0) "))
        if m:
            lchild = int(input("Enter left child of " + str(self.val) + " : "))
            self.left = BinaryTree(lchild)
            self.left.addChild()


    def display(self):
        print("Node Value: ", self.val)
        if self.right:
            self.right.display()
        if self.left:
            self.left.display()
        


root = int(input("Enter root: "))
rootObj = BinaryTree(root)
rootObj.addChild()
rootObj.display()
    



