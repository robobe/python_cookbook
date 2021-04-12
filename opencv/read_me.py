
import cv2

def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

tm = cv2.TickMeter()

cap = cv2.VideoCapture("/dev/video2")
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)
cap.set(cv2.CAP_PROP_FPS, 20)
fps = int(cap.get(cv2.CAP_PROP_FPS))
cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
codec = 844715353.0 # YUY2
#codec = 1196444237.0 # MJPG
cap.set(cv2.CAP_PROP_FOURCC, codec)
fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height =  cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

tm.start()
while True:
    tm.start()
    r, img = cap.read()
    if r == False:
        break
    tm.stop()
    print(tm.getTimeMilli())
    tm.reset()
    cv2.putText(img, "Mode: {}".format(fourcc), (15, 40), font, 1.0, color)
    cv2.putText(img, "FPS: {}".format(fps), (15, 80), font, 1.0, color)
    cv2.putText(img, "Width: {}".format(width), (15, 120), font, 1.0, color)
    cv2.putText(img, "Height: {}".format(height), (15, 160), font, 1.0, color)
    img = cv2.cvtColor(img, cv2.COLOR_YUV2GRAY_YUYV)
    # img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_YUYV)
    # img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow("Video", img)
    k = cv2.waitKey(1)
    
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


#capture.py
# import cv2
# cap = cv2.VideoCapture(“/dev/video0”)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
# cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
# code, frame = cap.read()