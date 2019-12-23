#!/usr/bin/env bash
# 删除上次编译的缓存
rm -rf Poseidon_test.egg-info/
rm  -rf dist/
# 本地编译系统
python setup.py check &&
python setup.py sdist
