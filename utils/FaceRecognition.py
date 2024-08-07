import cv2
import numpy as np
from PIL import Image
import os
from common.const import classifiers_path, facedata_path
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


# 数据训练
def getImageAndLabels(path: str, label: str):
    #储存人验数据
    facesSamples=[]
    #储存姓名数据
    labels = []
    #储存图片信息
    imagePath=path
    #如载分类器
    face_detector = cv2.CascadeClassifier(classifiers_path())
    #遍历列表中的图片
    # 灰度化PIL有九种不同模式：1，L,P,RGB,RGBA,CMYK,YCbCr,I,F.
    PIL_img=Image.open(imagePath).convert('L')
    print('阿松大', classifiers_path(),PIL_img, face_detector)
    #将图像转换为数组，以黑白深浅
    img_numpy=np.array(PIL_img, 'uint8')
    #获取图片人验特征
    faces = face_detector.detectMultiScale(img_numpy)
    # id = int(os.path.split(imagePath)[1].split('.')[0])
    for x, y, w, h in faces:
        labels.append(id)
        facesSamples.append(img_numpy[y:y+h, x:x+w])
        #打印脸部特征和1d
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(facesSamples,np.array(1))
    recognizer.write(facedata_path()+label+'.yml')

# 人脸比对
# names = []

#准备识别的图片
def face_detect(img):
    files = os.listdir(facedata_path())
    for file in files:
        file_path = os.path.join(facedata_path(), file)
        if os.path.isfile(file_path):
            recogizer = cv2.face.LBPHFaceRecognizer.create()
            print("file阿松大", file_path, img)
            recogizer.read(file_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 转换为灰度
            face_detector = cv2.CascadeClassifier(classifiers_path())
            face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
            for x,y, w, h in face:
                ids, confidence = recogizer.predict(gray[y: y+h, x: x+w])
                # print('标签id:',ids,'置信评分：'，confidence)
                if confidence < 80:
                    return file.join('.')[0], True

    return False



