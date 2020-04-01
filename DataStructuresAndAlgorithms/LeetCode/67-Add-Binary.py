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
    def addBinary(self, a: str, b: str) -> str:
        count = str(int(a) + int(b))
        count = list(map(int, count))

        for i in range(len(count)-1, -1, -1):
            if i > 0:
                if count[i] == 2:
                    count[i] = 0
                    count[i-1] += 1
                if count[i] == 3:
                    count[i] = 1
                    count[i - 1] += 1
            if i == 0:
                if count[i] == 2:
                    count.insert(0, 1)
                    count[1] = 0
                if count[i] == 3:
                    count.insert(0, 1)
                    count[1] = 1
        return "".join([str(i) for i in count])


# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         c = int(a,2) + int(b,2)
#         return bin(c)[2:]


if __name__ == '__main__':
    s = Solution()
    ans = s.addBinary("1111", "1111")
    print(ans)
