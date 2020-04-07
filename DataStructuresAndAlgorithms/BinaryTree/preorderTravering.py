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


class BinaryTree(object):

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def traverse(self, node):
        if not node:
            return
        print(node.root)
        self.traverse(node.left)
        self.traverse(node.right)


if __name__ == '__main__':
    c = BinaryTree(0, BinaryTree(1), BinaryTree(2))
    c.traverse(c)
