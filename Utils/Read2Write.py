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

# 装饰器: 从path中读取后, 使用function修改数据, 再存储到原地址.

import functools


def read_utf8(path):
    with open(path, "r", encoding="utf-8") as fr:
        data = [i for i in fr]
        return data


def write_utf8(path, data):
    with open(path, "w", encoding="utf-8") as fw:
        for i in data:
            fw.write(i)


def read2write(func):
    @functools.wraps(func)
    def wrapper(path):
        ori_path = path
        path = read_utf8(path)
        result = func(path)
        write_utf8(ori_path, path)
        return result
    return wrapper


# 示例
@read2write
def test(path):
    for i in range(len(path)):
        path[i] = "bbb" + "\t" + path[i]
    return path
