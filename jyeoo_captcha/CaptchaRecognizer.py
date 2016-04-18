#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
import numpy as np
from scipy.spatial.distance import cosine

class CaptchaRecognizer:
    def __init__(self, trainingicons_dirpath):
        digits_iconset =  ['1','2','3','4','5','6','7','8','9']
        operators_iconet = ['+', '-']
        self.digits_trainingset = self.load_trainingset(trainingicons_dirpath, digits_iconset)
        self.operators_trainingset = self.load_trainingset(trainingicons_dirpath, operators_iconet)
        self.xlen = 10
        self.ylen = 8

    def _similarity(self, v1, v2):
        return 1 - cosine(v1, v2)

    def buildvector(self, im):
        im = im.convert("L")
        return np.array(im, dtype=int).flatten()

    def load_trainingset(self, dirpath, iconset):
        trainingset = {}
        for s in iconset:
            trainingset[s] = []
        for imageName in os.listdir(dirpath):
            if imageName[0] in iconset and imageName[-3:] == "png":
                trainingset[imageName[0]].append(self.buildvector(Image.open(os.path.join(dirpath, imageName))))

        return trainingset

    def recognize_char(self, im, trainingset):
        guess = []
        imv = im.flatten()
        for c in trainingset.keys():
            vs = trainingset[c]
            for v in vs:
                guess.append( (self._similarity(v, imv), c) )
        guess.sort(reverse=True)
        return guess[0][1]

    def recognize_digit(self, im):
        return self.recognize_char(im, self.digits_trainingset)

    def recognize_operator(self, im):
        return self.recognize_char(im, self.operators_trainingset)

    def recognize_captcha(self, imageName):
        im = Image.open(imageName)
        im = np.array(im.convert("L"), dtype=int)

        s = ''
        digits, operators = self.extract_icons(im)
        for d in digits:
            s += self.recognize_digit(d)
        for o in operators:
            s += self.recognize_operator(o)
        
        s = s[0]+s[3]+s[1]+s[4]+s[2]
        print(s)
        return eval(s)

    def computeDensity(self, img, x, y):
        if x+self.xlen >= img.shape[0] or y+self.ylen >= img.shape[1]:
            return 255
        return np.average(img[x:x+self.xlen, y:y+self.ylen])

    def extract_icons(self, img):
        sub_img = img[:, 5:120]
        all_desity = []
        for (x, y), e in np.ndenumerate(sub_img):
            d = self.computeDensity(sub_img, x, y)
            all_desity.append((d, x, y))

        already_used = []
        candidates = []
        for k in sorted(all_desity, key=lambda k:k[0]):
            if k[2] in already_used:
                continue
            for i in range(-10, 15):
                already_used.append(k[2]+i)
            if len(candidates) < 5:
                candidates.append(k)

        digits = []
        for k in sorted(candidates[:3], key=lambda k:k[2]):
            # print(k)
            digits.append(sub_img[k[1]:k[1]+self.xlen, k[2]:k[2]+self.ylen])

        operators = []
        for k in sorted(candidates[3:], key=lambda k:k[2]):
            # print(k)
            operators.append(sub_img[k[1]:k[1]+self.xlen, k[2]:k[2]+self.ylen])

        return digits, operators


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print('usage: ./*** filename')
        sys.exit(-1)

    cr = CaptchaRecognizer('./training_icons')
    print(cr.recognize_captcha(sys.argv[1]))

