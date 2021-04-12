#!/usr/bin/env python3

import cv2
import gi
import traceback

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

# def on_new_buffer(sink):
#     try:
#         # A datatype to hold a time, measured in nanoseconds.
#         print(sink.clock.get_internal_time())
#     except Exception as e:
#         print('ERROR', traceback.format_exc())

#     return Gst.FlowReturn.OK

Gst.init(None)

pipe = "videotestsrc name=src num-buffers=100 ! video/x-raw,width=640,height=480 ! autovideosink name=sink"
pipeline = Gst.parse_launch(pipe)
# Add for debug / dot file
Gst.debug_bin_to_dot_file(pipeline, Gst.DebugGraphDetails.ALL, "debug_pipe")
# sink = pipeline.get_by_name('sink')
# sink.set_property("max-buffers",2)
# sink.set_property("emit-signals", True)
# sink.connect("new-sample", on_new_buffer)

pipeline.set_state(Gst.State.READY)
pipeline.set_state(Gst.State.PLAYING)

loop = GLib.MainLoop()
loop.run()



