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

# 卡特兰数:


# 递归
def catalan_d(n):
    if n == 1:
        return 1
    n = n - 1
    return (4*n - 2) * catalan_d(n) / (n + 1)


# 循环
def catalan_x(n):
    def catalan(n):
        s1, g1 = 1, 1
        for i in range(n, 2 * n):
            s1 = s1 * i
        for g in range(0, n):
            g1 = g1 * g
        ans = s1 / g1
        return ans
    return catalan(n) / (n)


if __name__ == '__main__':
    ans = catalan_d(5)
    print(ans)
