import matplotlib.pyplot as plt
img_array = plt.imread('Brain.jpg')
print("Dimensions of image :", img_array.shape)
plt.imshow(img_array)
plt.show()
plt.imshow(img_array, cmap='Greys_r')
plt.show()
