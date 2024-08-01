# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        t=head
        i=0
        c=0
        while(t):
            if(c==i+1):
                l.append(c)
                c=0
                i+=1
            t=t.next
            c+=1
        l.append(c)
        t1=t=head
        i=0
        a=ListNode()
        while(t):
            if(l[i]%2==1):
                while(l[i]!=0):
                    t1=t
                    t=t.next
                    l[i]-=1
            else:
                if((i+1)%2==1):
                    t1=p
                p=None
                while(l[i]!=0):
                    n=t.next
                    t.next=p
                    p=t
                    t=n
                    l[i]-=1
                t1.next=p
                while(p.next):
                    p=p.next
                p.next=t
            i+=1
        return head