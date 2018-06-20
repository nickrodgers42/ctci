# Write a function to return the kth to last element in a linked list

# My solution was pretty much identical to the one in the book for the iterative version
# But they also had a recursive one, which was a little simpler, but there were a few gotchas

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def appendToEnd(self, val):
        n = self
        while n.next != None:
            n = n.next
        n.next = Node(val)

def kthToLast(k, head):
    kth = head
    toEnd = head
    num = k
    while num >= 0 and toEnd != None:
        num -= 1
        toEnd = toEnd.next
    while toEnd != None:
        kth = kth.next
        toEnd = toEnd.next
    return kth

if __name__ == "__main__":
    lst = input().split()
    linkedList = Node(lst[0])
    for i in range(1, len(lst)):
        linkedList.appendToEnd(lst[i])
    k = int(input())
    head = linkedList
    print(kthToLast(k, head).val)