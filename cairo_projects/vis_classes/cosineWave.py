#!/usr/bin/env python

import math
import cairo

import sys

# Import utility function
sys.path.insert(0, './../utils')
from image_utils import *

class CosineWave:
    def __init__(self, width, height):
        self.surface, self.ctx = new_context(width, height)

        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.set_source_rgb(0.0, 0.0, 0.0)
        self.ctx.fill()

    def execute_vis(self, num_steps, filename_base):
        x_offset = 0.5
        y_offset = 0.5

        x0 = -0.5 + x_offset
        y0 = 0.0 + y_offset

        scale = 0.25

        self.ctx.move_to(x0, 0.25 + y0)

        for i in range(0, 129):
            x = x0 + i*1.0/128
            y = scale*math.cos(2.0 * math.pi * x) + y0
            self.ctx.line_to(x, y)

        self.ctx.set_source_rgb(0.0, 1.0, 0.0)
        self.ctx.set_line_width(0.002)
        self.ctx.stroke()

        self.ctx.move_to(x0, y0)

        for i in range(0, 128):
            x = x0 + i*1.0/128
            y = y0
            self.ctx.line_to(x, y)

        self.ctx.set_source_rgb(1.0, 0.0, 0.0)
        self.ctx.set_line_width(0.002)
        self.ctx.stroke()

        save_canvas(self.surface, filename_base, 0)
