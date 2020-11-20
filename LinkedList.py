class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    # Function to add new node at beggining
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Function to add new node at end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # Function to add node between nodes
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Wed")
e3 = Node("Thur")
e4 = Node("Fri")

# Link first Node to second node
list.headval.nextval = e2
# Link n Node to n+1 node
e2.nextval = e3
e3.nextval = e4

list.AtBegining("Sun")
list.AtEnd("Sat")
list.Inbetween(list.headval.nextval,"Tue")
list.listprint()
