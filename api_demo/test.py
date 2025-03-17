from api1 import API1
from api2 import API2
from api3 import API3
from api4 import API4
from db_config import get_db_config

# 数据库配置
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'demo'
} 

def test_api1():
    api = API1()
    users = api.execute()
    print("API1 - 所有用户:", users)

def test_api2(user_id):
    api = API2()
    user = api.execute(user_id)
    print(f"API2 - 用户 {user_id}:", user)

def test_api3(name, email):
    api = API3()
    api.execute(name, email)
    print(f"API3 - 插入用户: {name}, {email}")

def test_api4(user_id, new_email):
    api = API4()
    api.execute(user_id, new_email)
    print(f"API4 - 更新用户 {user_id} 的邮箱为: {new_email}")

if __name__ == "__main__":
    # 测试API1
    test_api1()
    
    # 测试API3 - 插入新用户
    test_api3("测试用户", "test@example.com")
    
    # 测试API2 - 查询新插入的用户
    test_api2(1)  # 假设新用户的ID为1
    
    # 测试API4 - 更新用户邮箱
    test_api4(1, "new_email@example.com")
    
    # 再次测试API1，查看更新后的用户列表
    test_api1()