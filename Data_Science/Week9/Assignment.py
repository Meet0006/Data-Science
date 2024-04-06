import cv2
# Add cv2
img = cv2.imread('images/img1.jpg')  # Read Image

# new_img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)  # HLS Image
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # Gray Image

# img[:, :, 2] = 0
resize_img = cv2.resize(img, (256, 256))

# r_c = img[:,:,0]
cv2.imshow('Image', resize_img)  # Show Image
cv2.waitKey(0)  # Hold Image for the Infinite time

print(resize_img.shape)  # Check Resolution and channel like (Black & White(2), Grayscale(0, 255) and RGB(0, 255) * 3)
