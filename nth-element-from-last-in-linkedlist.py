m=2
mylist=[10,200,3,40000,5]

# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
  
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
  
    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def mthElementFromLast(self,m):
        left = self.head
        right = self.head
        count = 1
        n = m
        while m > 0 and right:
            #print(right.data)
            right = right.next
            m -= 1
            count += 1

        if(count < n):
            print("NIL")
        else:
            while right:
                left=left.next
                right=right.next
            print(left.data)


ll = LinkedList()


for i in mylist:
    ll.insert(i)

#ll.printLL()
print("----")
ll.mthElementFromLast(m)
