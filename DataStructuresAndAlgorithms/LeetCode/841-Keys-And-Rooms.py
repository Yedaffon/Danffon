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

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = set()
        stack.add(0)
        while stack:
            key = stack.pop()
            for keys in rooms[key]:
                if seen[keys] is False:
                    seen[keys] = True
                    stack.add(keys)
        return all(seen)


if __name__ == '__main__':
    c = Solution()
    d = c.canVisitAllRooms([[1],[3],[3],[]])
