#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image

def load_image(path):
    return np.asarray(Image.open(path))/255.0

def save(path, img):
    tmp = np.asarray(img*255.0, dtype=np.uint8)
    Image.fromarray(tmp).save(path)
