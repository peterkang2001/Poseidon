#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-06
"""

import os
from pytest_testconfig import config as pyconfig

class Files:
    @staticmethod
    def del_allFiles(path):
        """
        删除指定目录下的所有文件
        :param path:  通过os.path.abspath转换成的string类型
        """
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                os.chdir(path)

                # list2 = os.listdir(path)
                # Files.del_allFiles(path_file)

    @staticmethod
    def del_allSubDir(path):
        """
        删除制定目录下的所有目录
        :param path:
        :return:
        """


    @staticmethod
    def get_root():
        """
        获取项目路径
        :return:
        """

        # _dir = os.path.dirname(__file__)
        # for i in range(2):
        #     _dir = os.path.dirname(_dir)
        # return _dir
        return pyconfig['rootdir']

    @staticmethod
    def clean_testlog():
        root = Files.get_root()
        # 日志目录
        testLog_path = os.path.join(root,'logs')
        Files.del_allFiles(testLog_path)


        pass

    def print_files(self,mesg):
        print("print_files.......{}".format(mesg))

    @staticmethod
    def print_files_static(mesg):
        print("print_files_static.......{}".format(mesg))