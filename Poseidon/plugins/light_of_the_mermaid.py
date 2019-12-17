"""
人鱼之光（TV未用，星矢重生手游设定绝招，发出紫红色光芒，对敌人造成念力伤害）
"""

from py._xmlgen import html
from datetime import datetime
import pytest
import logging
from pytest_testconfig import config as pyconfig
from Tetis.base.MonitorAlert import MonitorAlert
from Tetis.base.SendMail import SendMail


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    '''修改report.html中的results-table头部分'''
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    '''修改report.html中的results-table行部分'''
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

def pytest_html_results_table_html(report, data):
    """ Called after building results table additional HTML. """
    pass



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

def pytest_runtest_setup(item):
    import re
    _msg = str(item.function.__doc__)
    _msg = re.search('\w+', _msg).group()
    logging.info("执行用例{nodeid}:{desc}".format(nodeid=item.nodeid,
                                              desc=_msg.strip()))

def pytest_terminal_summary(terminalreporter):
    '''
    :param terminalreporter:
    :return: 1:自动发送测试报告 2:自动发送巡检报警
    '''
    xj = MonitorAlert()
    _section_report = pyconfig["sections"].get('report', None)
    json_report_dict = xj._read_json_file(pyconfig['logfile'].get('json'))
    html_path = pyconfig['logfile'].get('html')
    monitor = True if 'monitor' in pyconfig else False
    url = xj._get_xunjian_html_report_path(html_path, monitor) # 点击跳转的链接
    item_name = pyconfig['rootdir'].split('/')[-1]
    # metric = _section_report.get('metric', None)
    if 'receivers' in _section_report:
        # 发送测试报告
        receivers = _section_report['receivers']
        receivers = receivers.strip('[').strip(']').strip().split(',')
        header = "质量管理平台"

        subject = '%s自动化测试报告'%(item_name)
        send_mail = SendMail(receivers, header, subject, url)
        mail_msg = send_mail.html_report(subject, json_report_dict)
        send_mail.send_mail(mail_msg)

    # 发送巡检报警
    xj.send_wx_warning(url, json_report_dict, monitor, metric=item_name)
