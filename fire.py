import cv2
import numpy as np 
import matplotlib.pyplot as plt
livecam=cv2.VideoCapture(0)
lowb=np.array([11,33,111])
upperb=np.array([90,255,255])
while(livecam.isOpened()):
    ret,frm=livecam.read()
    frm=cv2.resize(frm,(1280,720))
    frm=cv2.flip(frm,1)
    frmsmoo=cv2.GaussianBlur(frm,(7,7),0)
    mask=np.zeros_like(frm)
    mask[0:720,0:1280]=[255,255,255]
    img_r=cv2.bitwise_and(frmsmoo,mask)
    frm_hs=cv2.cvtColor(img_r,cv2.COLOR_BGR2HSV)
    img_bin=cv2.inRange(frm_hs,lowb,upperb)
    check=cv2.countNonZero(img_bin)
    if int(check)>=20000:
        cv2.putText(frm,"fire deteced!",(300,60),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),2)
    cv2.imshow("fire detection",frm)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    imgrgb=cv2.cvtcolor(frm,cv2.COLOR_BGR2RGB)
    imgcap=plt.imshow(imgrgb)
    plt.show()
livecam.release()
cv2.destroyAllWindows()
