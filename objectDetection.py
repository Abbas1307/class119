import cv2
import time
import math

video =cv2.VideoCapture("bb3.mp4")

# 1. loading tracker
tracker=cv2.TrackerCSRT_create()

# 2. read the first frame of the video
returned,img= video.read()

# 3. select the bounding box on the image(roi region of interset) 
bbox=cv2.selectROI("tracker",img,False)

# 4. Intilize the tracker on the image and the bbox
tracker.init(img,bbox)

print("what is bbox: ",bbox)

def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),3,1)

while True:
    dummy,img= video.read()

    # 5. update the tracker on the image and bbox
    success,bbox=tracker.update(img)
    
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost the tracker",(200,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    cv2.imshow("result",img)

    key=cv2.waitKey(25)

    if key ==32:
        print("stopped")
        break

video.release()
cv2.destroyAllWindows()

 
 


