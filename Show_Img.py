import cv2

#read imge

image=cv2.imread("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/vikram.jpg",1)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#convert image to grayscale color

gray_image=cv2.resize(gray_image,(200,200))#resize image 1st width 2nd height

original=cv2.imshow("original",image)#show original image
cv2.imshow('Grayscale Image', gray_image)#show  gray_image image

print(image)#print image shape and size of image in pixel width and height and color channel  
cv2.waitKey(0)#wait for any key to be pressed to close all windows time in milliseconds show image
cv2.destroyAllWindows()#close all windows
