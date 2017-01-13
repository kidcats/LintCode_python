class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
        # write your code here
    if head is None:
        return False
    if head.next is None:
        return False
    pre=head
    end=head
    while pre is not None and end is not None:
        if end.next is None:
            return False
        pre=pre.next
        end=end.next.next
        if pre==end:
            return True
    return False