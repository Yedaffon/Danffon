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

# Manacher算法

class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        t = "#"
        for i in range(size):
            t += s[i]
            t += "#"
        t_len = 2 * size + 1

        p = [0 for _ in range(t_len)]

        max_right = 0
        center = 0

        max_len = 1
        start = 1

        for i in range(t_len):
            if i < max_right:
                mirror = 2 * center - i
                p[i] = min(max_right - i, p[mirror])

            left = i - (1 + p[i])
            right = i + (1 + p[i])

            while left >= 0 and right < t_len and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1

            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i

            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2

        return s[start: start + max_len]
