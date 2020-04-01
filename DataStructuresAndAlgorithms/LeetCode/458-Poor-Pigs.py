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

# 假设有1000只水桶, 猪饮水中毒后会在15分钟内死亡, 你需要多少猪(x)就能在60分钟内找出"有毒"水桶?
# 这1000只水桶里有且仅有一只有毒的桶.

# 解析:
# 这道题并没有找到其数学原理. 按 x ** y 计算.

import math


class Solution:

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets, states))


if __name__ == '__main__':
    c = Solution()
    d = c.poorPigs(1000, 15, 60)
    print(d)
