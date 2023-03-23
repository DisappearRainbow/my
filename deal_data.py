import os,shutil
import time
import random
def train_val():

    dir_name = os.listdir(r"E:\无人机检测与追踪2\无人机检测与追踪2\data\labels")
    print(len(dir_name))
    random.shuffle(dir_name)

    src_path='E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\labels\\'
    target_path='E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\train\\'
    target_path_1='E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\test\\'

    #8:2
    for file in dir_name[:16000]:
        shutil.move(src_path+file,target_path+file)
    for file in dir_name[16000:20000]:
        shutil.move(src_path+file,target_path_1+file)


def trans_img():
    dir_name_1 = os.listdir(r"E:\无人机检测与追踪2\无人机检测与追踪2\data\labels\train")
    dir_name_2 = os.listdir(r"E:\无人机检测与追踪2\无人机检测与追踪2\data\labels\val")
    target_path_1 = 'E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\images\\train\\'
    target_path_2 = 'E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\images\\val\\'

    for file in dir_name_1:
        f = file.split(".")
        shutil.move("E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\image\\" + f[0] +".jpg", target_path_1 + f[0] +".jpg")
    for file in dir_name_2:
        f = file.split(".")
        shutil.move("E:\\无人机检测与追踪2\\无人机检测与追踪2\\data\\image\\" + f[0] + ".jpg", target_path_2 + f[0] + ".jpg")
import numpy as np
np.version

trans_img()