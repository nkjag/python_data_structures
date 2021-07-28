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

            print (temp.data,end=" ")
            temp = temp.next

    def deletefromBegining(self):
        if self.length == 0:
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

    def reorderList(self):
        # step1 : find middle
        if not self.head: return []
        slow, fast = self.head, self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step2 : reverse the second the half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        # step3 : merge list
        head1, head2 = self.head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt


linkedlist = LinkedList()
linkedlist.insertAtBegining(1)
linkedlist.insertAtEnd(2)
linkedlist.insertAtEnd(3)
linkedlist.insertAtEnd(4)
linkedlist.printList()
linkedlist.reorderList()
linkedlist.printList()
#linkedlist.deletefromEnd()
#linkedlist.printList()
