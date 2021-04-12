#!/usr/bin/env python3

import cv2
import gi
import traceback

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)

pipe = "videotestsrc name=src num-buffers=100 ! video/x-raw,width=640,height=480 ! autovideosink name=sink"
pipeline = Gst.parse_launch(pipe)
#  Start playing 
pipeline.set_state(Gst.State.PLAYING)

# wait for EOS or error
bus = pipeline.get_bus()

msg = bus.timed_pop_filtered(
    Gst.CLOCK_TIME_NONE,
    Gst.MessageType.ERROR | Gst.MessageType.EOS
)

pipeline.set_state(Gst.State.NULL)