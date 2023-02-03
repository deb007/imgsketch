import cv2
import numpy as np

def sketch_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Blur the grayscale image to reduce high-frequency noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Perform edge detection to highlight the edges in the image
    canny_edges = cv2.Canny(blurred_image, 10, 70)
    
    # Invert the binary image
    inverted_image = cv2.bitwise_not(canny_edges)
    
    return inverted_image

# Load the input image
input_image = cv2.imread("input.jpg")

# Generate the sketch image
sketch_image = sketch_image(input_image)

# Save the sketch image
cv2.imwrite("output.jpg", sketch_image)

# Display the sketch image
cv2.imshow("Sketch Image", sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
