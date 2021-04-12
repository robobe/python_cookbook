#!/usr/bin/env python3

import cv2
import gi
import traceback

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

play = False

def on_message(bus: Gst.Bus, message: Gst.Message, loop: GLib.MainLoop):
    mtype = message.type
    
    if mtype == Gst.MessageType.EOS: 
        # Handle End of Stream 
        print("End of stream") 
        loop.quit()
    elif mtype == Gst.MessageType.ERROR: 
        # Handle Errors 
        err, debug = message.parse_error() 
        print(err, debug) 
        loop.quit()
    elif mtype == Gst.MessageType.WARNING: 
        # Handle warnings 
        err, debug = message.parse_warning() 
        print(err, debug) 
    elif mtype == Gst.MessageType.STATE_CHANGED:
        old_state, new_state, pending_state = message.parse_state_changed()
        print(message.src)
    return True

Gst.init(None)

pipe = "videotestsrc name=src num-buffers=20 ! video/x-raw,width=640,height=480 ! autovideosink name=sink"
pipeline = Gst.parse_launch(pipe)
#  Start playing 
pipeline.set_state(Gst.State.PLAYING)

bus = pipeline.get_bus()
bus.add_signal_watch()

loop = GLib.MainLoop()
bus.connect('message', on_message, loop)

try:
    loop.run()
except KeyboardInterrupt:
    pass


pipeline.set_state(Gst.State.NULL)


