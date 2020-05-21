import math
import cairo
import sys

# Import visualization functions
sys.path.insert(0, './../vis_classes')
from hexagons import *

if __name__ == '__main__':
    hex = Hexagons(512, 512)
    hex.execute_vis(6, "./../images/hexagons2")
