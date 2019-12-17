#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""
import click
from Poseidon.bin.scripts.command import start


@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def startproject(name):
    """create test project by scaffold """
    start(name)




if __name__ == '__main__':
    startproject()


