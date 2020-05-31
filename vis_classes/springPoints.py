#!/usr/bin/env python

import math
import cairo

import sys

# Import utility function
sys.path.insert(0, './../utils')
from image_utils import *

class SpringPoints:
    def __init__(self, width, height):
        self.surface, self.ctx = new_context(width, height)

        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.set_source_rgb(0.0, 0.0, 0.0)
        self.ctx.fill()

    def execute_vis(self, num_steps, filename_base):
        dt = 0.001
        fac = 1.0
        r = 0.4

        dt2 = dt**2

        x_offset = 0.5
        y_offset = 0.5

        # pt0
        x0_0 = -0.1
        y0_0 = 0.0
        vx0_0 = 0.0
        vy0_0 = 0.0

        # pt1
        x0_1 = 0.1
        y0_1 = 0.0
        vx0_1 = 0.0
        vy0_1 = 0.0

        # temp variables
        x0_temp = 0.0
        y0_temp = 0.0
        vx_temp = 0.0
        vy_temp = 0.0

        for j in range(0, num_steps):
            dx = abs(x0_1 - x0_0)
            x1_0 = 0.5*fac*dt2*(r - dx) + vx_0*dt + x0_0
            vx1_0 = vx0_0 + fac*(r - 0.5*(x1_0 + x0_0))
            x0_0 = x1_0
            vx0_0 = vx1_0

            self.ctx.arc(x + x_offset, 0.0 + y_offset, 0.01, 0.0, 2.0*math.pi)
            self.ctx.set_source_rgb(0.0, 1.0, 0.0)
            self.ctx.set_line_width(0.05)
            #self.ctx.stroke()
            self.ctx.fill()

            save_canvas(self.surface, filename_base, j)
