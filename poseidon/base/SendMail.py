# coding=utf-8

__author__ = 'songmengyun'

import smtplib
import logging
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header
from pytest_testconfig import config as pyconfig



class SendMail():

    def __init__(self, sender, receiver, mail_title, smtp_server='xxx@xxx.com', smtp_port=25):
        self.sender = sender
        self.receiver = receiver

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.mail_title = mail_title

    def _get_html_report_path(self):
        html_path = pyconfig['logfile'].get('html')
        return html_path

    def _read_html_report(self):
        path = self._get_html_report_path()
        with open(path, 'rb') as f:
            mail_body = f.read()
        return mail_body

    def html_report(self, name, json_report_dict, url):
        summary = json_report_dict['report']['summary']
        mail_msg = """
                <p>Hi, All:</p>
                <p>以下是：%s(%s)：</p>
                <p>总用例数:%s</p>
                <p><font style='color:green;'>成功:%s</font> &nbsp; <font style='color:red;'>失败:%s</font> &nbsp; <font style='color:gray;'>跳过:%s</font></p>
                <p>执行时长: %s</p>
                <p><a href="%s">点击查看报告详情</a></p>
                """%(name, pyconfig['env'], summary.get('num_tests'),
                     summary.get('passed', 0),summary.get('failed', 0),
                     summary.get('skipped', 0),summary.get('duration', 0),  url)
        return mail_msg

    def send_mail(self):
        receivers = self.receiver  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        mail_body = self._read_html_report()

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(mail_body , 'html' , 'utf-8')
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人

        try:
            smtpObj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            # smtpObj.set_debuglevel(1)
            smtpObj.sendmail(self.sender , receivers , message.as_string())
            logging.info("邮件发送成功")
        except smtplib.SMTPException as e:
            logging.error("Error: 邮件发送失败")
            raise e
        finally:
            smtpObj.quit()
