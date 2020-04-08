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

# 简单工厂模式: 感觉没有必要?


class Person(object):

    def love(self):
        raise NotImplementedError

    def sex(self):
        raise NotImplementedError


class YangDanFeng(Person):

    def love(self):
        print("Love somebody that he used to know!")

    def sex(self):
        print("Boy")


# 工厂模式:
class Role(object):

    def select(self, name):
        if name == "杨丹枫":
            return YangDanFeng()
        else:
            return "Not Created"


if __name__ == '__main__':
    role = Role()
    person = role.select("杨丹枫")
    person.love()
    person.sex()