# 导包
import configparser
config = configparser.ConfigParser() # 类实例化
# 定义文件路径
path = r'config.ini'

# 第一种读取ini文件方式,通过read方法
config.read(path,encoding='UTF-8')
value = config['select']['age']
print('第一种方法读取到的值：',value)

# 第二种读取ini文件方式，通过get方法
value = config.getint('select','age')
print('第二种方法读取到的值：',value)

# 第三种读取ini文件方式，读取到一个section中的所有数据，返回一个列表
value = config.items('select')
print('第三种方法读取到的值：',value)

# 将数据写入到ini文件中
config.add_section('login') # 首先添加一个新的section
config.set('login','username','admin')  # 写入数据
config.set('login','password','123456') # 写入数据

 #保存数据
config.write(open(path,'a',encoding='UTF-8'))           

# 读取ini文件中所有的section
section = config.sections()
print(section)