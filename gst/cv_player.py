"""
https://www.ardusub.com/developers/opencv.html
https://gist.github.com/patrickelectric/443645bb0fd6e71b34c504d20d475d5a
"""
# cap = cv2.VideoCapture("rtsp://192.168.2.253:8554/test", cv2.CAP_FFMPEG)

out_pipe = 'appsrc ! queue ! videoconvert \
    ! video/x-raw,width=320, heigh=240 ! omxh264enc ! video/x-h264 \
    ! h264parse \
    ! rtph264pay \
    ! udpsink host=127.0.0.1 port=5600 sync=false'

out_pipe = "appsrc ! \
 video/x-raw,width=640,height=480 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
 udpsink host=127.0.0.1 port=5600"

in_pipe = "/dev/video2"
in_pipe = "videotestsrc ! video/x-raw,width=640,height=480,format=YUY2 ! videoconvert ! appsink"

import cv2

cap = cv2.VideoCapture(in_pipe, cv2.CAP_GSTREAMER)
out = cv2.VideoWriter(out_pipe,cv2.CAP_GSTREAMER, 0,25.0,(640,480), True)
while True:
    ret, frame = cap.read()
    out.write(frame)
    # cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()