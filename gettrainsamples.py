#--coding:utf-8--
import numpy as np
import pandas as pd
import cv2


traini = 1
m = 59
obj_num = 12

cap = cv2.VideoCapture(0)
rt = np.zeros([2,2], dtype=np.int)
index = 0
count = np.zeros(obj_num)
issaved = False
list_file = open('./gestures_data/train%d.txt' % traini, 'a+')
while(True):
    _, frame = cap.read()
    img = frame.copy()
    rt[0,0] = np.random.randint(8,img.shape[1]-8)
    rt[0,1] = np.random.randint(8,img.shape[0]-8)
    ratio = 1 if np.random.rand()>0.5 else 1.6
    width = np.random.randint(50, int(img.shape[1]/3.))
    rt[1,0] = rt[0,0]+width if rt[0,0]+width<img.shape[1] else img.shape[0]
    rt[1,1] = int(width*ratio+rt[0,1]) if int(width*ratio+rt[0,1])<img.shape[0] else img.shape[0]
    if rt[1,0]-rt[0,0]<50 or rt[1,1]-rt[0,1]<50:
        continue
    
    frame = cv2.rectangle(frame,(rt[0,0],rt[0,1]),(rt[1,0],rt[1,1]),(0,255,0),3)
    cv2.imshow('frame',frame)
    if index==99:
        continue
    if index==100:
        break
    single_num = 0
    print count
    while(True):
        _, frame = cap.read()
        img = frame.copy()
        if issaved:
            cv2.imwrite(('./gestures_data/train%d/%d_%d.jpg' % (traini, index,count[index])), img)
            list_file.write("./gestures_data/train%d/%d_%d.jpg " %(traini,index,count[index])+ "%d,%d,%d,%d,%d\n" %(rt[0,0], rt[0,1],rt[1,0],rt[1,1],index))
            print (index, count[index])
            single_num += 1
            count[index] += 1

        frame = cv2.rectangle(frame,(rt[0,0],rt[0,1]),(rt[1,0],rt[1,1]),(0,255,0),3)
        cv2.imshow('frame',frame)

        key = cv2.waitKey(5)
        if key==115: #press 's'
            issaved = not issaved
            if issaved:
                print 'save'
                index = int(raw_input('input class(0-11):'))
                print index
                cv2.waitKey(1000)

            else:
                print 'pause'
        if key==110: #press 'n'
            issaved = False
            break
        if key==113: #press 'q'
            exit()
        if single_num > m:
            issaved = False
            break

cap.release()
cv2.destroyAllWindows()