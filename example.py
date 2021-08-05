# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, img = cap.read()
#     if ret:  # <<<<< этот параметр вам не просто так выдают
#         cv2.imshow("camera", img)
#     if cv2.waitKey(10) & 0xFF == 27:  # <<<<< 0xFF
#         break
#
# cap.release()
# cv2.destroyAllWindows()