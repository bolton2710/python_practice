#Picture manipulation
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.imshow(face,cmap=plt.cm.gray)
sy, sx = face.shape
y, x = np.ogrid[0:sy, 0:sx]
centerx, centery = (660,300)
mask = (((y - centery)/1.4)**2 + (x - centerx)**2) > 230**2
face[mask] = 0
plt.imshow(face)
