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

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")

# Link first Node to second node
list.headval.nextval = e2
# Link n Node to n+1 node
e2.nextval = e3
e3.nextval = e4

list.AtBegining("Sun")
list.listprint()