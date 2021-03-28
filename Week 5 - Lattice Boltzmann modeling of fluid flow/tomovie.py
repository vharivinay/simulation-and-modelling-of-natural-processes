#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:52:49 2021

@author: harivinay
"""
import ffmpeg

import os
my_path = os.path.dirname(__file__)


import ffmpeg
(
    ffmpeg
    .input('~/Desktop/EasyAccess/Academics and Thesis/Academics/Similation and Modelling of Natural Processes/Week 6 - Particles and point-like objects/figures/*.png', pattern_type='glob', framerate=24)
    .filter('deflicker', mode='pm', size=10)
    .filter('scale', size='hd1080', force_original_aspect_ratio='increase')
    .output('galaxy_1080.mp4', crf=20, preset='slower', movflags='faststart', pix_fmt='yuv420p')
    .run()
)