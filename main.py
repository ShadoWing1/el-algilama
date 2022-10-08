import cv2
"""         bilgisayarin kamerasi için            """
from cvzone.HandTrackingModule import HandDetector
kamera = cv2.VideoCapture(0)
detector = HandDetector()
while True:
    ret,kare=kamera.read()
    kare =cv2.flip(kare,1)
    hands,kare=detector.findHands(kare,flipType=False)
    cv2.imshow("kamera",kare)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()




"""
img = cv2.imread("a.jpeg")
s = 60
img= cv2.resize(img, (9*s, 16*s))   
hands,img=detector.findHands(img)
                                            secili fotoğraflar icin
cv2.imshow("Resim",img)

cv2.waitKey(0)
cv2.destrolAllWindows()"""