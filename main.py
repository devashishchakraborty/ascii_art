import cv2
import numpy as np

# Setup
IMAGE_PATH = "india-gate.jpg"
image = cv2.imread(IMAGE_PATH)
image = cv2.resize(image,(image.shape[1]//20,image.shape[0]//20), interpolation=cv2.INTER_AREA)

brightness = np.empty((image.shape[0],image.shape[1]))
ascii_image = np.empty((brightness.shape[0], brightness.shape[1]), dtype=str)


# Calculate Brightness values
for x in range(len(image)):
	for y in range(len(image[x])):
		pixel = image[x][y]
		avg = sum(pixel)//len(pixel)
		brightness[x][y] = avg

ascii_vals = ['`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

ascii_vals_brightness = {}
val = 0
increment = 255//len(ascii_vals)

for x in ascii_vals:
	ascii_vals_brightness[(val, val + increment)] = x
	val += increment + 1

for key, val in ascii_vals_brightness.items():
	for x in range(brightness.shape[0]):
		for y in range(brightness.shape[1]):
			if brightness[x][y] >= key[0] and brightness[x][y] <= key[1]:
				ascii_image[x][y] = f'{val}'

# Printing it out
for row in ascii_image:
	line = [x+x for x in row]
	print("".join(line))