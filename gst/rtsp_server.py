#!/usr/bin/env python

"""
udp test
gst-launch-1.0 videotestsrc ! video/x-raw,width=640,height=480,format=YUY2 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
 udpsink host=127.0.0.1 port=5600


gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-raw,width=640,height=480 ! \
 videoconvert ! \
 x264enc ! \
 h264parse ! \
 rtph264pay ! \
 udpsink host=127.0.0.1 port=5600

gst-launch-1.0 playbin uri=rtsp://localhost:8554/test
or
gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/test \
	! queue \
	! rtph264depay \
	! h264parse \
	! avdec_h264 \
	! videoconvert \
	! videoscale \
	! video/x-raw,width=640,height=480 \
	! autovideosink

gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/test \
	! queue \
	! rtph264depay \
	! h264parse \
	! avdec_h264 \
	! videoconvert \
	! videoscale \
	! video/x-raw,width=640,height=480 \
	! videoconvert \
	! x264enc \
	! rtph264pay \
	! udpsink host=127.0.0.1 port=5600
"""

import sys
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GLib, Gst, GstRtspServer, GObject

loop = GLib.MainLoop ()
Gst.init(None)

class MyFactory(GstRtspServer.RTSPMediaFactory):
	def __init__(self):
		GstRtspServer.RTSPMediaFactory.__init__(self)

	def do_create_element(self, url):
		# s_src = "v4l2src device=/dev/video2 ! video/x-raw,rate=30,width=640,height=480 ! videoconvert"
		s_src = "videotestsrc ! video/x-raw,width=640,height=480,format=YUY2 ! videoconvert"
		s_h264 = "x264enc tune=zerolatency"
		pipeline_str = "( {s_src} ! queue max-size-buffers=1 name=q_enc ! {s_h264} ! rtph264pay name=pay0 pt=96 )".format(**locals())
		print(pipeline_str)
		return Gst.parse_launch(pipeline_str)

class GstServer():
	def __init__(self):
		self.server = GstRtspServer.RTSPServer()
		f = MyFactory()
		f.set_shared(True)
		m = self.server.get_mount_points()
		m.add_factory("/test", f)
		self.server.attach(None)

if __name__ == '__main__':
	s = GstServer()
	loop.run()