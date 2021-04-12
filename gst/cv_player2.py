import cv2

# Camera device
in_pipe = "/dev/video2"
# Test source
in_pipe = "videotestsrc pattern=ball ! video/x-raw,width=640,height=480,format=YUY2 ! videoconvert ! appsink"

out_pipe = "appsrc ! \
 video/x-raw,width=640,height=480 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
 udpsink host=127.0.0.1 port=5600"

out_pipe = "appsrc ! \
 video/x-raw,width=640,height=480 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
 udpsink host=224.1.1.1 auto-multicast=true port=5600"

cap = cv2.VideoCapture(in_pipe, cv2.CAP_GSTREAMER)
out = cv2.VideoWriter(out_pipe,cv2.CAP_GSTREAMER, 0,30.0,(640,480), True)
while True:
    ret, frame = cap.read()
    out.write(frame)
    # cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

"""
gst-launch-1.0 \
videotestsrc ! \
video/x-raw,width=640,height=480,format=YUY2 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
udpsink host=224.1.1.1 auto-multicast=true port=5600
"""