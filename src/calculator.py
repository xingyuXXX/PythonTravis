#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author: XingyuZhou
@Date: 03.10.20 13:27
@Desc:
"""


class Calculator:

    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2


if __name__ == '__main__':
    calculator = Calculator(1, 2)
    print(calculator.add())
