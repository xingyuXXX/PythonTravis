#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author: XingyuZhou
@Date: 03.10.20 13:46
@Desc:
"""
from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self) -> None:
        self.x = 1
        self.y = 2
        self.calculator = Calculator(self.x, self.y)

    def test_add(self):
        assert self.calculator.add() == self.x + self.y, "add method doesnt work"

    def test_subtract(self):
        assert self.calculator.subtract() == self.x - self.y, "subtract method doesnt work"
