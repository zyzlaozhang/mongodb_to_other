import pymongo
import xlwt

def mongodb_to_xls(db_name,xls_path):
    #初始化变量
    key_list=[]
    l,i=-1,0
    #初始化输入参数
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('json',cell_overwrite_ok=True)
    #初始化数据库
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    db = myclient.testdb #testdb可按需求改动
    coll = db.get_collection(db_name)
    #开始写入
    for i in coll.find():
        for x in i.items(): 
            db_item={x[0]:x[1]}
            #的出一个数据库项
            for key,value in db_item.items():
                key_list.clear()
                key_list.extend((key, value))
                #位置设置
                i,l=1,l+1
                #写入
                #i 列，l 行
                for i in range(len(key_list)):
                    sheet.write(l,i,str(key_list[i]))
    book.save(xls_path)

#示例
mongodb_to_xls("userdb","D:\\test123.xls")