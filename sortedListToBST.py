class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    
def sortedListToBST(head):
    res=kst(head)
    return res
    
def kst(head):
        
    if head is None:
        return head
    if head.next is None:
        return TreeNode(head.val)
    curr=head
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    end=head
    while end is not None and end.next is not None:
        end=end.next.next
        pre=pre.next
        
    tem=pre.next
    root=TreeNode(tem.val)
    pre.next=None
        
    root.left=kst(curr)
    root.right=kst(tem.next)
        
    return root


if __name__=='__main__':
    l=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    a=sortedListToBST(l)
    print(a.val)