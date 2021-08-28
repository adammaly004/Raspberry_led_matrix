from samplebase import SampleBase
import time
from rgbmatrix import graphics


class PixelArt(SampleBase):
    def __init__(self, data, **kwargs):
        super(PixelArt, self).__init__(data, **kwargs)
        self.data = data

    def run(self):
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()

        self.offscreen_canvas.Clear()
        for i in self.data:
            i = i.split(", ")
            self.offscreen_canvas.SetPixel(int(i[0]), int(
                i[1]), int(i[2]), int(i[3]), int(i[4]))

        for _ in range(1000):
            self.offscreen_canvas = self.matrix.SwapOnVSync(
                self.offscreen_canvas)
            # time.sleep(0.05)


class RunText(SampleBase):
    def __init__(self, text, color, **kwargs):
        super(RunText, self).__init__(text, color, **kwargs)
        self.text = text
        self.color = color

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        font = graphics.Font()
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

        font2 = graphics.Font()
        font2.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13O.bdf")

        color = graphics.Color(self.color[0], self.color[1], self.color[2])
        position = offscreen_canvas.width

        while True:

            offscreen_canvas.Clear()

            length = graphics.DrawText(
                offscreen_canvas, font, position, 20, color, self.text)

            position -= 1
            if (position + length < 0):
                break

            time.sleep(0.05)

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
