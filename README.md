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

```cmd
  from mongodb_to_xls.mongodb_to_xls import mongodb_to_xls
  #倒库
  mongodb_to_xls("userdb","D:\\test.xls")
```

在上面代码中 *mongodb_to_xls* 函数有两个值，第一个值为数据库中collections文件夹下要装换的集合，第二个值为要输出的文件地址

**如何将testdb更改为自己的db,打开*mongodb_to_xls.py*找到

```python
  db = myclient.testdb
```

将*testdb*更改为自己的数据库即可**


