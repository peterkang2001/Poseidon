#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""
import click
from poseidon.bin.scripts.command import command_start


@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', default="mysite")
def startproject(name):
    """create test project by scaffold """
    command_start(name)



if __name__ == '__main__':
    cli()


