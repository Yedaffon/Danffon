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
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]
        minimize_num = [(abs(x-i), i) for i in arr]
        mini_index = [i[1] for i in minimize_num]
        answer = mini_index[:k]
        answer.sort()
        return answer


if __name__ == '__main__':
    c = Solution()
    d = c.findClosestElements([0,1,2,2,2,3,6,8,8,9],5,9)
    print(d)







