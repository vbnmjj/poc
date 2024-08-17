from pymongo import MongoClient

def test_mongodb_connection(uri):
        # 创建一个MongoDB客户端
        client = MongoClient(uri)
        
        # 尝试连接到服务器
        client.admin.command('ping')
        print("MongoDB connection successful!")
        
        # 获取数据库列表
        dbs = client.list_database_names()
        print("Databases:", dbs)
        
# MongoDB URI格式："mongodb://username:password@host:port/dbname"
# 本地MongoDB示例："mongodb://localhost:27017/"
mongodb_uri = "mongodb://10.154.18.40:27017/"
test_mongodb_connection(mongodb_uri)
