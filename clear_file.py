# 定期删除指定日期之前的日志文件
import os
import time
import shutil

# 1、确定文件路径
path = 'E:\\test'
# 2、确定要删除的指定天数
DEL_DAY = 20
# 3、获取文件名称，判断文件时间，循环删除
now = time.time()  # 获取当前时间
for i in range(1, 6):
    list_dir = os.listdir(path.format(i))
    if len(list_dir) == 0:
        print('该目录下没有文件')
        pass
    else:
        for dir_name in list_dir:
            time_ = int(now - os.path.getctime(path + '\\' + dir_name)) // 86400
            if time_ >= 20:
                if os.path.isdir(path + '\\' + dir_name):
                        shutil.rmtree(path + '\\' + dir_name)
                else:
                        os.remove(path + '\\' + dir_name)
print('清理完成')
