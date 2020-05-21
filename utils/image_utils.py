import cairo

def save_canvas(surface, filename, index):
    if( index < 10 ):
        padding = "000"
    if( index > 9 and j < 100):
        padding = "00"
    if( index > 99 and j < 1000):
        padding = "0"
    if( index > 999 ):
        padding = ""

    surface.write_to_png(filename + "_" + padding + str(index) + ".png")

def new_context( width, height ):
    width, height = 512, 512

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(width, height)

    return surface, ctx
