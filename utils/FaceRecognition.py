import cv2
import numpy as np
from PIL import Image
import  os
# def DetectFaces():
#     grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     detect_face = cv.CascadeClassifier('/Users/atlas/fastAPI_py/.venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#     face = detect_face.detectMultiScale(grey_img, 1.01, 5,0,(100,100),(300, 300))
#     for (x, y, w, h) in face:
#         cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv.imshow('result', img)

#
# img = cv.imread('../images/face1.jpg')
# DetectFaces()
#
# while True:
#     if ord('q') == cv.waitKey(0):
#         break
#
# cv.destroyAllWindows()

names = []
recogizer = cv2.face.LBPHFaceRecognizer.create()
recogizer.read('train/train.yml')
# 数据训练
def getImageAndLabels(path):
    #储存人验数据
    facesSamples=[]
    #储存姓名数据
    ids=[] #储存图片信息
    imagePaths=[os. path. join(path, f) for f in os.listdir(path)] #如载分类器
    face_detector = cv2.Cascadeclassifier('/Users/atlas/fastAPI_py/.venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml') #遍历列表中的图片
    for imagePath in imagePaths:
        # 灰度化PIL有九种不同模式：1，L,P,RGB,RGBA,CMYK,YCbCr,I,F.
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转换为数组，以黑白深浅
        img_numpy=np.array(PIL_img, 'uint8') #获取图片人验特征
        faces = face_detector.detectMultiscale(img_numpy) #获取每张图片的10和姓名
        id = int(os. path.split(imagePath)[1].split('.')[0]) #预防无面容照片
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy [y: y+h, x: x+w]) #打印脸部特征和1d
        print('id:', id)
        print('fs:', facesSamples)
        return facesSamples, ids

# 人脸比对
#准备识别的图片
def face_detect_demo(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
    face_detector=cv2.Cascadeclassifier('D: /opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face=face_detector. detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    #face=face_detector.detectMultiscale(gray)
    for x,y, w, h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img, center=(x+w//2, y+h//2), radius=w//2, color=(0, 255,0), thickness=1) #人脸识别
        ids, confidence = recogizer.predict(gray[y: y+h, x: x+w])
        #print('标签id:',ids,'置信评分：'，confidence)
        if confidence >80:
            global warningtime
            warningtime + 1
            if warningtime > 100:
                warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img, str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow( 'result',img)



