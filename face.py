# coding=utf-8

import sys
import os
import dlib
import glob
from skimage import io

predictor_path = './predictor/data'
face_model_path = './model/data'
img_path = './shit/'

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_path)
face_rec = dlib.face_recognition_model_v1(face_model_path)
win = dlib.image_window()

def get_face_vectors(img, show=False):
    dets = detector(img, 1)
    face_vectors = list()
    for k, d in enumerate(dets):
        shape = shape_predictor(img, d)
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        face_vectors.append(face_descriptor)
        if show:
            show_pic(img, d, shape)
            dlib.hit_enter_to_continue()
    return face_vectors

def load_imgs():
    imgs = list()
    names = list()
    for f in glob.glob(os.path.join(img_path, "*.jpg")):
        print("Processing file: {}".format(f))
        img = io.imread(f)
        imgs.append(img)
        names.append(f)
    return imgs, names

def show_pic(img, d, shape):
    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(d)
    win.add_overlay(shape)

def write(face_vector, filename):
    with open('tiny-vector/'+filename+'.txt', 'w') as fw:
       # for each in face_vector:
        fw.write(str(face_vector)+'\t')

def main():
    imgs, names = load_imgs()
    #face_vectors = list()
    for i in range(len(imgs)):
        vec = get_face_vectors(imgs[i])
        try:
            write(vec[0], names[i][7:-4])
        except IndexError:
            print(names[i])
            pass
        print(names[i] + "writed.")
    #for each in imgs:
        #face_vectors.extend(get_face_vectors(each))
        #print(face_vectors)
    #assert len(face_vectors) == len(names)
    #for i in range(len(face_vectors)):
        #write(face_vectors[i], names[i])

main()
