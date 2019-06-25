# 定期删除指定日期之前的日志文件
import os
import datetime

# 1、确定文件路径
path = './'
# 2、获取文件名称，判断文件时间
list_dir = os.listdir(path)
for dir in list_dir:
    print(dir)
    if os.path.isfile(dir):
        os.path.getctime(dir)
        print('wenjian', datetime.datetime.fromtimestamp(os.path.getctime(dir)))
    else:
        os.path.getctime(dir)
        print('wenjianjia')
# 3、删除指定日期之前的所有文件，文件夹
delta = datetime.timedelta(days=20)  # 设定365天前的文件为过期
now = datetime.datetime.now()  # 获取当前时间

