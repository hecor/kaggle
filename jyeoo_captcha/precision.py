#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CaptchaRecognizer import *
from datetime import datetime
import os

print(datetime.now())

total = 0.0
correct = 0

cr = CaptchaRecognizer('./training_icons')
for f in os.listdir('./cases'):
    try:
        v = int(f.strip('.png').split('_')[1])
    except:
        continue
    total += 1
    if cr.recognize_captcha(os.path.join('./cases', f)) == v:
        correct += 1
        print('correct: %s, total: %s' % (correct, total))
        

print('correct: %s, total: %s' % (correct, total))
print('precision:', correct/total)
print(datetime.now())
