# 其他
- **如何使用requirements.txt**
```bash
pip freeze > requirements.txt    #生成
pip install -r requirements.txt  #使用
```
<br/>

- **日志使用尽量只使用error、info、debug三个等级**
 - error： 表示错误
 - info：  表示执行过程中需要显示的内容，方便跟踪错误点
 - debug： 表示在调试时使用，在巡检过程中不会显示 
  
```python
import logging

logging.error("error info detail")
logging.info("log info detail")
logging.debug("debug info detail")
```
<br/>







- 制作 plugin 命令
```shell
python setup.py sdist upload -r http://qa.pip.yeshj.com # 制作安装包并上传
or
python setup.py sdist # 制作安装包
pip install Tetis -i http://qa.pip.yeshj.com/simple --trusted-host qa.pip.yeshj.com    #安装Tetis          
or 
pip install Tetis
pip install --upgrade  Tetis -i http://qa.pip.yeshj.com/simple --trusted-host qa.pip.yeshj.com   #更新Tetis
or
pip install --upgrade  Tetis
```



- 设置pip私有仓库

```shell
# vim ~/.pip/pip.conf
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
extra-index-url = http://qa.pip.yeshj.com/simple

trusted-host=
        mirrors.aliyun.com
        qa.pip.yeshj.com
```

- 查看pip私有仓库中的安装包


```shell
pip search Tetis -i http://qa.pip.yeshj.com/simple
```
