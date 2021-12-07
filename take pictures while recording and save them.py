import cv2
 
# Opens the Video file
cap= cv2.VideoCapture(0)
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite("images/Aaron/"+str(i)+'.jpg',frame) #pfad eingeben 
    i+=1
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()