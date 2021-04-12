import cv2

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (200,200)
fontScale              = 2
fontColor              = (255,0,0)
lineType               = 2

cap = cv2.VideoCapture("videotestsrc ! video/x-raw,width=640,height=480,framerate=10/1 ! videoconvert ! timeoverlay ! appsink")
out_pipe = "appsrc ! video/x-raw,width=640,height=480,framerate=10/1 ! videoconvert ! timeoverlay xpad=100 ypad=100 ! x264enc ! \
 rtph264pay ! \
 udpsink host=127.0.0.1 port=5600"
out = cv2.VideoWriter(out_pipe, 0, 10.0, (640,480))

while True:
    ret, frame = cap.read()
    cv2.imshow("cv", frame)
    cv2.putText(frame,'Hello World!', 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    out.write(frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
