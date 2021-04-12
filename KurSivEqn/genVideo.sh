#!/bin/sh

#mv screen-0* frames
ffmpeg -r 10 -i ./frames/screen-%04d.tif -crf 20 -pix_fmt yuv420p out.mp4
#ffmpeg -r 30 -i screen-%04d.tif -crf 10 -pix_fmt yuv420p out.mp4
