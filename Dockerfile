FROM python:3.8.0

# 将宿主机目录下的文件拷贝进入/app
ADD . /app

# 登录后进入的目录
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["pytest", "-q","tests/test_example/test_api.py","--alluredir","allure-results"]
