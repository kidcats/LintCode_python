class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


#思路如下
#先将A链表的尾部和B链表的头部相衔接，制造出一个带环链表
#然后遍历找出带环链表的开始节点，并打断环即可
#
def getIntersectionNode(headA, headB):
    listA = []
    listB = []
    if headA is None or headB is None:
        return None
    while headA:
        listA.append(headA.val)
        headA = headA.next
    while headB:
        listB.append(headB.val)
        headB = headB.next

    if listA[-1] != listB[-1]:
        return None
    minlen = len(listA) if len(listA) < len(listB) else len(listB)

    for i in range(1,minlen +1):
        if listA[-i] != listB[-i]:
            return ListNode(listA[-i+1])
        if i == minlen:
            return ListNode(listA[-i])

if __name__ == '__main__':
    a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    b = ListNode(3,ListNode(4,ListNode(5)))
    ss = None
    ss = getIntersectionNode(a,b)
    print(ss)