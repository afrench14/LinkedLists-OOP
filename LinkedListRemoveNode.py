class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def Atbegining(self, dataval_in):
        NewNode = Node(dataval_in)
        NewNode.next = self.headval
        self.headval = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.headval
        while (printval):
            print(printval.dataval),
            printval = printval.next


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()