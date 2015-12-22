#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

out = open('submission.txt', 'w')

for root, dirs, files in os.walk('./test'):
    for f in files:
        dirty_image = os.path.join(root, f)
        clean_image = denoise_image(dirty_image)

