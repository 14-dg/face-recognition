import cv2


cap = cv2.VideoCapture("cars_on_road.mp4")

#Object detection from stable camera
objext_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    height, width, _ = frame.shape
    
    mask = objext_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ =cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    for cnt in contours:        
        #calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 80: 
            x, y, w, h = cv2.boundingRect(cnt)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (125, 0, 0), 3)
            cv2.drawContours(frame, [cnt], -1, (125, 125, 0), 2)

    cv2.imshow("FRAME", frame)
    #cv2.imshow("MASK", mask)
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()