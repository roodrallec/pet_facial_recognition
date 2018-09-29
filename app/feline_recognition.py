import argparse
import cv2

DEFAULT_CASCADE = "haarcascade_frontalcatface.xml"


def detect_face(image, cascade=DEFAULT_CASCADE):
    # load the input image and convert it to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the cat detector Haar cascade, then detect cat faces in the input image
    detector = cv2.CascadeClassifier(cascade)
    rectangles = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))

    # loop over the cat faces and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rectangles):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # show the detected cat faces
    cv2.imshow("Cat Faces", image)
    cv2.waitKey(0)
