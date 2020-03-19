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


# 解码方法:
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1: i+1] == '10' or s[i-1: i+1] == '20':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if 10 < int(s[i-1: i+1]) <= 26:
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[-1]


if __name__ == '__main__':
    c = Solution()
    print(c.numDecodings("110"))