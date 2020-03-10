#!/usr/bin/env bash
# 删除上次编译的缓存
rm -rf .pytest_cache
rm -rf Poseidon_test.egg-info/
rm  -rf dist/
# 切换python虚拟环境
#source ~/Documents/py3_env/py3_other/bin/activate
# 本地编译系统
python setup.py check &&
python setup.py sdist


