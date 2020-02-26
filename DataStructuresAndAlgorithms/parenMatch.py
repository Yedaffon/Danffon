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

import re


def paren(parse):
    so = []
    parse = re.findall(r"\[|\]|\{|\}|\(|\)", parse)
    paren_dict = {"(": ")", "[": "]", "{": "}"}
    for i in parse:
        if i in "{[(":
            so.append(i)
        elif i in "}])":
            right = so.pop()
            if i != paren_dict[right]:
                return False
    if not so:
        return True


if __name__ == '__main__':
    parse = "[(])"
    s = paren(parse)
    print(s)
