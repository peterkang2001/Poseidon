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
