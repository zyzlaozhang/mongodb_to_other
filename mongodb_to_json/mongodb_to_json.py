import json
import pymongo
def mongodb_to_json(db_name,set_name,json_path,port=27017):
    client = pymongo.MongoClient(host= '127.0.0.1', port=port)
    db = client[db_name]
    coll = db.get_collection(set_name)
    coll=list(coll.find())
    print(type(coll))
    l=len(coll)
    with open(json_path,"w+",encoding="utf-8") as f:
        f.write("[")
    n=0
    for i in coll:
        n+=1   
        with open(json_path,"a+",encoding="utf-8") as f:
            del i["_id"]
            print(i)
            print(type(i))
            f.write("   ")
            print(coll.index(i))
            print(l)
            if coll.index(i)==l-1:
                json.dump(i, f,ensure_ascii=False)
            else:
                json.dump(i, f,ensure_ascii=False)
                f.write(",")
            f.write("\n")
            f.close
        
    with open(json_path,"a+",encoding="utf-8") as f:
        f.write("]")