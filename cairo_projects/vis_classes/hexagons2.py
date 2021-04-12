#!/usr/bin/env python

import math
import cairo

import sys

# Import utility function
sys.path.insert(0, './../utils')
from image_utils import *

class Hexagons2:
    def __init__(self, width, height):
        self.surface, self.ctx = new_context(width, height)

        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.set_source_rgb(0.0, 0.0, 0.0)
        self.ctx.fill()

    def execute_vis(self, num_steps, filename_base):
        x_offset = 0.5
        y_offset = 0.5

        for j in range(0, num_steps):
            x = 0.1 + x_offset
            y = 0.1 + y_offset
            self.ctx.arc(x, y, 0.001, 0.0, 2.0*math.pi)
            self.ctx.set_source_rgb(0.0, 1.0, 0.0)
            self.ctx.set_line_width(0.05)
            #self.ctx.stroke()
            self.ctx.fill()

            save_canvas(self.surface, filename_base, j)
