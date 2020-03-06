# coding=utf-8

"""
@author:songmengyun
@file: test_android.py
@time: 2019/12/25

"""

import pytest
import time
import logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.connectiontype import ConnectionType

from collections import namedtuple
from poseidon.ui.mobile.android.init_driver import init_driver


'''
Android 6.0 
包名和界面名
设置：com.android.settings/.Settings
短信：com.android.messaging/.ui.conversationlist.ConversationListActivity
系统浏览器：com.android.browser/.BrowserActivity
联系人：com.android.contacts/.activities.PeopleActivity
英语口语700句：com.hj.kouyu700/com.hujiang.browser.JSWebViewActivity
cctalk登录页面：com.hujiang.cctalk/com.hujiang.browser.view.X5HJWebViewActivity
安智市场：cn.goapk.market/com.anzhi.market.ui.MainActivity
京东：com.jingdong.app.mall/.main.MainActivity

'''

Device = namedtuple('device_info', ['platformName', 'platformVersion', 'deviceName'])
App = namedtuple('app_info', ['appPackage', 'appActivity'])

class TestAndroid:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which usually contains tests).
        """
        logging.info('setup_class'.center(50, "*"))
        cls.device_and_6 = Device('Android', '6.0', '192.168.57.103:5555')   # 需要连接平台名称，不区分大小写
        cls.app_setting = App('com.android.settings', '.Settings')   # 平台的版本[5.4.3/5.4/5]
        cls.app_mis = App('com.android.messaging', '.ui.conversationlist.ConversationListActivity')   # 设备的名称，随便写，但不能为空
        cls.app_anzi = App('cn.goapk.market', 'com.anzhi.market.ui.MainActivity')   # 需要打开的应用名称，可通过 adb shell dumpsys window windows | grep mFocusedApp 获取
        cls.app_lock = App('com.android.settings', '.ChooseLockPattern')   # 需要打开的界面名称

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to setup_class.
        """
        logging.info('teardown_class'.center(50, "*"))

    def setup_method(self, method):
        """ 所有case初始化操作 """
        logging.info('setup_method'.center(50, '*'))
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '192.168.57.103:5555',
            'platformVersion': '6.0',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings',
            'newCommandTimeout': '120',
            'noSign': True
        }
        self.driver = init_driver(desired_caps, command_executor='http://localhost:4723/wd/hub')

    def teardown_method(self, method):
        logging.info('teardown_method'.center(50, '*'))
        self.driver.quit()


    def test_start_activity(self):
        '''打开其他app： setup/teardown'''

        time.sleep(3)
        self.driver.start_activity(self.app_mis.appPackage, self.app_mis.appActivity)

    def test_get_package_activity(self):
        '''获取当前程序包名和界面名'''

        time.sleep(3)
        # 输出当前程序包名和界面名
        print(self.driver.current_package)
        print(self.driver.current_activity)

        # 切换到短信页面
        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_mis.appPackage  # 需要打开的应用名称，可通过 adb shell dumpsys window windows | grep mFocusedApp 获取
        desired_caps['appActivity'] = self.app_mis.appActivity  # 需要打开的界面名称
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        # 输出短信程序包名和界面名
        print(driver.current_package)
        print(driver.current_activity)

    def test_close_quit_app(self):
        '''关闭当前app/关闭驱动'''

        time.sleep(3)

        # self.driver.close_app()
        print(self.driver.current_package)
        print(self.driver.current_activity)
        print(self.driver.context)
        print(self.driver.contexts)
        print(self.driver.current_context)
        time.sleep(5)

        # self.driver.quit()
        # print(self.driver.current_package)
        # print(self.driver.current_activity)

    def test_install_uninstall_check(self):
        '''安装和卸载app'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        # 判断安智市场是否已经安置
        if driver.is_app_installed(self.app_anzi.appPackage):
            driver.remove_app(self.app_anzi.appPackage)
        else:
            driver.install_app('/Users/songmengyun/Downloads/testing/appium/anzhishichang_6630.apk')

        time.sleep(3)
        driver.quit()

    def test_background(self):
        '''后台运行app'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_anzi.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_anzi.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        # 置后台5s
        driver.background_app(5)

        time.sleep(3)
        driver.quit()

    def test_setting_element(self):
        '''定位1个元素：设置-点击放大镜-输入at-返回'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        # 通过ID定位放大镜按钮，点击
        search_butoon = driver.find_element_by_id('com.android.settings:id/search')
        search_butoon.click()
        # 通过CLASS定位输入框，输入at
        search_box = driver.find_element_by_class_name('android.widget.EditText')
        search_box.send_keys('at')
        # 通过XPATH定位返回按钮，点击
        driver.find_element_by_xpath("//*[@content-desc='收起']").click()

        time.sleep(5)
        driver.quit()

    def test_setting_elements(self):
        '''定位1组元素：设置-输出所有id/title上text的内容'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        # 通过ID获取resource-id为：com.android.settings:id/title的元素，并打印文字内容
        titles_ids = driver.find_elements_by_id('com.android.settings:id/title')
        for title in titles_ids:
            print(title.text)
        print('分割线'.center(100,'*'))

        # 通过CLASS获取class为：android.widget.TextView的元素，并打印文字内容
        titles_class = driver.find_elements_by_class_name('android.widget.TextView')
        for title in titles_class:
            print(title.text)
        print('分割线'.center(100,'*'))

        # 通过XPATH获取所有包含"设"的元素，并打印文字内容
        titles_xpath = driver.find_elements_by_xpath("//*[contains(@text,'设')]")
        for title in titles_xpath:
            print(title.text)

        time.sleep(5)
        driver.quit()

    def test_setting_implicitly_wait(self):
        '''元素等待：隐式等待'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 隐式等待
        driver.implicitly_wait(3)

        print('---准备找返回进行点击')
        driver.find_element_by_xpath("//*[@content-desc='收起']").click()
        print('---点完了')

        # time.sleep(5)
        driver.quit()

    def test_setting_webdriverwait(self):
        '''元素等待：显示等待'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 显示等待
        print('---准备找返回进行点击')
        wait = WebDriverWait(driver, 10, 1)
        back_button = wait.until(lambda x:x.find_element_by_xpath("//*[@content-desc='收起']"))
        # back_button = WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[@content-desc='收起']"))
        back_button.click()
        print('---点完了')

        driver.quit()

    def test_setting_click_element(self):
        '''元素等待：显示等待'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称
        desired_caps['unicodeKeyboard'] = True   # 输入框中文
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        eles = driver.find_elements_by_id('com.android.settings:id/title')
        for ele in eles:   # 获取文本内容
            print(ele.text)
            print((ele.get_attribute('enabled')))
            print((ele.get_attribute('clickable')))
            print((ele.get_attribute('focusable')))
            print((ele.get_attribute('name')))   # 获取content-desc或text值
            print((ele.get_attribute('scrollable')))
            print((ele.get_attribute('className')))   # 获取class属性值
            print((ele.get_attribute('resourceId')))   # 获取resource-id属性值

        search_buttton = driver.find_element_by_id('com.android.settings:id/search')
        print('放大镜位置：', search_buttton.location)   # 获取放大镜位置
        print(search_buttton.location['x'])
        print(search_buttton.location['y'])
        print('放大镜大小：',search_buttton.size)   # 获取放大镜大小
        print(search_buttton.size['width'])
        print(search_buttton.size['height'])
        search_buttton.click()   # 点击设置-放大镜按钮
        input_label = driver.find_element_by_class_name('android.widget.EditText')
        input_label.send_keys('hello')   # 输入"hello"
        time.sleep(2)   # 暂停2秒
        input_label.clear()   # 清空所有文本
        time.sleep(3)   # 暂停5秒
        input_label.send_keys('你好')   # 输入"你好"

        time.sleep(3)
        driver.quit()

    def test_setting_swipe(self):
        '''滑动：模拟手指从（100，2000），滑动到（100，1000）'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 模拟手指从（100，2000），滑动到（100，1000）
        # driver.swipe(100, 1500, 100, 1000)
        # driver.swipe(100, 1000, 100, 500)
        # driver.swipe(100, 500, 100, 0)
        # 从"更多"滑动到"语言和输入法"
        time.sleep(3)
        save_button = driver.find_element_by_xpath("//*[@text='更多']")
        more_button = driver.find_element_by_xpath("//*[@text='应用']")
        driver.scroll(save_button, more_button)
        # 从"更多"滑动到"打印"
        driver.drag_and_drop(more_button, save_button)

        time.sleep(20)
        driver.quit()

    def test_setting_touch_action_tap(self):
        '''手指轻敲操作：模拟手指对某个元素或坐标按下并快速抬起。比如固定点击100，100位置'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        waln_button = driver.find_element_by_xpath("//*[@text='WLAN']")

        # 轻敲"WLAN"
        # 1.创建TouchAction对象 2.调用tap执行动作 3.使用perform执行动作
        TouchAction(driver).tap(waln_button).perform()

        time.sleep(3)
        TouchAction(driver).tap(x=200,y=200,count=2).perform()

        time.sleep(5)
        driver.quit()

    def test_setting_touch_action_press_and_release(self):
        '''按下和抬起操作：模拟手指一直按下，模拟手指抬起'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        waln_button = driver.find_element_by_xpath("//*[@text='WLAN']")

        # 按下WLAN安装，2s后抬起
        TouchAction(driver).press(waln_button).perform()
        time.sleep(2)
        TouchAction(driver).press(waln_button).release().perform()

        time.sleep(5)
        driver.quit()

    def test_setting_touch_action_wait(self):
        '''等待操作：模拟手指等待，'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        waln_button = driver.find_element_by_xpath("//*[@text='WLAN']")

        # 点击WLAN，等待5秒后，再按下wiredssid等待2s再抬起
        TouchAction(driver).tap(waln_button).perform()
        time.sleep(2)
        TouchAction(driver).press(x=228, y=408).wait(2000).release().perform()

        time.sleep(5)
        driver.quit()

    def test_setting_touch_action_long_press(self):
        '''长按操作：模拟手指对元素或坐标的长按操作'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        waln_button = driver.find_element_by_xpath("//*[@text='WLAN']")

        # 使用坐标的形式点击WLAN，等待2s后，再长按下wiredssid的位置持续2s
        TouchAction(driver).tap(waln_button).perform()
        time.sleep(2)
        TouchAction(driver).long_press(x=228, y=408, duration=2000).release().perform()

        time.sleep(5)
        driver.quit()

    def test_setting_touch_action_move_to(self):
        '''移动操作：手势解锁，先按下再移动'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_lock.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_lock.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(2)

        # 根据坐标位置滑动元素
        TouchAction(driver).press(x=179,y=630).move_to(x=539,y=630)\
            .move_to(x=901,y=630). move_to(x=901,y=989)\
            .move_to(x=542,y=989).move_to(x=901,y=1349).release().perform()

        time.sleep(5)
        driver.quit()

    def test_get_windows_size_and_screenshort(self):
        '''获取当前设备分辨率并截图'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 获取当前设备的分辨率
        print(driver.get_window_size())
        # 手机截图
        driver.get_screenshot_as_file("screen.png")

        driver.quit()

    def test_get_set_network_connect(self):
        '''获取和设置当前网络'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 获取当前网络类型并打印
        print(driver.network_connection)
        # 设置当前网络-飞行模式
        driver.set_network_connection(1)
        # 判断当前网络是不是流量: 如果是,设置为wifi
        if driver.network_connection == ConnectionType.DATA_ONLY:
            driver.set_network_connection(ConnectionType.WIFI_ONLY)
        if driver.network_connection == ConnectionType.AIRPLANE_MODE:
            driver.set_network_connection(ConnectionType.WIFI_ONLY)

        driver.quit()

    def test_press_keycode(self):
        '''发送键到设备：模拟按返回/home键等等操作，'''

        # 点击三次音量加键
        self.driver.press_keycode(24)
        self.driver.press_keycode(24)
        self.driver.press_keycode(24)

        # 再点击返回
        self.driver.press_keycode(4)

        # 再点击两次音量减
        self.driver.press_keycode(25)
        self.driver.press_keycode(25)

    def test_open_notifications(self):
        '''操作手机通知栏'''

        desired_caps = dict()  # 初始化字典
        desired_caps['platformName'] = self.device_and_6.platformName  # 需要连接平台名称，不区分大小写
        desired_caps['platformVersion'] = self.device_and_6.platformVersion  # 平台的版本[5.4.3/5.4/5]
        desired_caps['deviceName'] = self.device_and_6.deviceName  # 设备的名称，随便写，但不能为空
        desired_caps['appPackage'] = self.app_setting.appPackage  # 需要打开的应用名称
        desired_caps['appActivity'] = self.app_setting.appActivity  # 需要打开的界面名称

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 打开通知栏
        driver.open_notifications()
        time.sleep(5)
        # 关闭通知栏，使用返回键
        driver.press_keycode(4)

        driver.quit()





