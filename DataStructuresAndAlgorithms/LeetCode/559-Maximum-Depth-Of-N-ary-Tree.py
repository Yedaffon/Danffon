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

# N叉树的最大深度:


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif root.children is None:
            return 1
        else:
            height = [self.maxDepth(i) for i in root.children]
            return max(height) + 1


if __name__ == '__main__':
    node = Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6), Node(7)])])
    c = Solution()
    print(c.maxDepth(node))