import os, sys
import random 

dir = os.path.dirname(__file__)
sys.path.append(dir)
#from ocr.tools.get_train_data import get_sample_set
#from ocr.tools.trian import train

from PIL import Image
import cv2
import numpy as np
from cv2 import boundingRect, countNonZero, cvtColor, drawContours, findContours, getStructuringElement, imread, morphologyEx, pyrDown, rectangle, threshold


def image_definition(fn):
    large = imread(fn)
    # downsample and use it for processing
    rgb = pyrDown(large)
    # apply grayscale
    small = cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    # morphological gradient
    morph_kernel = getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    '''
    getStructuringElement，可以获取常用的结构元素的形状：矩形（包括线形）、椭圆（包括圆形）及十字形。
    MORPH_RECT， MORPH_ELLIPSE， MORPH_CROSS
    而getStructuringElement函数的第二和第三个参数分别是内核的尺寸以及锚点的位置。对于锚点的位置，有默认值Point(-1,-1)，表示锚点位于中心。且需要注意，交叉形的element形状唯一依赖于锚点的位置。而在其他情况下，锚点只是影响了形态学运算结果的偏移。
    '''
    grad = morphologyEx(small, cv2.MORPH_GRADIENT, morph_kernel) 
    # MORPH_GRADIENT -形态学梯度（Morphological gradient）,一幅图像腐蚀与膨胀的区别，可以得到轮廓：膨胀减去腐蚀.可以突出高亮区域的外围，因为它是区域的膨胀减去区域的收缩
    # morph_kernel:形态学运算的内核.一般使用函数 getStructuringElement配合这个参数的使用

    # binarize
    _, bw = threshold(src=grad, thresh=0, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # threshold阈值化操作.给定一个输入数组和一个阈值，数组中的每个元素将根据其与阈值之间的大小发生相应的改变
    '''
        double cv::threshold(  
        cv::InputArray src, // 输入图像  
        cv::OutputArray dst, // 输出图像  
        double thresh, // 阈值  
        double maxValue, // 向上最大值  
        int thresholdType // 阈值化操作的类型   
    );  
    '''
    morph_kernel = getStructuringElement(cv2.MORPH_RECT, (9, 1))
    # connect horizontally oriented regions
    connected = morphologyEx(bw, cv2.MORPH_CLOSE, morph_kernel) # 闭运算先膨胀后腐蚀
    mask = np.zeros(bw.shape, np.uint8)
    # find contours 检测出物体的轮廓
    '''
    CV_RETR_CCOMP  检测所有的轮廓，但所有轮廓只建立两个等级关系，外围为顶层，若外围内的内围轮廓还包含了其他的轮廓信息，则内围内的所有轮廓均归属于顶层
    
    CV_CHAIN_APPROX_SIMPLE 仅保存轮廓的拐点信息，把所有轮廓拐点处的点保存入contours向量内，拐点与拐点之间直线段上的信息点不予保留
    '''
    im2, contours, hierarchy = findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    '''
    contours:返回的所有轮廓
    hierarchy：其中的元素个数和轮廓个数相同，每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。
    '''
    # filter contours 
    #print(small.shape)
    img_var = 0
    num = 0
    for idx in range(0, len(hierarchy[0])):
        # Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
        rect = x, y, rect_width, rect_height = boundingRect(contours[idx])
        # fill the contour
        mask = drawContours(mask, contours, idx, (255, 255, 2555), cv2.FILLED)
        # ratio of non-zero pixels in the filled region
        r = float(countNonZero(mask)) / (rect_width * rect_height)
        if r > 0.45 and rect_height > 12 and rect_width > 14:
            val = random.randint(0,3)
            #print(rect)
            if val != 2:
                rgb = rectangle(rgb, (x, y+rect_height), (x+rect_width, y), (0,255,0),1)
                img = small[x:x+rect_width, y:y+rect_height]
                #print(img)
                if not img.any():
                    continue
                else:
                    d = cv2.Laplacian(img, cv2.CV_64F).var()
                    img_var = img_var+d
                    num = num+1
                    #break
    #Image.fromarray(rgb).show()
    print(img_var/num)
    print('--------------------------------------')


def run_all_test_cases():
    #image_definition('./imgs/DoCoPhyExRe/Double01.jpg')
    file_dir = dir+'/imgs/DefinitionTestImages/'
    for root, dirs, files in os.walk(file_dir):
        # print(root, dirs, files)
        fns = sorted(files)
        for file in fns:
            print(file, ':\n')
            fn = file_dir + file
            image_definition(fn)


import datetime

start = datetime.datetime.now()

run_all_test_cases()

end = datetime.datetime.now()
print('run time:', (end-start).seconds/18)
