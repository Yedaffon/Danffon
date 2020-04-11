# coding=utf-8
# Copyright 2020 Yedaffon Author.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def num_list(x):
            if x.next:
                return x.val + num_list(x.next) * 10
            else:
                return x.val

        ans = num_list(l1) + num_list(l2)

        def turn2ListNode(num):
            if num == 0:
                return None
            lf = ListNode(num % 10)
            lf.next = turn2ListNode(num // 10)
            return lf

        if ans == 0:
            return l1
        else:
            return turn2ListNode(ans)


if __name__ == '__main__':
    c = ListNode(5)
    c.next = ListNode(6)
    c.next.next = ListNode(4)
    d = ListNode(2)
    d.next = ListNode(4)
    d.next.next = ListNode(3)
    l1 = c
    l2 = d
    m = Solution()
    print(m.addTwoNumbers(l1, l2))
