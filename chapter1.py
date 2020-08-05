import cv2

print(" package imported")


# img = cv2.imread('lena.jpg', -1)
cap = cv2.VideoCapture(0)
#widthidis-3
cap.set(3,680)
#heightidis-4
cap.set(4,480)
#brightnessidis-(10,brightness)
cap.set(10,10000)

# cv2.imshow('image', img)
# cv2.waitKey(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
