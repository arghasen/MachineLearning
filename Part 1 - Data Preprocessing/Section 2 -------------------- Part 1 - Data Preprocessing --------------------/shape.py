#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:39:51 2018

@author: argha
"""

# reshape 1D array
from numpy import array
from numpy import reshape
# define array
data = array([11, 22, 33, 44, 55])
print(data.shape)
# reshape
data1 = data.reshape((data.shape[0], 1))
print(data1.shape)