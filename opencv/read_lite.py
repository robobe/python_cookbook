
import cv2


tm = cv2.TickMeter()

cap = cv2.VideoCapture("/dev/video2")
cap.set(cv2.CAP_PROP_FPS, 20)
fps = int(cap.get(cv2.CAP_PROP_FPS))
cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
#codec = 844715353.0 # YUY2
codec = 1196444237.0 # MJPG
cap.set(cv2.CAP_PROP_FOURCC, codec)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height =  cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"W:{width}, H:{height},FPS:{fps}")
tm.start()
while True:
    tm.start()
    r, img = cap.read()
    if r == False:
        break
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)

    tm.stop()
    print(tm.getTimeMilli())
    tm.reset()
    cv2.imshow("Video", img)
    k = cv2.waitKey(1)
    
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
