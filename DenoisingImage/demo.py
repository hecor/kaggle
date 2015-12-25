#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import *
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser(usage = 'Usage: python %prog -i input_image_path -a algorithm')
    parser.add_option('-i', '--input', type='string', action='store', dest='inp_path', default='test/1.png')
    parser.add_option('-a', '--algo', type='string', action='store', dest='algo', default='BackgroundRemoval', help=u'算法文件名，除去.py')
    (options, args) = parser.parse_args()

    inp_path = options.inp_path
    algo = options.algo
    out_path = 'output/'+inp_path.split('/')[1]
    print 'inputpath:', inp_path
    print 'outpath:', out_path

    exec('from %s import denoise_image' % (algo,))

    inp = load_image(inp_path)
    out = denoise_image(inp)

    save(out_path, out)

