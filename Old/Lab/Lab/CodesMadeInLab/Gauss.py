# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:52:39 2021

@author: allendavism
"""
import numpy as np

def Upper(aug):
	[n,m] = np.shape(aug)
	for jj in range(n):
		for ii in range(n):
			if ii > jj:
				aug[ii][:] = aug[ii][:] - aug[ii][jj]/aug[jj][jj]*aug[jj][:]
				aug[ii][:] = aug[ii][:]/aug[ii][jj+1]
	return aug

def Lower(aug):
	[n,m] = np.shape(aug)
	for kk in range(-n+1,1):
		for ll in range(-n+1,1):
			ii = -kk
			jj = -ll
			if ii < jj:
				aug[ii][:] = aug[ii][:] - aug[ii][jj]/aug[jj][jj]*aug[jj][:]
				aug[ii][:] = aug[ii][:]/aug[ii][jj-1]
	return aug