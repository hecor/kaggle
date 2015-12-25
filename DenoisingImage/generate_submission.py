#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from util import *

exec('from %s import denoise_image' % (sys.argv[1],))

print 'id,value'
for root, dirs, files in os.walk('./test'):
    for f in files:
        file_id = f.split('.')[0]
        dirty_image = load_image(os.path.join(root, f))
        clean_image = denoise_image(dirty_image)
        for (x,y), value in np.ndenumerate(clean_image):
            print file_id+'_'+str(x+1)+'_'+str(y+1)+','+str(value)

