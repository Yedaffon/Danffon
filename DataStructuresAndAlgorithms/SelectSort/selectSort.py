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
from typing import List


# 选择排序:
def select_sort(slist: List):
    for i in range(len(slist)):
        min = i
        for j in range(i, len(slist)):
            if slist[j] < slist[min]:
                min = j
        slist[i], slist[min] = slist[min], slist[i]
    return slist


if __name__ == '__main__':
    bbl = [1, 2, 3, 4, 5, 6, 1, 2, 3]
    select_sort(bbl)
    print(bbl)
