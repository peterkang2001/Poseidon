# coding=utf-8

"""
@author:songmengyun
@file: test_allure2.py
@time: 2020/03/05

"""

import pytest

class TestCase2():

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_expected_failure(self):
        """this test is an xfail that will be marked as expected failure"""
        assert False

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_unexpected_pass(self):
        """this test is an xfail that will be marked as unexpected success"""
        assert True

    # 如果触发了条件 就跳过
    @pytest.mark.skipif("2+2!=5", reason="this test is skipped by a triggered condition in @pytest.mark.skipif")
    def test_skip_by_triggered_condition(self):
        pass



