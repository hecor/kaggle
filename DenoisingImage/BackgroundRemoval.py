#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple background removal code

__author__ : Rangel Dokov

The basic idea is that we have a foreground object of interest (the dark text)
and we want to remove everything that is not part of this foreground object.

This should produce results somewhere around 0.06 on the leaderboard.
"""

import numpy as np
from scipy import signal


def denoise_image(inp):
    # estimate 'background' color by a median filter
    bg = signal.medfilt2d(inp, 11)
#    save('background.png', bg)

    # compute 'foreground' mask as anything that is significantly darker than
    # the background
    mask = inp < bg - 0.1
#    save('foreground_mask.png', mask)

    # return the input value for all pixels in the mask or pure white otherwise
    return np.where(mask, inp, 1.0)

