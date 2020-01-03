# Changelog history
### 0.0.44 (2019-12-04)
1. 修改旧版本MQ都新版本

### 0.0.43 (2019-08-28)
1. 支持大小写application/x-www-form-urlencoded的pycurl请求

### 0.0.42 (2019-08-27)
1. 新增application/x-www-form-urlencoded的pycurl请求

### 0.0.41 (2019-08-27)
1. 优化application/x-www-form-urlencoded的request请求

### 0.0.40 (2019-08-27)
1. 新增支持application/x-www-form-urlencoded的request请求

### 0.0.39 (2019-07-16)
1. 修复自动识别metric，根据项目名获取metric

### 0.0.38 (2019-07-15)
1. 修复了memcache中多余的引用
2. 修复了redis中默认值为uc

### 0.0.37 (2019-07-04)
1. 新增UI无头浏览
2. 修改metric

### 0.0.36 (2019-07-04)
1. 修改错别字，优化巡检和发送邮件功能

### 0.0.35 (2019-07-04)
1. 新增运行后发邮件功能

### 0.0.34 (2019-07-02)
1. 优化requests发送请求

### 0.0.33 (2019-07-02)
1. 更新requests发送请求，修改data序列化

### 0.0.32 (2019-06-27)
1. 优化巡检脚本，接入新的报警接口

### 0.0.31 (2019-06-27)
1. 优化巡检脚本

### 0.0.30 (2019-06-27)
1. 优化巡检脚本

### 0.0.29 (2019-06-27)
1. 新增巡检失败微信报警，如果命令行传入"--xunjian",代码接入微信报警

### 0.0.28 (2019-06-19)
1. 更新了setup中默认安装包，新增了requests


### 0.0.27 (2019-06-19)
1. 弃用commonbase中的tc_describe方法，统一使用python文档注释作为测试用例的中文说明
2. 将测试用例的文档注释加入到html和log格式的日志中

### 0.0.26 (2019-06-14)
1. 通过类型判断http请求的header，支持list和dict两种类型的header格式
2. 修复包中ui目录下空文件的问题

### 0.0.25 (2019-06-14)
1. 为http请求增加了基础方法method和response日志
2. 增加了了mq的实现
3. 增加了memcache的实现
至此 三大工具 redis、mq、memcache基本完成

### 0.0.24 (2019-06-14)
1. 完善了redis的实现
2. 修复了commonBase中的getTimestamp不支持python3的问题
3. 修复了commonBase日志中带<red>的信息

### 0.0.23 (2019-06-13)
1. 增加request的支持，同时支持pycurl和request请求
2. 对pycurl和增加容错处理
3. 对pycurl增加patch方法的支持
