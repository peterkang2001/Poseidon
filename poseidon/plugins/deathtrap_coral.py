import pytest
import logging
from pytest_testconfig import config as pyconfig
import poseidon.base.CommonBase as cb



def pytest_cmdline_preparse(config, args):

    # 如果能从命令行获取传入env和frequency参数
    # 就将其替换pytest.ini extra section中的值
    pyconfig["sections"] = config.inicfg.config.sections
    _section_extra = pyconfig["sections"].get('extra', None)
    _section_report = pyconfig["sections"].get('report', None)
    _section_mail = pyconfig['sections'].get('mail', None)
    _section_mobile = pyconfig['sections'].get('mobile', None)
    pyconfig['mail'] = _section_mail
    pyconfig['mobile'] = _section_mobile

    # 设置各种格式的日志
    if _section_report.get("html").strip().lower() == "true":
        args.append("--html={}".format(pyconfig['logfile'].get('html')))
        args.append("--self-contained-html")
    if _section_report.get("json").strip().lower() == "true":
        args.append("--json={}".format(pyconfig['logfile'].get('json')))
    if _section_report.get("xml").strip().lower() == "true":
        args.append("--junitxml={}".format(pyconfig['logfile'].get('xml')))

    # 设置默认addopts
    args.append("--cache-clear")    # remove all cache contents at start of test run.
    args.append("-v")               # increase verbosity
    args.append("--color=yes")      # color terminal output (yes/no/auto)

    for _cmdline_args_item in args:
        # 如果能从命令行获取传入env，将其赋予pyconfig全局变量中
        if "--env" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            config.inicfg.config.sections['extra']['env'] = arg_item[-1]
            pyconfig["env"] = arg_item[-1]  # 替换全局变量 env
        else:
        #  否则从ini中获取env
           pyconfig['env'] = _section_extra.get("env", None)

        if "frequency" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            config.inicfg.config.sections['extra']['frequency'] = arg_item[-1]
            pyconfig["frequency"] = arg_item[-1] # 替换全局变量 frequency
        else:
            pyconfig["frequency"] = _section_extra.get("frequency", None)

        if "--monitor" in _cmdline_args_item:
            pyconfig['monitor'] = True

        if "--driver" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            pyconfig['driver'] = arg_item[-1]

def pytest_addoption(parser):
    # 自动产生日志文件
    pyconfig["rootdir"] = parser._anonymous.parser.extra_info['rootdir'].strpath
    pyconfig['logfile'] = cb.get_log_path_forPytest()
    parser.addini(name='log_file' , help="log file" , type=None , default=pyconfig['logfile'].get("log"))

    # 添加命令行参数
    parser.addoption("--env", action="store", default='qa',
        help="测试环境输入项 如qa、yz、prod 可参考poseidon/base/Env.py")
    parser.addoption("--frequency", action="store", default='five_min',
        help="执行间隔输入项 如one_min、five_min、one_hour、one_day、one_day 可参考poseidon/base/Frequency.py")

def pytest_collection_modifyitems(session, config, items):
    """
    通过env和frequency过滤需要执行的测试用例
    """
    # 根据mark.run传入的参数，过滤需要执行的用例
    for item in items:
        # 获取mark为run的items
        mark_run = [env.args for env in item.iter_markers(name='run')]
        mark_runs = list(mark_run[0]) if mark_run and mark_run[0] else []
        if len(mark_runs) != 0:

            mark_runs_env = [item.name for item in mark_runs[0]]
            mark_runs_frequency = [item.name for item in mark_runs[1]]

            # 获取命令行或者ini中传入env和frequency
            _filter_env = pyconfig.get("env", "qa")
            _filter_frequency = pyconfig.get("frequency", "one_min")

            if _filter_env not in mark_runs_env:
                skip_mark = pytest.mark.skip("因为env参数不是: %s" % (_filter_env))
                item.add_marker(skip_mark)
            if _filter_frequency not in mark_runs_frequency:
                skip_mark = pytest.mark.skip("因为frequency参数不是: %s" % (_filter_frequency))
                item.add_marker(skip_mark)

@pytest.fixture(scope='class')
def driver_headless():

    if 'driver' in pyconfig and pyconfig['driver'].strip().lower() == 'chrome':
        from selenium import webdriver
        options = webdriver.ChromeOptions()  # option对象
        options.add_argument('headless')  # 给option添加属性
        driver = webdriver.Chrome(options=options)
        return driver
    else:
        print('该浏览器不支持无头')

@pytest.fixture(scope='function')
def driver_android():

    from poseidon.ui.mobile.android.init_driver import get_desired_caps

    _desired_caps = get_desired_caps()
    if not 'newCommandTimeout' in _desired_caps:
        _desired_caps['newCommandTimeout'] = 60

    if 'command_executor' in _desired_caps:
        _com_executor = _desired_caps.pop('command_executor')
    else:
        _com_executor = 'http://localhost:4723/wd/hub'

    from appium import webdriver
    driver = webdriver.Remote(_com_executor, _desired_caps)
    logging.info(f'starting launch {_desired_caps}'.center(50, '#'))

    yield driver

    logging.info(f'ending {_desired_caps}'.center(50, '#'))
    driver.quit()
