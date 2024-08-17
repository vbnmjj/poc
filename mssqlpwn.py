import pyodbc

def test_mssql_connection(server, database, username, password):
    try:
        # 设置连接字符串
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        
        # 创建连接
        conn = pyodbc.connect(connection_string)
        
        # 创建一个cursor对象
        cursor = conn.cursor()
        
        # 执行一个简单的查询
        cursor.execute("SELECT 1")
        
        # 获取查询结果
        result = cursor.fetchone()
        
        if result:
            print("MSSQL connection successful!")
        else:
            print("MSSQL connection failed.")
        
        # 关闭连接
        cursor.close()
        conn.close()
        
    except pyodbc.Error as e:
        print("Could not connect to MSSQL:", e)

# MSSQL服务器配置
server = 'your_server'      # 替换为你的服务器地址
database = 'your_database'  # 替换为你的数据库名称
username = 'your_username'  # 替换为你的用户名
password = 'your_password'  # 替换为你的密码

test_mssql_connection(server, database, username, password)
