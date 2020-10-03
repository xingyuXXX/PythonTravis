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
    def test_add(self):
        x = 1
        y = 2
        calculator = Calculator.add(x, y)
        assert calculator.add() == x + y, "add method doesnt work"

    def test_subtract(self):
        x = 1
        y = 2
        calculator = Calculator.subtract(x, y)
        assert calculator.subtract() == x - y, "subtract method doesnt work"
