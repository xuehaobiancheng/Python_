import os
import shutil
import time

import logging


TEMP_PATH = '/data/temp'
PACKAGE_PATH = '/data/package'


def rm_file():
    if os.path.exists(TEMP_PATH):
        shutil.rmtree(TEMP_PATH, True)
        os.makedirs(TEMP_PATH)
    else:
        os.makedirs(TEMP_PATH)
    return True
#转移，需要传入需要转移的文件路径，和要转移到的路径
def move_file(file_path, new_file_path):
    if os.path.exists(new_file_path):
            shutil.move(file_path, new_file_path)
    else:
        os.makedirs(new_file_path)
        shutil.move(file_path, new_file_path)
    return True


#对象文件的类型指定
file_type_list = ['pdf','txt','xls','xlsx','pptx','mp4']  

#取得文件夹下面的所有指定类型的文件全名（路径+文件名）
def get_file_list(folder):
    filelist = []  #存储要copy的文件全名
    for dirpath,dirnames,filenames in os.walk(folder):
        for file in filenames:
            # file_type = file.split('.')[-1]
            # if(file_type in file_type_list):
                file_fullname = os.path.join(dirpath, file) #文件全名
                filelist.append(file_fullname)
    return filelist

#将文件list里面的文件拷贝到指定目录下
def copy_file(src_file_list, dst_folder):
    print('===========copy start===========')
    for file in src_file_list:
        shutil.copy(file, dst_folder)
    print('===========copy end!===========')


def clear(path):
    logging.info('正在扫描：' + path)
    # 获取目录中的所有文件和文件夹名字
    dir_list = os.listdir(path)
    # 遍历循环每个目录
    for i in dir_list:
        # 拼接绝对路径
        abspath = os.path.join(os.path.abspath(path), i)
        # 判断是否是文件
        if os.path.isfile(abspath):
            # 判断文件是否是 ._ 开头的文件
            if i.startswith("."):
                # 删除文件
                # 这是彻底删除 回收站不会存在
                # 这是彻底删除 回收站不会存在
                # 这是彻底删除 回收站不会存在
                os.remove(abspath)
                logging.info('清理文件 : ' + abspath)
 
        else:
            # 不是文件就继续递归
            clear(abspath)
 
 

if(__name__=="__main__"):
    #copy源所在目录
    src_folder = r'/Volumes/wenMemory/haha'  #路径最后不要加\  (填入对应的copy源路径）
    #copy到的指定目录
    dst_folder = r'/Volumes/wenMemory/hahanew'   #路径最后不要加\  (填入对应的copy to路径）

    clear(src_folder)
    clear(dst_folder)    
    #取得文件夹下所有指定类型的文件全名
    filelist = get_file_list(src_folder)
    # copy_file(filelist, dst_folder)



    #将文件下的文件移动到指定路径
    #思考重名文件如何处理
    for file in filelist:
        # file_name = file.split(r'\')[-1]
        # os.path.abspath(des_folder)
        # if os.path.exists(file_name):
        #     os.rename(file_name,'')
        shutil.move(file,dst_folder)
        # time.sleep(1)
