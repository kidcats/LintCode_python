class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLists( l1, l2):
        # write your code here
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        cur=ListNode(0)
        if l1.val<l2.val:
            cur=l1
            cur.next=mergeTwoLists(l1.next,l2)
        elif l1.val==l2.val:
            cur=l2
            cur.next=mergeTwoLists(l1.next,l2.next)
        else:
            cur=l2
            cur.next=mergeTwoLists(l1,l2.next)
            
        return cur
        


if __name__=='__main__':
    l1=ListNode(1,ListNode(3))
    l2=ListNode(2)
    a=mergeTwoLists(l1,l2)
    print(a.val)