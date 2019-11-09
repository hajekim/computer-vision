""" Disparity map """
import cv2
import matplotlib.pyplot as plt


""" Load dataset """
fpath = '/mnt/hgfs/store1/bypark/test_ComVis/4_stereo/'

img_L = cv2.imread(fpath + 'im0.png', cv2.IMREAD_GRAYSCALE)
img_R = cv2.imread(fpath + 'im1.png', cv2.IMREAD_GRAYSCALE)

""" Create disparity map """
nd = 64	# number of Disparities
bs = 15 # block size
stereo = ??
disparity = ??

plt.figure(figsize=(10, 5), dpi=150)
plt.subplot(1,3,1), plt.imshow(img_L, 'gray')
plt.subplot(1,3,2), plt.imshow(img_R, 'gray')
plt.subplot(1,3,3), plt.imshow(disparity)
plt.show()
