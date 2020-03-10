#!/usr/bin/env bash
pip uninstall Poseidon-test &&
echo "卸载完毕"
pip install /Users/songmengyun/automation/poseidon/dist/poseidon-*.tar.gz &&
echo "安装完毕"
pip show -f poseidon
echo "更新requirements.txt文件"
pip freeze -> requirements.txt
echo "更新完成"


#po-admin startproject mystest1


