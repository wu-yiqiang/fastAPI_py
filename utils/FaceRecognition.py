import cv2 as cv
def DetectFaces():
    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    detect_face = cv.CascadeClassifier('/Users/atlas/fastAPI_py/.venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = detect_face.detectMultiScale(grey_img, 1.01, 5,0,(100,100),(300, 300))
    for (x, y, w, h) in face:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('result', img)


img = cv.imread('../images/face1.jpg')
DetectFaces()

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()

