#!/usr/bin/env python

import math
import numpy as np
import cairo

import sys

# Import utility function
sys.path.insert(0, './../utils')
from image_utils import *

class GradientDescent:
    def __init__(self, width, height):
        self.surface, self.ctx = new_context(width, height)

        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.set_source_rgb(0.0, 0.0, 0.0)
        self.ctx.fill()

        self.facX = 2.0 * np.pi
        self.facY = 2.0 * np.pi

    def calc_dzdx(self, x, y, xInd, yInd, coeffs):

        dzdx = 0.0
        for i in yInd:
            for j in xInd:
                dzdx = dzdx - coeffs[i - 1][j - 1]*self.facX*np.cos(yInd[i - 1] * self.facY * y)*np.sin(xInd[j - 1] * self.facX * x)

        return dzdx

    def calc_dzdy(self, x, y, xInd, yInd, coeffs):

        dzdy = 0.0
        for i in yInd:
            for j in xInd:
                dzdy = dzdy - coeffs[i - 1][j - 1]*self.facY*np.sin(yInd[i - 1] * self.facY * y)*np.cos(xInd[j - 1] * self.facX * x)

        return dzdy

    def execute_vis(self, num_steps, filename_base):

        num_streams = 50
        nx = 16
        ny = 4

        coeffs = [ [ np.random.rand() for j in range(1, nx) ] for i in range(1, ny) ]

        xArr = [ [ 0.0 for j in range(0, num_streams) ] for i in range(0, num_steps + 1) ]
        yArr = [ [ 0.0 for j in range(0, num_streams) ] for i in range(0, num_steps + 1) ]

        #for i in range(0, 25):
        #    xArr[0][i] = 0.05 + 0.008*i

        #for i in range(25, num_streams):
        #    xArr[0][i] = 0.55 + 0.008*i

        for i in range(0, num_streams):
            xArr[0][i] = 0.30 + 0.008*i

        xInd = np.arange(1, nx)
        yInd = np.arange(1, ny)

        for j in range(0, num_steps):
            self.ctx.rectangle(0, 0, 1, 1)
            self.ctx.set_source_rgb(0.0, 0.0, 0.0)
            self.ctx.fill()

            for k in range(0, num_streams):
                dzdx = self.calc_dzdx(xArr[j][k], yArr[j][k], xInd, yInd, coeffs) - 25.0*(2.0*xArr[j][k] - 1.0)
                dzdy = self.calc_dzdy(xArr[j][k], yArr[j][k], xInd, yInd, coeffs) - 40.0*(1.0 - yArr[j][k]) - 20

                x = xArr[j][k] - 0.0002*dzdx
                y = yArr[j][k] - 0.0002*dzdy

                xArr[j + 1][k] = x
                yArr[j + 1][k] = y

                self.ctx.move_to(xArr[0][k], yArr[0][k])
                for i in range(0, j + 1):
                    self.ctx.line_to(xArr[i][k], yArr[i][k])

            self.ctx.set_source_rgb(1.0-yArr[j][k], 0.0, yArr[j][k])
            self.ctx.set_line_width(0.0025)
            self.ctx.stroke()

            if (yArr[j + 1][k] > 1.0):
                break

            save_canvas(self.surface, filename_base, j)
