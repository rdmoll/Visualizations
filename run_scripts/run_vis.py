import math
import cairo
import sys

# Import visualization functions
sys.path.insert(0, './../vis_classes')
from hexagons import *
from hexagons2 import *
from cosineWave import *
from gradientDescent import *

if __name__ == '__main__':
    vis_string = str(sys.argv[1])
    print("Running visualization: " + vis_string)
    if vis_string == "grad":
        gradDes = GradientDescent(512, 512)
        gradDes.execute_vis(200, "./../images/grad")
