from samplebase import SampleBase
import time


class PixelArt(SampleBase):
    def __init__(self, data, **kwargs):
        super(PixelArt, self).__init__(data, **kwargs)
        self.data = data

    def run(self):
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()

        while True:
            self.offscreen_canvas.Clear()
            for i in self.data:
                i = i.split(", ")
                self.offscreen_canvas.SetPixel(int(i[0]), int(
                    i[1]), int(i[2]), int(i[3]), int(i[4]))

            time.sleep(0.05)
            self.offscreen_canvas = self.matrix.SwapOnVSync(
                self.offscreen_canvas)
