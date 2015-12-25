#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
from sklearn.linear_model import LinearRegression
from util import *
from matplotlib.pyplot import plot


def denoise_image(inp):
    for (x,y), value in np.ndenumerate(inp):
        inp[x][y] = model.predict(value)

    return inp
    

def train_model():
    print 'training model...'
    train_dir = './train'
    train_cleaned_dir = './train_cleaned'
    X = []
    Y = []
    for f in os.listdir(train_dir):
        dirty_image = load_image(os.path.join(train_dir, f))
        clean_image = load_image(os.path.join(train_cleaned_dir, f))
        for (x,y), value in np.ndenumerate(dirty_image):
            X.append([value,])
            Y.append(clean_image[x][y])

    plot(X, Y)
    model.fit(X, Y)


model = LinearRegression()
train_model()

