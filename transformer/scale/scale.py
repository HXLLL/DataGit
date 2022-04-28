import cv2
import sys
import os
from tqdm import tqdm

scale = 0.6

bar = tqdm(os.listdir(sys.argv[1]))
bar.set_description("Transforming")

for f in bar:
    if f == ".datagit":
        continue
    f_dir = os.path.join(sys.argv[1], f)
    img = cv2.imread(f_dir)

    w = int(img.shape[1] * scale)
    h = int(img.shape[0] * scale)

    new = cv2.resize(img, (w, h))

    cv2.imwrite(f_dir, new)

bar.close()