#!/usr/bin/env python

import math
import cairo

import sys

# Import utility function
sys.path.insert(0, './../utils')
from image_utils import *

class Hexagons:
    def __init__(self, width, height):
        self.surface, self.ctx = new_context(width, height)

        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.set_source_rgb(0.0, 0.0, 0.0)
        self.ctx.fill()

    def execute_vis(self, num_steps, filename_base):
        x_offset = 0.5
        y_offset = 0.5

        scale = 0.2
        dtheta = 0.05

        for j in range(0, num_steps):
            self.ctx.rectangle(0, 0, 1, 1)
            self.ctx.set_source_rgb(0.0, 0.0, 0.0)
            self.ctx.fill()

            x = scale*math.cos((5.0 + dtheta*j) * math.pi / 3.0) + x_offset
            y = scale*math.sin((5.0 + dtheta*j) * math.pi / 3.0) + y_offset
            self.ctx.move_to(x, y)

            for i in range(0, 6):
                x = scale*math.cos((1.0*i + dtheta*j) * math.pi / 3.0) + x_offset
                y = scale*math.sin((1.0*i + dtheta*j) * math.pi / 3.0) + y_offset
                self.ctx.line_to(x, y)

            self.ctx.set_source_rgb(0.0, 1.0, 0.0)
            self.ctx.set_line_width(0.002)
            self.ctx.stroke()

            save_canvas(self.surface, filename_base, j)
