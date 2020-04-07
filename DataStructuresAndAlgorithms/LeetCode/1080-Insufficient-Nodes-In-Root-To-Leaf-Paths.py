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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(root, limit):
            if root.left is None and root.right is None:
                if root.val < limit:
                    return None
                else:
                    return root
            if root.left:
                root.left = dfs(root.left, limit - root.val)
            if root.right:
                root.right = dfs(root.right, limit - root.val)
            if root.left or root.right:
                return root
            else:
                return None
        return dfs(root, limit)
