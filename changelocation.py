import os
import shutil


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

def same_name()


#对象文件的类型指定
file_type_list = ['pdf','txt','xls','xlsx','pptx']  

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


if(__name__=="__main__"):
    #copy源所在目录
    src_folder = r'C:\Users\eguwenh\Desktop\python'  #路径最后不要加\  (填入对应的copy源路径）
    #copy到的指定目录
    dst_folder = r'C:\Users\eguwenh\Desktop\python_t'   #路径最后不要加\  (填入对应的copy to路径）
    
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
