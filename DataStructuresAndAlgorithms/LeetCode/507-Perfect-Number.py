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

# 完美数:
# 对于一个正整数, 如果它和除了它自身以外的所有正因子之和相等,我们称它为"完美数".
# 给定一个整数n, 如果他是完美数, 返回True, 否则返回False.

# 欧拉定理-欧几里得: 2^(p-1)*(2^p-1)  p:为质数


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        prime = [2, 3, 5, 7, 13, 17, 19, 31]
        perfect = [2 ** (p-1) * (2 ** p - 1) for p in prime]
        if num in perfect:
            return True
        else:
            return False


if __name__ == '__main__':
    c = Solution()
    d = c.checkPerfectNumber(33550336)
    print(d)
