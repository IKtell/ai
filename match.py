# coding=utf-8

import sys
import os
import dlib
import glob
import math
from skimage import io

test_img = sys.argv[1]
predictor_path = 'predictor/data'
face_model_path = './model/data'

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_path)
face_rec = dlib.face_recognition_model_v1(face_model_path)
win = dlib.image_window()


def get_pic():
    pass

def distance(vec1, vec2):
    assert len(vec1) == len(vec2)
    sum = 0.0
    for i in range(len(vec1)):
        sum += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(sum)

def get_filenames():
    files = os.listdir('tiny-vector')
    return files

def read_datas():
    files = os.listdir('tiny-vector')
    vectors = list()
    for each in files:
        with open('./tiny-vector/'+each, 'r') as fr:
            data = [float(x[:-1]) for x in fr.readlines()]
            vectors.append(data)
    return vectors

def match():
    img = io.imread(test_img)
    win.clear_overlay()
    win.set_image(img)
    dets = detector(img,1)

    face_des = list()
    for k, d in enumerate(dets):
        shape = shape_predictor(img, d)
        win.clear_overlay()
        win.add_overlay(d)
        win.add_overlay(shape)

        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        face_des.append(face_descriptor)
        print(face_descriptor)
        dlib.hit_enter_to_continue()
    return face_des[0]

def main():
    vectors = read_datas()
    vec = match()
    min = 1
    distances = list()
    for i in range(0, len(vectors)):
        dis = distance(vec, vectors[i])
        distances.append(dis)
        if (dis < min):
            min = dis
    filenames = get_filenames()
    dic = dict()
    for i in range(len(filenames)):
        dic[distances[i]] = filenames[i]

    distances.sort()    
    for i in range(0, 5):
        print('您的照片匹配的是:' + dic[distances[i]] + ' ' + str(distances[i]))

main()