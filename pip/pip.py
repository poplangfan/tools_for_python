# 自动化安装第三方库脚本
import os

libs = []
with open('E:/PythonCode/pip/packages.txt', 'r', encoding='utf-8') as f:
    cont = f.read()
    conts = cont.split(',')
    for package in conts:
        libs.append(package)
# print(libs)
try:
    for lib in libs:
        os.system('pip install ' + lib)
    print('Successful')
except:
    print('Failed Somehow')
