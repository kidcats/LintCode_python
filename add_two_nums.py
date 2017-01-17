class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def addTwoNums(l1,l2):
    if l1 is None and l2 is None:
        return None
    head=ListNode(0)
    pret=head
    tem=0
    while True:
        if l1 is not None:
            tem+=l1.val
            l1=l1.next
        if l2 is not None:
            tem+=l2.val
            l2=l2.next

        head.val=tem%10
        tem=int(tem/10)

        if l1 is not None or l2 is not None or tem>0:
            head.next=ListNode(0)
            head=head.next
        else:
            break
    return pret

if __name__ =='__main__':
    l1=ListNode(1,ListNode(1,ListNode(1,ListNode(1))))
    l2=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))
    a=addTwoNums(l1,l2)
    print(a.val)
    