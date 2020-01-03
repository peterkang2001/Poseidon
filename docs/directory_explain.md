# 目录结构
**business:**
- **apiBuinessCaseA**:  业务相关方法
- **pages**: 当使用到ui自动化的时候，这个目录保存某个页面的相关操作方法，这个属于[PO(PageObject)](https://blog.csdn.net/leelanting/article/details/80662321)的概念
- **commonUtils**: 与业务相关的公共方法（比如生成用户名，生成密码等）
- **model**: 保存orm对应的数据类（使用SQLAlchemy访问数据库的时候会使用到
<br/>
备注: 
<br/>
1. 为减少目录结构的复杂性，建议只在该目录下建立一层目录
2. 目录前面前缀api表示这个业务与api测试有关
3. 框架不限制用户使用自己熟悉的数据库访问的第三方库（推荐使用[SQLAlchemy](https://www.sqlalchemy.org/)访问mysql数据库，谁用谁知道😆）
<br/>
<br/>

**data:**
- **dataBuinessCaseA**: BuinessCaseA相关的测试数据
- **dataBuinessCaseB**: BuinessCaseB相关的测试数据（以此类推不再穷举）
<br/>
备注
<br/>
1. 子目录必须以data开头，余下部分单词首字母大写
2. 为减少目录结构的复杂性，建议只在该目录下建立一层目录
3. 测试数据文件可以以任何格式进行保存， 目前常用文件格式有.py .ini .json .yaml(不建议使用xls作为数据文件)
<br/>
<br/>

**testcase:**
- **testBuinessCaseA**: BuinessCaseA相关的测试用例
- **testBuinessCaseB**: BuinessCaseB相关的测试用例（以此类推不再穷举）
<br/>
备注
<br/>
1. 子目录必须以test开头，余下部分单词首字母大写
2. 为减少目录结构的复杂性，建议只在该目录下建立一层目录
3. 业务测试目录中保存测试用例文件，文件名必须以test开头，余下部分单词首字母大写（如testXxxxXxxx.py）
4. 测试文件中的测试类必须以Test开头，余下部分单词首字母大写(如 class TestXxxxXxx)
<br/>
<br/>
**testcase_pc_ui:**
- web ui的自动化测试用例在此保存（如果项目中没有web ui脚本可以删除这个目录，web ui自动化测试和api接口测试公用一个business目录）
<br/>
<br/>

**logs:**
<br/>
备注
<br/>
1. 操作所以运行日志，每执行一次都会产生相应的日志文件
2. 目前一次会产生3中格式的日志(.log .html .json)
<br/>
<br/>



**项目根目录**
- **.dockerignore**: 生成docker image时使用，一般无需修改
- **.gitignore**：git专用文件，一般无需修改
- **conftest.py**: pytest专用文件，一般无需修改
- **Dockerfile**： 生成docker image时使用，一般无需修改
- **Dockerfile_base**： 生成docker image时使用，一般无需修改
- **pytest.ini**: pytest配置文件，视情况修改
- **README.md**: 项目帮助文档入口
- **requirements.txt**: 重新搭建开发环境使用
