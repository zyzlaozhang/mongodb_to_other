import pymongo
import xlwt
import sys

#获取命令行输入
db_name=sys.argv[1]
set_name=sys.argv[2]
xls_path=sys.argv[3]

def mongodb_to_xls(db_name,set_name,xls_path,port=27017):
    #初始化变量
    key_list=[]
    l,i=-1,0
    #初始化输入参数
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('json',cell_overwrite_ok=True)
    #初始化数据库
    myclient = pymongo.MongoClient(f'mongodb://localhost:{port}/')
    db = myclient[db_name] #testdb可按需求改动
    coll = db.get_collection(set_name)
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
                for y in range(len(key_list)):
                    if isinstance(key_list[y],list):
                        z=y
                        for u in key_list[y]:
                            sheet.write(l,z,str(u))
                            z+=1
                    else:
                        sheet.write(l,y,str(key_list[y]))
    book.save(xls_path)

#示例

mongodb_to_xls(db_name,set_name,xls_path)

#命令行————››› python mongodb_to_xls_cmd.py 你的数据库名 你的集合名 输出文件路径