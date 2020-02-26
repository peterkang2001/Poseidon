#!/usr/bin/env bash
pip uninstall Poseidon-test &&
echo "卸载完毕"
pip install /Users/songmengyun/automation/poseidon/dist/poseidon-*.tar.gz &&
echo "安装完毕"
pip show -f poseidon

#po-admin startproject mystest1


