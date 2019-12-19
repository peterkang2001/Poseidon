#!/usr/bin/env bash
# 需要在上传pip包的计算机中边际  ~/.pypirc
# 设置如下用户名密码
#[pypi]
#repository=https://pypi.python.org/pypi
#username=xxxx
#password=xxx
python setup.py check &&
python setup.py sdist upload -r pypi
