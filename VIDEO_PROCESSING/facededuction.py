import cv2
cap = cv2.VideoCapture(0)
classifire=cv2.CascadeClassifier('frontalface.xml')

while True :

    ret,frame = cap.read()
    faces =classifire.detectMultiScale(frame)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),2)
    #print(frame)
    cv2.imshow('reading webcam',frame)
    
    if cv2.waitKey(100) & 0xff == ord('q'):
         break

cv2.destroyAllWindows()
cap.release()