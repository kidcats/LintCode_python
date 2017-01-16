class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

'''
递归的思路是求两个数满足
'''
def sortList(head):
    # write your code here
    # 思路是先递归排序然后就是合并两个有序列表
    if head is None:
        return None
    if head.next is None:
        return head
    tem=head
    mid = getMid(head)
    right = sortList(mid.next)
    mid.next = None
    left = sortList(tem)

    return merge(left, right)


def getMid(head):
    if head is None:
        return None
    if head.next is None:
        return head
    pre = head
    end = head.next
    while end is not None and end.next is not None:
        pre = pre.next
        end = end.next.next
    return pre

def merge(left, right):
    tem = ListNode(0)
    curr = tem

    while left is not None and right is not None:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr=curr.next
    if left is None:
        curr.next = right
    else:
        curr.next = left
    return tem.next


if __name__=='__main__':
    l=ListNode(1,ListNode(-1))
    a=sortList(l)
    print(a.val)