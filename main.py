import cv2 as q
"""         bilgisayarin kamerasi için            """
from cvzone.HandTrackingModule import HandDetector
kamera = q.VideoCapture(0)
detector = HandDetector()
c = input("c/b: ")
if(c == "c"):
    while True:
        ret,kare=kamera.read()
        kare =q.flip(kare,1)
        hands,kare=detector.findHands(kare,flipType=False)
        q.imshow("kamera",kare)
        if q.waitKey(1) & 0xFF == ord("q"):
            break
    kamera.release()
    q.destroyAllWindows()




elif(c == "b"):
    img = q.imread("a.jpeg")
    s = 60
    img= q.resize(img, (9*s, 16*s))   
    hands,img=detector.findHands(img)
    """                                            secili fotoğraflar icin"""
    q.imshow("Resim",img)

    q.waitKey(0)
    q.destrolAllWindows()