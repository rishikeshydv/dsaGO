#problem statement:
# Merge the two lists into one sorted list. Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeSortedLL(LL1: ListNode, LL2: ListNode) -> ListNode:
    dummy = ListNode()  # Dummy node to ease insertion
    sortedLL = dummy  # Pointer to track the current node in the merged list
    
    while LL1 and LL2:
        if LL1.val < LL2.val:
            sortedLL.next = LL1
            LL1 = LL1.next
        else:
            sortedLL.next = LL2
            LL2 = LL2.next
        sortedLL = sortedLL.next
    
    # Append the remaining nodes of LL1 or LL2, if any
    if LL1:
        sortedLL.next = LL1
    elif LL2:
        sortedLL.next = LL2
    
    return dummy.next  # Return the head of the merged list

    
#builing manual linked lists
_ll1 = ListNode(1,ListNode(3,ListNode(5)))
_ll2 = ListNode(2,ListNode(4,ListNode(6)))

print(mergeSortedLL(_ll1,_ll2))


