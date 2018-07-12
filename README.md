# obj_annot
object annotation for object detection or recognition, here is for gesture annotation, left hand(0-5) and right hand(0-5, actually label 6-11). Actually it can be used any other object annotation if you want, such as faces.

The annotation results can be used for training or evalution in https://github.com/GaopanHuang/keras-yolo3, which is forked from https://github.com/qqwweee/keras-yolo3 

  1.press n for generating new boundingbox

  2.make sure object in the boundingbox, then press s for start

  3.enter object label in cmd window

  4.then the images with annotation will be saved automaticly, each time there will be saved m images.

  5.press q for exit

Here is the params:

    traini = 1   #the path images saved

    m = 59       #number of images saved each time

    obj_num = 12 #number of objects
