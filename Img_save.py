
import cv2

# Read the image
image = cv2.imread("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/vikram.jpg", 1)

if image is None:
    print("Error: Could not read the image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray_image)
    
    # Wait for any key to be pressed to close all windows
    wait = cv2.waitKey(0)
    
    if wait==ord('s'):
        print("Saved")
        cv2.imwrite("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/vikram.png",gray_image )  # Save the image with the correct extension
    else:
        print("Not saved")
    
    # Close all windows
    cv2.destroyAllWindows()
    