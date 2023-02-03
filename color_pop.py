import cv2
import numpy as np

def color_pop(img_path, strength=100):
    # Load the image
    img = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert grayscale image
    gray = 255 - gray

    # Normalize the grayscale image
    gray = gray.astype("float32") / 255

    # Apply a contrast filter
    gray = cv2.pow(gray, strength / 100)

    # Convert the grayscale image back to 8-bit
    gray = np.uint8(gray * 255)

    # Blur the grayscale image
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Blend the original image and the grayscale image
    output = img.astype("float32") * gray[..., None] / 255
    output = np.uint8(output)

    return output

img = color_pop("input.jpg")
cv2.imwrite("output_pop.jpg", img)
