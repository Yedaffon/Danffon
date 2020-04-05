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

from typing import Callable
import threading


class ZeroEvenOdd(object):

    def __init__(self, n):
        self.n = n + 1
        self.Zero = threading.Semaphore(1)
        self.Even = threading.Semaphore(0)
        self.Odd = threading.Semaphore(0)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            self.Zero.acquire()
            printNumber(0)
            if i % 2 == 1: self.Odd.release()
            else: self.Even.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            if i % 2 == 0:
                self.Even.acquire()
                printNumber(i)
                self.Zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            if i % 2 == 1:
                self.Odd.acquire()
                printNumber(i)
                self.Zero.release()


class Number(object):

    def __init__(self, n):
        self.n = n
        print(self.n, end="")


if __name__ == '__main__':
    c = ZeroEvenOdd(2)
    thread0 = threading.Thread(target=c.zero, args=(Number,))
    thread1 = threading.Thread(target=c.odd, args=(Number,))
    thread2 = threading.Thread(target=c.even, args=(Number,))
    thread0.start()
    thread1.start()
    thread2.start()
