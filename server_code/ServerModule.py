import anvil.server
import cv2
import numpy as np
logging = Logger(level=DEBUG, format="SERVER: {msg}")


@anvil.server.callable
def create_contour(file):
  logging.debug("create_contour")
  with anvil.media.TempFile(file) as filename:
    image = cv2.imread(filename)
  # grayed
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # make another thresh for contour
  blur = cv2.GaussianBlur(gray, (5,5), 0)
  thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
  # find contours: each contour is the outline of one shape, an array of (x, y) points.
  # RETR_EXTERNAL keeps only outermost outlines; the board border is the largest of those.
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  best_cnt = max(contours, key=cv2.contourArea, default=None)
  if best_cnt is None or cv2.contourArea(best_cnt) <= 1000:
    raise ValueError("Geen Calcudoku-rand gevonden in de foto")
  logging.debug(f"{len(contours)} contours, max_area: {cv2.contourArea(best_cnt)}")
  #
  mask = np.zeros((gray.shape),np.uint8)
  cv2.drawContours(mask,[best_cnt],0,255,-1)   #thickness -1
  cv2.drawContours(mask,[best_cnt],0,0,2)     # thickness 2
  return _to_png_media(mask, "mask.png")