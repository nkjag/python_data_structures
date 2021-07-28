class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.next =next

class LinkedList(object):
    def __init__(self,node=None):
        self.length = 0
        self.head = node

    def insertAtBegining(self,data):
        newNode = Node()
        newNode.data =data

        if self.length == 0:
            self.head =newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1

    def insertAtEnd(self,data):
        newNode = Node()
        newNode.data = data

        current = self.head
        while current.next!=None:
            current= current.next
        current.next = newNode
        self.length +=1

    def printList(self):
        temp = self.head
        print("\n")
        while (temp):

            print (temp.data,end=" -->")
            temp = temp.next

    def deletefromBegining(self):
        if self.length ==0:
            return
        else:
            self.head = self.head.next
            self.length -=1

    def deletefromEnd(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentNode = self.head
            previous = self.head
            while currentNode.next!=None:
                previous = currentNode
                currentNode = currentNode.next
            previous.next  = None
            self.length -=1

linkedlist = LinkedList()
linkedlist.insertAtBegining("Nandakishor")
linkedlist.insertAtBegining("Nandakishor 123")
linkedlist.printList()
linkedlist.deletefromEnd()
linkedlist.printList()
