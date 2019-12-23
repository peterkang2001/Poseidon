#!/usr/bin/env bash
pip uninstall Poseidon-test &&
echo "卸载完毕"
pip install ~/Documents/Git/GitHub/Python/Poseidon/dist/Poseidon-test-0.0.2.tar.gz &&
echo "安装完毕"
pip list
po-admin startproject mystest1


