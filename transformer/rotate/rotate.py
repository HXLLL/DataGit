import cv2
import sys
import os
from tqdm import tqdm

angles = [cv2.cv2.ROTATE_90_CLOCKWISE, cv2.cv2.ROTATE_180, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE]

bar = tqdm(os.listdir(sys.argv[1]))
bar.set_description("Transforming")

for f in bar:
    if f == ".datagit":
        continue
    f_dir = os.path.join(sys.argv[1], f)
    name, ext = os.path.splitext(f_dir)
    img = cv2.imread(f_dir)

    i = 1
    for a in angles:
        new = cv2.rotate(img, a)
        i += 1
        cv2.imwrite("%s_%d%s" % (name, i, ext), new)

bar.close()