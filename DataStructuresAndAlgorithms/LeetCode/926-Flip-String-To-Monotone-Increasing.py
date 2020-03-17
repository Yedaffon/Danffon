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

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        zero, one = 0, 0
        for i in S:
            if i == "1":
                one += 1
            else:
                zero = min(zero+1, one)
        return zero


if __name__ == '__main__':
    c = Solution()
    print(c.minFlipsMonoIncr("11110001"))
