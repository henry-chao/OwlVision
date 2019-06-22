import wx
import cv2 as cv
from app.WebCam import WebCam


class OwlFrame(wx.Frame):

    def __init__(self):
        style = wx.STAY_ON_TOP | wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.CAPTION
        super(OwlFrame, self).__init__(None, title="OwlFrame", style=style)
        self.pnl = wx.Panel(self)

        self.webcam = WebCam()
        if not self.webcam.has_webcam():
            print("No webcam found")
            self.close()

        height, width = self.webcam.size()
        self.SetSize(wx.Size(width, height))

        # Set 30 fps for video
        self.timer = wx.Timer(self)
        self.timer.Start(1000./30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.updating = False

        self.pnl.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.pnl.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        self.timer.Stop()
        self.Destroy()

    def onUpdate(self, event):
        self.Refresh()

    def onPaint(self, event):
        frame_w, frame_h = self.pnl.GetSize()
        frame = self.webcam.get_image(frame_w, frame_h)
        h, w = frame.shape[:2]
        image = wx.BitmapFromBuffer(w, h, frame)

        # Buffer the image
        dc = wx.BufferedPaintDC(self.pnl)
        dc.DrawBitmap(image, 0, 0)

    # Avoid flickering
    def onEraseBackground(self, event):
        return
