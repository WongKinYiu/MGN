#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np  
import sys,os  
import cv2
caffe_root = '/home/lwp/beednprojects/caffe-2.7/'
sys.path.insert(0, caffe_root + 'python')  
import caffe
from PIL import Image

def MGN(image_path):    
    # PIL Image
    image = Image.open(image_path) # RGB
    print(image.size)
    image = image.resize((128, 384))
    print(image.size)

    image = np.array(image)
    image = image / 255.0
    
    transformer = caffe.io.Transformer({'blob1': (net.blobs['blob1'].data.shape)}) # (1,3,348,128)
    transformer.set_transpose('blob1', (2, 0, 1))  # python read image format as (h,w,c),-->(c,h,w)

    transformer_image = transformer.preprocess('blob1', image)
    print(transformer_image.shape)
    net.blobs['blob1'].data[...] = transformer_image
    
    output = net.forward()
    batch_norm11 = net.blobs['batch_norm11'].data[0][:]
    print(batch_norm11)
    # conv1 = net.blobs['conv1'].data[0]
    # print(conv1)

    
if __name__ == '__main__':
    np.set_printoptions(precision=8, threshold='nan')

    # 配置路径
    model_def     = 'MGN.prototxt'
    model_weights = 'MGN.caffemodel' 
    image_path    = "test.jpg"
    # 加载模型
    net = caffe.Net(model_def, model_weights, caffe.TEST)
    
    # MGN
    MGN(image_path)

    print("Done!")
    
        
