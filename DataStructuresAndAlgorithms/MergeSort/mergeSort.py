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

# 归并排序:


class Merge(object):

    def __init__(self, mlist):
        self.times = 0
        self.mlist = mlist
        self.merge_sort(0, len(mlist))
        mlist = self.mlist
        pass

    def merge_sort(self, lo: int, hi: int):
        if hi - lo < 2:
            return
        mi = (hi + lo) // 2
        self.merge_sort(lo, mi)
        self.merge_sort(mi, hi)
        self.merge(lo, mi, hi)
        pass

    def merge(self, lo: int, mi: int, hi: int):
        listA = self.mlist[lo: hi]
        lb = mi - lo
        lc = hi - mi
        listB = self.mlist[lo: mi]
        for i in range(lb):
            listB[i] = listA[i]
        listC = self.mlist[mi: hi]
        i, j, k = 0, 0, 0
        while (j < lb) or (k < lc):
            if j < lb and ((lc <= k) or (listB[j] <= listC[k])):
                self.mlist[lo + i] = listB[j]
                j += 1
                i += 1
            elif k < lc and ((lb <= j) or (listB[j] > listC[k])):
                self.mlist[lo + i] = listC[k]
                k += 1
                i += 1
            self.times += 1

        del listB


if __name__ == '__main__':
    bbl = [1, 2, 3, 4, 5, 6, 1, 2, 3]
    yebubble = Merge(bbl)
    print(bbl)



