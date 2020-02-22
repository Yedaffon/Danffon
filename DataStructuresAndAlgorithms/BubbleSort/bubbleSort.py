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

# 冒泡排序.

import time


class Bubble(object):

    def __init__(self, elem):
        self.start = time.time()
        self.elem = elem
        self.lo = 1
        self.hi = len(elem)
        self.bubble_sort()
        elem = self.elem
        self.end = time.time()
        self.cost = self.end - self.start
        pass

    def bubble_sort(self):
        while self.lo < self.hi:
            self.hi = self.bubble()

    def bubble(self):
        last = 0
        while self.lo < self.hi:
            if self.elem[self.lo - 1] > self.elem[self.lo]:
                last = self.lo
                self.elem[self.lo], self.elem[self.lo - 1] = self.elem[self.lo - 1], self.elem[self.lo]
            self.lo += 1
        self.lo = 1
        return last

    def __str__(self):
        return "冒泡排序结果为: %s  耗时: %.4f ms" % (str(self.elem), self.cost * 1000)


if __name__ == '__main__':
    bbl = [1, 2, 3, 4, 5, 6, 1, 2, 3]
    yebubble = Bubble(bbl)
