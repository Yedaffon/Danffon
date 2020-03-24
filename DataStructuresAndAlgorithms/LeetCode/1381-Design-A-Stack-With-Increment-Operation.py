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


class CustomStack(object):

    def __init__(self, maxSize: int):
        self.aim = []
        self.maxSize = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.aim.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        else:
            x = self.aim.pop()
            self.size -= 1
            return x

    def increment(self, k: int, val: int) -> None:
        num = min(k, self.size)
        for i in range(num):
            self.aim[i] += val
