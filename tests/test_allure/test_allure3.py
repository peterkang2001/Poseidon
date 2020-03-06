# coding=utf-8

"""
@author:songmengyun
@file: test_allure3.py
@time: 2020/03/05

"""

import pytest
import allure

@allure.step('用户登录')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
def login(user, pwd):
    '''用户名+密码登录'''
    print(user, pwd)

@allure.feature('购物车功能')  # 用feature说明产品需求，可以理解为JIRA中的Epic
class TestShoppingTrolley(object):
    '''测试购物车功能'''

    @allure.story('加入购物车')  # 用story说明用户场景，可以理解为JIRA中的Story
    @allure.severity('blocker')
    def test_add_shopping_trolley(self):
        '''商品加入购物车'''

        login('刘春明', '密码')  # 步骤1，调用“step函数

        with allure.step("浏览商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('笔记本', '商品1')  # attach可以打印一些附加信息
            allure.attach('手机', '商品2')
        with allure.step("点击商品"):  # 步骤3
            pass
        with allure.step("校验结果"):  # 步骤4
            allure.attach('添加购物车成功', '期望结果')
            allure.attach('添加购物车失败', '实际结果')
            assert 'success' == 'failed'

    @allure.story('修改购物车')
    @allure.severity('critical')
    def test_edit_shopping_trolley(self):
        '''修改购物车商品信息'''
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车中商品')
    @allure.severity('normal')
    def test_delete_shopping_trolley(self):
        '''删除购物车商品'''
        pass

@allure.feature('消费者功能')  # 用feature说明产品需求
@allure.severity('minor')
class TestCustom(object):

    @allure.story('新增消费者')  # 用story说明用户场景
    def test_add_custom(self):
        login('刘春明', '密码')  # 步骤1，调用“step函数
        with allure.step("浏览商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('笔记本', '商品1')  # attach可以打印一些附加信息
            allure.attach('手机', '商品2')
        with allure.step("点击商品"):  # 步骤3
            pass
        with allure.step("校验结果"):  # 步骤4
            allure.attach('添加购物车成功', '期望结果')
            allure.attach('添加购物车失败', '实际结果')
            assert 'success' == 'failed'

    @allure.story('修改消费者信息')
    def test_edit_shopping_trolley(self):
        pass

    @allure.story('删除购消费者')
    def test_delete_shopping_trolley(self):
        pass







