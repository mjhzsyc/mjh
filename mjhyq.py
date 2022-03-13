import os
import sys

filename = sys.argv[1]  # 从控制台获取执行文件的参数
filepath = os.path.abspath(filename)  # 获取当前文件的工作路径
txt = []  # 创建列表
with open(filepath, "r", encoding='ANSI') as f:
    for line in f.readlines():
        data = line.splitlines()
        for cont in data:
            sub_cont = cont.split()
        if sub_cont:
            txt.append(sub_cont)
# 逐行读取文件，并进行分割存入txt列表
x = len(txt)  # 求出列表的长度
with open('yq_out.txt', "a", encoding='ANSI') as file:
    a = 0
    b = []
    z = []

    for i in range(0, x):
        if a != 0:
            z = txt[i][0]
            if z != b:
                a = 1
                file.write('\n' + txt[i][0] + '\n' + txt[i][1] + '  ' + txt[i][2])
                b = txt[i][0]
            else:
                file.write('\n' + txt[i][1] + '  ' + txt[i][2])
        if a == 0:
            b = txt[i][0]
            file.write(txt[i][0] + '\n' + txt[i][1] + '  ' + txt[i][2])
            a = a + 1
# 写入yq_out.txt
print("执行成功")
