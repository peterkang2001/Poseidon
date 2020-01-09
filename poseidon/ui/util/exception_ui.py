# coding=utf-8

"""
@author:songmengyun
@file: exception_ui.py
@time: 2020/01/08

"""


class TooLongException(Exception):
    "this is user's Exception for check the length of name "
    def __init__(self,leng):
        self.leng = leng
    def __str__(self):
        print("字符长度是"+str(self.leng)+"，超过长度了")

class InitDriverError(Exception):
    '''this is user's Exception for check android init driver'''

    def __init__(self, ErrorInfo):
        self.errorinfo = ErrorInfo
        super().__init__(self)  # 初始化父类

    def __str__(self):
        return self.errorinfo

class KeyInvalidError(Exception):
    pass

