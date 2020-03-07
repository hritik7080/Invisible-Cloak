import cv2

cap = cv2.VideoCapture('./WhatsApp Video 2020-03-07 at 2.29.46 PM (3).mp4')

while cap.isOpened():
    ret, back = cap.read()
    if ret==True:
        # back = cv2.rotate(back, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("image6.jpg", back)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.imwrite('image7.jpg', back)
            break
    # if cv2.waitKey('q') % 0xFF == ord('q'):
    else:
        break

cap.release()
cv2.destroyAllWindows()

