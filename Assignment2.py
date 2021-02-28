import matplotlib.pyplot as plt
from scipy import ndimage

# Reading Brain.jpg image to numpy array
img_array = plt.imread('Brain.jpg')

# Finding the dimensions of the image
print("Dimensions of image :", img_array.shape)

# Displaying the image from img_array
plt.imshow(img_array)
plt.title('Image without colormap reversing')
plt.show()

# Using reverse colormap to display image properly
plt.imshow(img_array, cmap='Greys_r')
plt.title('Image after reversing colormap')
plt.show()

# plotting the histogram for image after flatttening
plt.hist(img_array.flatten(), bins=10)
plt.title('Histogram of image after flattening')
plt.show()

# plotting the histogram for image without flattening
plt.hist(img_array, bins=10)
plt.title('Histogram of image without flattening')
plt.show()

# Applying guassian filter for image smoothing with sigma values = 5,10,20,30,40,50
sigmavalues = [5, 10, 20, 30, 40, 50]
for sigma in sigmavalues:
    image_smooth = ndimage.gaussian_filter(img_array, sigma=sigma)
    # Displaying image after smoothing
    plt.imshow(image_smooth)
    plt.title('Smoothed image with sigma: ' + str(sigma))
    plt.show()

    # Displaying histogram for smoothed image
    plt.hist(image_smooth.flatten(), bins=10)
    plt.title('Histogram of smoothed image with sigma :' + str(sigma))
    plt.show()
