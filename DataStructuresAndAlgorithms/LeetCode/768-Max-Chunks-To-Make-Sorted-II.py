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

# 单调栈:

from typing import List


class Solution(object):
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        max_num = -1
        for num in arr:
            if num >= max_num:
                stack.append(num)
                max_num = num
            else:
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(max_num)
        return len(stack)
