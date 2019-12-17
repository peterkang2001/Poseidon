#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""
# 目前使用的是mysqlclient,如果实际使用时安装发现困难时，可以考虑将它换成 pymysql
# import pymysql
# pymysql.install_as_MySQLdb()

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker



class SqlSession(object):
    _session = None

    def __init__(self, sqlalchemystr, echo=True):
        self.sqlalchemystr = sqlalchemystr
        self.echo = echo

    def __enter__(self):
        if self._session:
            return self._session

        engine = create_engine(self.sqlalchemystr, echo=self.echo)
        Session = sessionmaker(bind=engine)
        self._session = Session()
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            self._session.close()
            self._session = None