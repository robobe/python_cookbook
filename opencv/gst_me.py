
import cv2

# gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-raw,width=640,height=480,framerate=20/1,format=\(fourcc\)YUY2 ! videoconvert ! fpsdisplaysink
# gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-raw,width=640,height=480,framerate=20/1 ! videoconvert ! video/x-raw,width=640,height=480,framerate=20/1,format=GRAY8 ! videoconvert ! fpsdisplaysink
# gst-launch-1.0 v4l2src device=/dev/video2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! fpsdisplaysink
# gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-h264,width=640,height=480,framerate=30/1 ! h264parse ! avdec_h264 ! videoconvert ! fpsdisplaysink

def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

tm = cv2.TickMeter()
gst_str = "v4l2src device=/dev/video2 ! video/x-raw,width=640,height=480,framerate=20/1 ! videoconvert ! video/x-raw,width=640,height=480,framerate=20/1,format=GRAY8 ! videoconvert ! appsink"
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
cap.set(cv2.CAP_PROP_CONVERT_RGB, False)

tm.start()
# print("Total frames number: {}".format(total_frame_count))

while True:
    tm.start()
    r, img = cap.read()
    if r == False:
        break
    tm.stop()
    print(tm.getTimeMilli())
    tm.reset()

    # cv2.imshow("Video", img)
    k = cv2.waitKey(1)
    
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()