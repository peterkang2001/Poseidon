#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""
import click
from poseidon.bin.scripts.command import command_start
import poseidon

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=poseidon.__version__)
def cli():
    """poseidon-admin：简单创建自动化脚本"""
    print('acddqwd')
    pass


@cli.command()
@click.argument('name', default="mysite")
def startproject(name):
    """创建测试脚本的脚手架命令 """
    command_start(project_name=name)


@cli.command()
@click.argument('type', default="docker")
@click.option('-w')
@click.option('--case')
def run(type, w, case):
    """在容器中运行脚本"""
    pass

if __name__ == '__main__':
    cli()


