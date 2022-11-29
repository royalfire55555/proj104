import cv2 as cv

img = cv.imread("./solar-system.jpg")

cv.putText(
    img,
    "Sun",
    (20, 300),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Mercury",
    (130, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.3,
    (255, 255, 255)
)

cv.putText(
    img,
    "Venus",
    (200, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Earth",
    (300, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Mars",
    (400, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Jupiter",
    (500, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Saturn",
    (800, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Uranus",
    (1000, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.putText(
    img,
    "Neptune",
    (1200, 250),
    cv.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv.imshow("output", img)


cv.waitKey(0)
cv.destroyAllWindows()
