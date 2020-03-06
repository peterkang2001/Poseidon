# coding=utf-8

"""
@author:songmengyun
@file: test_allure4.py
@time: 2020/03/05

"""

import pytest
import logging

@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    logging.info('function scope setup')
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        # function_scope_step()
        logging.info('function scope teardown')
    request.addfinalizer(function_scope_finalizer)

@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    logging.info('class scope setup')
    def class_finalizer_fixture():
        # class_scope_step()
        logging.info('class scope teardown')
    request.addfinalizer(class_finalizer_fixture)

@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    logging.info('module scope setup')
    def module_finalizer_fixture():
        # module_scope_step()
        logging.info('module scope teardown')
    request.addfinalizer(module_finalizer_fixture)

@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    logging.info('session scope setup')
    def session_finalizer_fixture():
        # session_scope_step()
        logging.info('session scope teardown')
    request.addfinalizer(session_finalizer_fixture)


class TestClass(object):

    def test_with_scoped_finalizers(self,
                                    function_scope_fixture_with_finalizer,
                                    class_scope_fixture_with_finalizer,
                                    module_scope_fixture_with_finalizer,
                                    session_scope_fixture_with_finalizer):
        # step_inside_test_body()
        logging.info('step_inside_test_body')
