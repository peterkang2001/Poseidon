# coding=utf-8

"""
@author:songmengyun
@file: search_page.py
@time: 2020/01/07

"""

from poseidon.ui.mobile.android.base_page import BasePage

import time

class Search_Page(BasePage):

    add_button_my=("com.juyang.mall:id/rb_Mine")         #点击我的
    clear_content=("com.juyang.mall:id/edit_Tel")        #清空
    input_username=("com.juyang.mall:id/edit_Tel")       #输入账户
    input_password=("com.juyang.mall:id/edit_Pwd")       #输入密码
    click_login_button=("com.juyang.mall:id/tv_Login")   #点击登陆按钮
    login_result_page_text=(u"商城")                      #验证返回商城首页

    def click_my_button(self):
        '''封装点击我的方法'''
        self.by_id(self.add_button_my).click()
        time.sleep(5)

    def clear_login_content(self):
        '''封装情空方法'''
        self.by_id(self.clear_content).clear()

    def input_text_username(self,username):
        '''封装输入用户名方法'''
        self.by_id(self.input_username).send_keys(username)
        time.sleep(3)

    def input_text_password(self,password):
        '''封装输入密码方法'''
        self.by_id(self.input_password).send_keys(password)

    def click_loginbtn(self):
        '''封装点击登陆方法'''
        self.by_id(self.click_login_button).click()
        time.sleep(5)

    def get_finish_button_text(self):
        '''登陆成功后获取首页商城信息'''
        return self.by_name(self.login_result_page_text).text

    def login_airen_appproject(self,user,passwd):
        '''登陆流程封装'''
        self.click_my_button()
        self.clear_login_content()
        self.input_text_username(user)
        self.input_text_password(passwd)
        self.click_loginbtn()
