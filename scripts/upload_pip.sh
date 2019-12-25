#!/usr/bin/env bash
# 第1步: 需要在上传pip包的计算机中编辑  ~/.pypirc
#[pypi]
#repository=https://pypi.python.org/pypi
#username=xxxx
#password=xxx

# 第2步 安装 pip install twine
# 第3步 上传
python setup.py check &&
twine register dist/Poseidon-test-0.0.2.tar.gz
twine upload --repository pypi dist/Poseidon-test-0.0.2.tar.gz

twine upload dist/Poseidon-test-0.0.2.tar.gz
