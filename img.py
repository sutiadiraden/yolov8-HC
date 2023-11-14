import cv2    
import time
cpt = 0
maxFrames = 500 # if you want 5 frames only.


cap=cv2.VideoCapture('derawan.mp4')
while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(1020,500))
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite(r'D:\yolov8-HC\test\coral_%d.jpg' %cpt, frame)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()