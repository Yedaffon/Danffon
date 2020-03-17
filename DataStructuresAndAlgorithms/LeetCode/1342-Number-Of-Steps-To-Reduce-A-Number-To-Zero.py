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


#  将数字变成 0 的操作次数.
class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                step += 1
            else:
                num = num - 1
                step += 1
        return step


if __name__ == '__main__':
    c = Solution()
    print(c.numberOfSteps(14))