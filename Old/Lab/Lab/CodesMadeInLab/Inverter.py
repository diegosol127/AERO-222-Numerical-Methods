# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:36:20 2021

@author: allendavism
"""

import numpy as np
import scipy.linalg as linalg

b6 = [-1,3,5,-6,3]
Amat = np.array([[3,4,7,-1,4],
				 [6,-2,0,2,-2],
				 [4,1,-1,2,4],
				 [2,10,-6,-4,1],
				 [5,3,-1,-8,3]])


[m,n] = np.shape(Amat)
Amat2 = Amat
for jj in range(m):
	for ii in range(n):
		if ii > jj and abs(Amat[jj][jj]) > 1e-10:
			Amat[ii][:] = Amat[ii][:] - Amat[ii][jj]/Amat[jj][jj]*Amat[jj][:]
			print(Amat)
			breakpoint()

# for jj in range(m):
# 	for ii in range(n):
# 		if ii < jj and abs(Amat2[jj][jj]) > 1e-10:
# 			Amat2[ii][:] = Amat2[ii][:] - Amat2[ii][jj]/Amat2[jj][jj]*Amat2[jj][:]
# 			print(Amat2)
# 			breakpoint()

# LU6 = linalg.lu(Amat)
# Ainv = np.linalg.inv(Amat)
# x6 = linalg.solve(Amat,b6)

# mat = np.array([[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]])
# [m,n] = np.shape(mat)
# if m != n:
# 	break
# augMat = np.append(mat,np.eye(m),axis=1)

# for row in augMat:
# 	if row != augMat[0]:
# 		for ii in range(k):
# 			row = row - augMat[0]*row[0]/augMat[0][0]


# mat1 = mat[0]
# mat2 = mat[1]
# mat3 = mat[2]

# mat[1] = mat[1] - mat1[0]*mat[1][0]/mat[0][0]
# mat[2] = mat[2] - mat1[0]*mat[1][0]/mat[0][0]
# mat[2] = mat[1] - mat1[0]*mat[1][0]/mat[0][0]
# mat3 = mat3 - mat1*mat3[0]/mat1[0]
# mat3 = mat3 - mat2*mat3[1]/mat2[1]


# augMat = 