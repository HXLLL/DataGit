import cv2
import sys
import os
import random
from tqdm import tqdm

percent = 0.01

bar = tqdm(os.listdir(sys.argv[1]))
bar.set_description("Transforming")

for f in bar:
    if f == ".datagit":
        continue
    f_dir = os.path.join(sys.argv[1], f)
    img = cv2.imread(f_dir)

    num = int(img.shape[0] * img.shape[1] * percent)

    for i in range(num):
        x = random.randint(0, img.shape[0] - 1)
        y = random.randint(0, img.shape[1] - 1)
        if random.randint(0, 1) == 0:
            img[x][y] = 0
        else:
            img[x][y] = 255

    cv2.imwrite(f_dir, img)

bar.close()