"""
Notes:
"""

"""
Problem:
A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the head node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        # Before iterating through a linked list, first check to make sure we have proper inputs.
        # If there is not a linked list, we will exit early and return none.
        if not head:
            return None
        # Track progress in the list with the current variable
        current = head
        # If there are nodes after current, we will delete duplicates.  We do this by checking if the codes next data is equal to the current data.
        while current.next:
            if current.next.data == current.data:
                # If equal, we will point our current node to the node two away
                current.next = current.next.next
            else:
                # If not equal, point to the next node
                current = current.next
        # When all the nodes have been checked, return the head
        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 