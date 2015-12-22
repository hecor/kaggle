#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from BackgroundRemoval import denoise_image

out = open('submission.csv', 'w')

for root, dirs, files in os.walk('./test'):
    for f in files:
        dirty_image = os.path.join(root, f)
        print 'processing', dirty_image
        clean_image = denoise_image(dirty_image)
        print clean_image[0][0]

