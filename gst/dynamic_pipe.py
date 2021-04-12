import gi
import threading
gi.require_version('Gst', '1.0')
from gi.repository import GLib, Gst


#Initializes the GStreamer library, setting up internal path lists, registering built-in elements, and loading standard plugins.
Gst.init(None)

class Main:
    def __init__(self):
        self.mainloop = GLib.MainLoop()
        #Creating the gst pipeline we're going to add elements to and use to play the file
        self.pipeline = Gst.Pipeline.new("mypipeline")

        #creating the filesrc element, and adding it to the pipeline
        self.filesrc = Gst.ElementFactory.make("filesrc", "filesrc")
        self.filesrc.set_property("location", "/tmp/gst/Big_Buck_Bunny_720_10s_1MB.mp4")
        self.pipeline.add(self.filesrc)
        
        #creating and adding the decodebin element , an "automagic" element able to configure itself to decode pretty much anything
        self.decode = Gst.ElementFactory.make("decodebin", "decode")
        self.pipeline.add(self.decode)
        #connecting the decoder's "pad-added" event to a handler: the decoder doesn't yet have an output pad (a source), it's created at runtime when the decoders starts receiving some data
        self.decode.connect("pad-added", self.decode_src_created) 
        
        self.conv = Gst.ElementFactory.make("videoconvert", "conv")
        self.pipeline.add(self.conv)

        #setting up (and adding) the alsasin, which is actually going to "play" the sound it receives
        self.tee = Gst.ElementFactory.make("tee", "tee")
        self.pipeline.add(self.tee)

        #linking elements one to another (here it's just the filesrc - > decoder link , the decoder -> sink link's going to be set up later)
        self.filesrc.link(self.decode)
        self.conv.link(self.tee)
            
    #handler taking care of linking the decoder's newly created source pad to the sink
    def decode_src_created(self, element, pad):
        print("pad add")
        caps = pad.get_current_caps()
        s = caps.get_structure(0)
        name = s.get_name()
        if "video/x-raw" == name:
            sinkpad = self.conv.get_static_pad("sink")
            if Gst.Pad.link(pad, sinkpad) != Gst.PadLinkReturn.OK:
                print("link bad")
                raise Exception()

            templ = self.tee.get_pad_template("src_%u")
            tee_pad = self.tee.request_pad(templ, None, None)
            queue = Gst.ElementFactory.make("queue")
            sink = Gst.ElementFactory.make("fakesink")
            sink.set_property("sync", True)
            self.pipeline.add(queue, sink)
            queue.link(sink)

            q_sinkpad = queue.get_static_pad("sink")
            Gst.Pad.link(tee_pad, q_sinkpad)
            # Gst.Object.unref(q_sinkpad)
            self.linked = True

            threading.Timer(3, self.timer_cb).start()

    def timer_cb(self):
        print("add")
        templ = self.tee.get_pad_template("src_%u")
        tee_pad = self.tee.request_pad(templ, None, None)
        queue = Gst.ElementFactory.make("queue")
        conv = Gst.ElementFactory.make("videoconvert")
        sink = Gst.ElementFactory.make("autovideosink")
        self.pipeline.add(queue, conv, sink)
        queue.link(conv)
        conv.link(sink)

        queue.sync_state_with_parent()
        conv.sync_state_with_parent()
        sink.sync_state_with_parent()

        q_sinkpad = queue.get_static_pad("sink")
        Gst.Pad.link(tee_pad, q_sinkpad)
        print("added")

    #running the shit
    def run(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        self.mainloop.run()

start=Main()
start.run()
