# -mongodb-python-
与mongodb有关

## 1.mongodb转xls

请确保自己的mongodb为此格式

_加粗的可以自行更改_

>**testdb**
>>collections
>>>**userdb**

本功能有两种方法调用

### 1.1 python函数

_以下代码请保证代码文件与 **mongodb_to_xls**在同一级目下运行_


```python
    from mongodb_to_xls.mongodb_to_xls import mongodb_to_xls
    #倒库
    mongodb_to_xls("testdb","userdb","D:\\test.xls")
```
在上面代码中 *mongodb_to_xls* 函数有三个值，**第一个值**为数据库的名称，**第二个值**为数据库中collections文件夹下要转换的集合，**第三个值**为要输出的文件地址

**如何将testdb更改为自己的db,打开*mongodb_to_xls.py*找到**

### 1.2 命令行
打开cmd输入 
```
 python mongodb_to_xls_cmd.py testdb userdb D:\\test.xls
```
三个值与1.1相同，不过多赘述


