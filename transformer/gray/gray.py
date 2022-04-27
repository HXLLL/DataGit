import cv2
import sys
import os
import random
from tqdm import tqdm

percent = 0.01

for f in tqdm(os.listdir(sys.argv[1])):
    if f == ".datagit":
        continue
    f_dir = os.path.join(sys.argv[1], f)
    img = cv2.imread(f_dir)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f_dir, gray)