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

import asyncio

num_list = [0] * 10


async def change_list(number):
    for i in range(len(number)):
        number[i] = i
        await asyncio.sleep(1)


async def get_num():
    for num in range(len(num_list)):
        # print(num_list[num])
        print(num_list)
        await asyncio.sleep(2)


async def main():
    task1 = asyncio.create_task(change_list(num_list))
    task2 = asyncio.create_task(get_num())
    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())