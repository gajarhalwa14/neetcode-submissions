class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return

        temp = head

        length = 0
        while temp:
            length += 1
            temp = temp.next

        tail = head
        prev = None
        for i in range(length):
            if i < length // 2:
                prev = tail
                tail = tail.next
            else:
                if i == length // 2:
                    if length %2 == 1:
                        prev = tail
                        tail = tail.next
                    prev.next = None
                nxt = tail.next
                tail.next = prev
                prev = tail
                if not nxt: break
                tail = nxt
        
        # temp_tail = tail
        # while temp_tail:
        #     print(temp_tail.val)
        #     temp_tail = temp_tail.next


        for i in range(length // 2):
            # print(i)
            head_nxt = head.next
            tail_nxt = tail.next

            head.next = tail
            tail.next = head_nxt
            if head_nxt:
                head = head_nxt
            tail = tail_nxt

        print(head.val)
        if head.next: print(head.next.val)
        if tail: print(tail.val)
        