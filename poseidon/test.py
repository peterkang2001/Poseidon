import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def cli():
    """poseido-admin：简单创建自动化脚本"""
    pass


@cli.command()
@click.argument('name', default='all', required=True)
# @click.option('--greeting', default='Hello', help='word to use for the greeting')
# @click.option('--caps', is_flag=True, help='uppercase the output')
def hellocmd(name):
    click.echo(
        click.style(
            'I am colored %s and bold' %
            name,
            fg='green',
            bold=True))


@cli.command()
@click.option('-t', default='a', required=True,
              type=click.Choice(['a', 'h']), prompt=True, help='检查磁盘空间,a表示所有空间，h表示空间大于50%')
def dfcmd(t):
    """
    检查磁盘空间 dfcmd
    :param t:
    :return:
    """
    click.echo(click.style('检查磁盘空间', fg='green', bold=True))


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.argument('x', type=int, required=True)
def square(x):
    """
    得到x平方 square x
    """
    click.echo(click.style('x= %s' % x, fg='green', bold=True))
    print(x * x)


if __name__ == '__main__':
    cli()
