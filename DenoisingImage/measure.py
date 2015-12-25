#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from util import *

exec('from %s import denoise_image' % (sys.argv[1],))

train_dir = './train'
clean_dir = './train_cleaned'

answer = []
predict = []
for root, dirs, files in os.walk('./train'):
    for f in files:
        dirty_image = load_image(os.path.join(root, f))
        processed_image = denoise_image(dirty_image)
        clean_image = load_image(os.path.join(clean_dir, f))
        for (x,y), value in np.ndenumerate(processed_image):
            answer.append(value)
            predict.append(clean_image[x][y])

from sklearn.metrics import mean_squared_error
RMSE = mean_squared_error(answer, predict)**0.5
print 'RMSE:', RMSE

