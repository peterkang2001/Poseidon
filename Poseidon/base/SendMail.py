# coding=utf-8

__author__ = 'songmengyun'

import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from pytest_testconfig import config as pyconfig



class SendMail():

    def __init__(self, receivers, header, subject, url, env='qa'):
        self.from_addr = 'hjqa@hujiang.com'
        self.smtp_server = 'mail.hujiang.com'
        self.smtp_port = 25
        self.receivers = receivers
        self.header = header
        self.subject = subject
        self.url = url
        self.env = env

    def html_report(self, name, json_report_dict):
        summary = json_report_dict['report']['summary']
        mail_msg = """
                <p>Hi, All:</p>
                <p>以下是：%s(%s)：</p>
                <p>总用例数:%s</p>
                <p><font style='color:green;'>成功:%s</font> &nbsp; <font style='color:red;'>失败:%s</font> &nbsp; <font style='color:gray;'>跳过:%s</font></p>
                <p>执行时长: %s</p>
                <p><a href="%s">点击查看报告详情</a></p>
                """%(name, self.env, summary.get('num_tests'),
                     summary.get('passed', 0),summary.get('failed', 0),
                     summary.get('skipped', 0),summary.get('duration', 0),  self.url)
        return mail_msg

    def send_mail(self, mail_msg):
        receivers = self.receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(mail_msg , 'html' , 'utf-8')
        message['From'] = Header("%s"%(self.header) , 'utf-8')  # 发送者
        message['To'] = Header(','.join(receivers) , 'utf-8')  # 接收者

        subject = '%s'%(self.subject) # 发送主题
        message['Subject'] = Header(subject , 'utf-8')

        try:
            smtpObj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtpObj.set_debuglevel(1)
            smtpObj.sendmail(self.from_addr , receivers , message.as_string())
            logging.info("邮件发送成功")
        except smtplib.SMTPException as e:
            logging.error("Error: 邮件发送失败")
            raise e
        finally:
            smtpObj.quit()
