class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

'''
递归的思路是求两个数满足
'''
def rotateRight(head, k):
        # write your code here
        #指针走到倒数第K个位置处,形成环然后打断
        if head==None or head.next==None:
            return head
        pre=head
        end=head
        curr=head
        j=0
        i=0
        while end.next!=None:
            end=end.next
            j+=1
        kk=k%(j+1)
        end=head
        if kk==0:
            return pre 
        while end.next!=None:
            if i>=kk-1:
                curr=pre
                pre=pre.next
            end=end.next
            i+=1
        end.next=head
        curr.next=None
        return pre


if __name__=='__main__':
    l=ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))
    a=rotateRight(l,10)
    print(a.val)