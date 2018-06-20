# Write code to remove duplicates from an unsorted linked list

# My solution was fairly close to the book's. 
# Runtime for removeDuplicates O(n)
# Runtime for noBufferRemove O(n^2) since we have to iterate through each time

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def appendToEnd(self, val):
        n = self
        while n.next != None:
            n = n.next
        n.next = Node(val)

def removeDuplicates(head):
    vals = []
    currentNode = head
    nextNode = head.next
    vals.append(currentNode.val)
    while nextNode != None:
        if nextNode.val not in vals:
            vals.append(nextNode.val)
            currentNode.next = nextNode
            currentNode = currentNode.next
        nextNode = nextNode.next
    currentNode.next = nextNode
        
def noBufferRemove(head):
    currentNode = head
    while currentNode != None:
        nextNode = currentNode.next
        prevNode = currentNode
        while nextNode != None:
            if nextNode.val != currentNode.val:
                prevNode.next = nextNode
                prevNode = prevNode.next
            nextNode = nextNode.next
        prevNode.next = nextNode
        currentNode = currentNode.next
        
            

if __name__ == "__main__":
    lst = input().split()
    linkedList = Node(lst[0])
    for i in range(1, len(lst)):
        linkedList.appendToEnd(lst[i])

    head = linkedList

    while head != None:
        print(head.val, end=' ')
        head = head.next

    print()

    head = linkedList

    noBufferRemove(head)

    while head != None:
        print(head.val, end=' ')
        head = head.next
