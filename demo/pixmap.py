#!/usr/bin/python
# -*- coding: utf-8 -*-
import fitz

'''
Created on Fri Jan 08 17:00:00 2016

@author: Jorj X. McKie

===============================================================================
PyMuPDF demo program
--------------------
Demonstrates some of MuPDF's non-PDF graphic capabilities.

Read an image and create a new one consisting of 3 * 4 tiles of it.
===============================================================================
'''
# create pixmap from file
pix0 = fitz.Pixmap("editra.png")
# calculate target pixmap colorspace and dimensions and then create it
tar_cs     = pix0.getColorspace()
tar_width  = pix0.width * 3
tar_height = pix0.height * 4
tar_irect  = fitz.IRect(0, 0, tar_width, tar_height)
tar_pix    = fitz.Pixmap(tar_cs, tar_irect)
tar_pix.clearWith(90)        # clear target with a "very lively stone gray" (Loriot)

# now fill target with 3 * 4 tiles of input picture
for i in list(range(4)):
    pix0.y = i * pix0.height                          # modify input's y coord
    for j in list(range(3)):
        pix0.x = j * pix0.width                       # modify input's x coord
        tar_pix.copyPixmap(pix0, pix0.getIRect())     # copy input to new loc
        # save also intermediate images to show what is happening
        fn = "target-" + str(i) + str(j) + ".png"
        tar_pix.writePNG(fn)
