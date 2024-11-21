import cv2

# Initialize webcam
#id = input("Please enter the number ID of the webcam you want to tuse (if youre not sure input 0 to use the windows default webcam :p)")
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Webcam Live Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
