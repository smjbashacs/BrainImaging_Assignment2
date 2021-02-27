import matplotlib.pyplot as plt

# Reading Brain.jpg image to numpy array
img_array = plt.imread('Brain.jpg')

# Finding the dimensions of the image
print("Dimensions of image :", img_array.shape)

# Displaying the image from img_array
plt.imshow(img_array)
plt.show()

# Using reverse colormap to display image properly
plt.imshow(img_array, cmap='Greys_r')
plt.show()
