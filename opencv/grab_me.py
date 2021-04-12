import numpy as np
import cv2 as cv
import time

def main():
    tm = cv.TickMeter()
    def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

    font = cv.FONT_HERSHEY_SIMPLEX
    color = (0, 255, 0)

    cap = cv.VideoCapture("/dev/video2")
    cap.set(cv.CAP_PROP_AUTOFOCUS, False)  # Known bug: https://github.com/opencv/opencv/pull/5474
    cap.set(cv.CAP_PROP_FPS, 20)
    cv.namedWindow("Video")

    convert_rgb = True
    fps = int(cap.get(cv.CAP_PROP_FPS))
    focus = int(min(cap.get(cv.CAP_PROP_FOCUS) * 100, 2**31-1))  # ceil focus to C_LONG as Python3 int can go to +inf

    # cv.createTrackbar("FPS", "Video", fps, 10, lambda v: cap.set(cv.CAP_PROP_FPS, v))
    # cv.createTrackbar("Focus", "Video", focus, 100, lambda v: cap.set(cv.CAP_PROP_FOCUS, v / 100))
    #codec = 0x47504A4D # MJPG
    codec = 844715353.0 # YUY2
    #codec = 1196444237.0 # MJPG

    #print 'fourcc:', decode_fourcc(codec)
    cap.set(cv.CAP_PROP_FOURCC, codec)
    while True:
        tm.start()
        #status, img = cap.read()
        status, img = cap.retrieve(cap.grab())
        cap.grab()
        fourcc = decode_fourcc(cap.get(cv.CAP_PROP_FOURCC))

        fps = cap.get(cv.CAP_PROP_FPS)

        if not bool(cap.get(cv.CAP_PROP_CONVERT_RGB)):
            if fourcc == "MJPG":
                img = cv.imdecode(img, cv.IMREAD_GRAYSCALE)
            elif fourcc == "YUYV":
                img = cv.cvtColor(img, cv.COLOR_YUV2GRAY_YUYV)
            else:
                print("unsupported format")
                break

        cv.putText(img, "Mode: {}".format(fourcc), (15, 40), font, 1.0, color)
        cv.putText(img, "FPS: {}".format(fps), (15, 80), font, 1.0, color)
        tm.stop()
        print(tm.getTimeMilli())
        tm.reset()
        cv.imshow("Video", img)
        k = cv.waitKey(1)
        
        if k == 27:
            break
        elif k == ord('g'):
            convert_rgb = not convert_rgb
            cap.set(cv.CAP_PROP_CONVERT_RGB, convert_rgb)

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
